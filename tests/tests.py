import sys
import os

sys.path.insert(0, os.getcwd() + '/..')
import pytest
import ast
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


@pytest.mark.parametrize('file, expected', [('file1', {
    "Module": {
        "body": [
            {
                "ImportFrom": {
                    "module": "setuptools",
                    "names": [
                        {
                            "alias": {
                                "name": "setup"
                            }
                        },
                        {
                            "alias": {
                                "name": "find_packages"
                            }
                        }
                    ],
                    "level": "0"
                }
            },
            {
                "Assign": {
                    "targets": [
                        {
                            "Name": {
                                "id": "long_description",
                                "ctx": "Store"
                            }
                        }
                    ],
                    "value": {
                        "Call": {
                            "func": {
                                "Attribute": {
                                    "value": {
                                        "Call": {
                                            "func": {
                                                "Name": {
                                                    "id": "open",
                                                    "ctx": "Load"
                                                }
                                            },
                                            "args": [
                                                {
                                                    "Constant": {
                                                        "value": "README.md"
                                                    }
                                                }
                                            ],
                                            "keywords": []
                                        }
                                    },
                                    "attr": "read",
                                    "ctx": "Load"
                                }
                            },
                            "args": [],
                            "keywords": []
                        }
                    }
                }
            },
            {
                "Expr": {
                    "value": {
                        "Call": {
                            "func": {
                                "Name": {
                                    "id": "setup",
                                    "ctx": "Load"
                                }
                            },
                            "args": [],
                            "keywords": [
                                {
                                    "keyword": {
                                        "arg": "name",
                                        "value": {
                                            "Constant": {
                                                "value": "export-ast"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "version",
                                        "value": {
                                            "Constant": {
                                                "value": "1.0.5"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "author",
                                        "value": {
                                            "Constant": {
                                                "value": "Tom Draper"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "author_email",
                                        "value": {
                                            "Constant": {
                                                "value": "tomjdraper1@gmail.com"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "license",
                                        "value": {
                                            "Constant": {
                                                "value": "MIT"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "description",
                                        "value": {
                                            "Constant": {
                                                "value": "Export a Python AST to a dictionary."
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "long_description",
                                        "value": {
                                            "Name": {
                                                "id": "long_description",
                                                "ctx": "Load"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "long_description_content_type",
                                        "value": {
                                            "Constant": {
                                                "value": "text/markdown"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "url",
                                        "value": {
                                            "Constant": {
                                                "value": "https://github.com/tom-draper/ast-export"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "key_words",
                                        "value": {
                                            "Constant": {
                                                "value": "ast syntax trees export dict json dictionary"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "install_requires",
                                        "value": {
                                            "List": {
                                                "elts": [],
                                                "ctx": "Load"
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "packages",
                                        "value": {
                                            "Call": {
                                                "func": {
                                                    "Name": {
                                                        "id": "find_packages",
                                                        "ctx": "Load"
                                                    }
                                                },
                                                "args": [],
                                                "keywords": []
                                            }
                                        }
                                    }
                                },
                                {
                                    "keyword": {
                                        "arg": "python_requires",
                                        "value": {
                                            "Constant": {
                                                "value": ">:3.6"
                                            }
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        ],
        "type_ignores": []
    }
})])
def test_code_file(file, expected):
    with open(f'{file}.py', 'r') as f:
        tree = ast.parse(f.read())
        got1 = ast_to_dict(tree)
        assert got1 == expected

        tree_str = ast.dump(tree, indent=2)
        got2 = ast_to_dict(tree_str)
        assert got2 == expected

        assert got1 == got2
