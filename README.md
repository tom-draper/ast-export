# AST Export

Export a Python abstract syntax tree to a dictionary/json.

## Usage

```py
import ast
from ast_export import ast_to_dict

tree = ast.parse("print('Hello World!')")

d = ast_to_dict(tree)

# Or as AST string (indent must be >0)...
tree_str = ast.dump(tree, indent=2)
d = ast_to_dict(tree_str)
```

## Example

### Python

```py
from colorama import init, Fore

init(wrap=False)

def hello_world():
    print(Fore.GREEN + 'Hello World!')

if __name__ == '__main__':
    hello_world()
```

### Abstract Syntax Tree

```py
Module(t
  body=[
    ImportFrom(
      module='colorama',
      names=[
        alias(name='init'),
        alias(name='Fore')],
      level=0),
    Expr(
      value=Call(
        func=Name(id='init', ctx=Load()),
        args=[],
        keywords=[
          keyword(
            arg='wrap',
            value=Constant(value=False))])),
    FunctionDef(
      name='hello_world',
      args=arguments(
        posonlyargs=[],
        args=[],
        kwonlyargs=[],
        kw_defaults=[],
        defaults=[]),
      body=[
        Expr(
          value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
              BinOp(
                left=Attribute(
                  value=Name(id='Fore', ctx=Load()),
                  attr='GREEN',
                  ctx=Load()),
                op=Add(),
                right=Constant(value='Hello World!'))],
            keywords=[]))],
      decorator_list=[]),
    If(
      test=Compare(
        left=Name(id='__name__', ctx=Load()),
        ops=[
          Eq()],
        comparators=[
          Constant(value='__main__')]),
      body=[
        Expr(
          value=Call(
            func=Name(id='hello_world', ctx=Load()),
            args=[],
            keywords=[]))],
      orelse=[])],
  type_ignores=[])
```

### Exporting Dictionary

```py
import ast
from pprint import pprint
from ast_export import ast_to_dict

with open('hello_world.py', 'r') as f:
    tree = ast.parse(f.read())

d = ast_to_dict(tree)

pprint(d, indent=0)
```

### Dictionary

```json
{
  "Module": {
    "body": [
      {
        "ImportFrom": {
          "module": "colorama",
          "names": [
            {
              "alias": {
                "name": "init"
              }
            },
            {
              "alias": {
                "name": "Fore"
              }
            }
          ],
          "level": 0
        }
      },
      {
        "Expr": {
          "value": {
            "Call": {
              "func": {
                "Name": {
                  "id": "init",
                  "ctx": "Load()"
                }
              },
              "args": [],
              "keywords": [
                {
                  "keyword": {
                    "arg": "wrap",
                    "value": {
                      "Constant": {
                        "value": "False"
                      }
                    }
                  }
                }
              ]
            }
          }
        }
      },
      {
        "FunctionDef": {
          "name": "hello_world",
          "args": {
            "arguments": {
              "posonlyargs": [],
              "args": [],
              "kwonlyargs": [],
              "kw_defaults": [],
              "defaults": []
            }
          },
          "body": [
            {
              "Expr": {
                "value": {
                  "Call": {
                    "func": {
                      "Name": {
                        "id": "print",
                        "ctx": "Load()"
                      }
                    },
                    "args": [
                      {
                        "BinOp": {
                          "left": {
                            "Attribute": {
                              "value": {
                                "Name": {
                                  "id": "Fore",
                                  "ctx": "Load()"
                                }
                              },
                              "attr": "GREEN",
                              "ctx": "Load()"
                            }
                          },
                          "op": "Add()",
                          "right": {
                            "Constant": {
                              "value": "Hello World!"
                            }
                          }
                        }
                      }
                    ],
                    "keywords": []
                  }
                }
              }
            }
          ],
          "decorator_list": []
        }
      },
      {
        "If": {
          "test": {
            "Compare": {
              "left": {
                "Name": {
                  "id": "__name__",
                  "ctx": "Load()"
                }
              },
              "ops": ["Eq()"],
              "comparators": [
                {
                  "Constant": {
                    "value": "__main__"
                  }
                }
              ]
            }
          },
          "body": [
            {
              "Expr": {
                "value": {
                  "Call": {
                    "func": {
                      "Name": {
                        "id": "hello_world",
                        "ctx": "Load()"
                      }
                    },
                    "args": [],
                    "keywords": []
                  }
                }
              }
            }
          ],
          "orelse": []
        }
      }
    ],
    "type_ignores": []
  }
}
```
