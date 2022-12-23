import sys
import os

sys.path.insert(0, os.getcwd() + '/..')

from export_ast import ast_to_dict
import pytest
import ast


@pytest.mark.parametrize("code, expected", [
    ("print('Hello World!')",
     {"Module": {"body": [{"Expr": {"value": {"Call": {"func": {"Name": {"id": "print", "ctx": "Load()"}}, "args": [{"Constant": {"value": "Hello World!"}}], "keywords": []}}}}], "type_ignores": []}})
])
def test_code(code, expected):
    tree = ast.parse(code)
    got1 = ast_to_dict(tree)
    assert got1 == expected

    tree_str = ast.dump(tree, indent=2)
    got2 = ast_to_dict(tree_str)
    assert got2 == expected

    assert got1 == got2
