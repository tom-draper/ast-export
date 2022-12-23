import sys
import os

sys.path.insert(0, os.getcwd() + '/..')
import ast
import pytest
from export_ast import ast_to_dict


@pytest.mark.parametrize('code, expected', [
    ('print("Hello World!")',
     {'Module': {'body': [{'Expr': {'value': {'Call': {'func': {'Name': {'id': 'print', 'ctx': 'Load'}}, 'args': [{'Constant': {'value': 'Hello World!'}}], 'keywords': []}}}}], 'type_ignores': []}}),
    ('x = 15',
     {'Module': {'body': [{'Assign': {'targets': [{'Name': {'ctx': 'Store', 'id': 'x'}}], 'value': {'Constant': {'value': 15}}}}], 'type_ignores': []}}),
    ('x = 15.0',
     {'Module': {'body': [{'Assign': {'targets': [{'Name': {'ctx': 'Store', 'id': 'x'}}], 'value': {'Constant': {'value': 15.0}}}}], 'type_ignores': []}}),
    ('x = 15.0\ny = 30',
     {'Module': {'body': [{'Assign': {'targets': [{'Name': {'id': 'x', 'ctx': 'Store'}}], 'value': {'Constant': {'value': 15.0}}}}, {'Assign': {'targets': [{'Name': {'id': 'y', 'ctx': 'Store'}}], 'value': {'Constant': {'value': 30}}}}], 'type_ignores': []}}),
])
def test_code(code, expected):
    tree = ast.parse(code)
    got1 = ast_to_dict(tree)
    assert got1 == expected

    tree_str = ast.dump(tree, indent=2)
    got2 = ast_to_dict(tree_str)
    assert got2 == expected

    assert got1 == got2
