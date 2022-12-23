# Export AST

Export a Python abstract syntax tree to a dictionary/json.

## Usage

```bash
pip install export-ast
```

```py
import ast
from export_ast import ast_to_dict

code = "print('Hello World!')"
tree = ast.parse(code)

d = ast_to_dict(tree)

# Or as AST string (indent must be >0)...
tree_str = ast.dump(tree, indent=2)
d = ast_to_dict(tree_str)
```

## Example

### Python

```py
def hello_world():
    print('Hello World!')

if __name__ == '__main__':
    hello_world()
```

### Abstract Syntax Tree

```py
Module(
  body=[
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
              Constant(value='Hello World!')],
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

### Dictionary

```json
{
  "Module": {
    "body": [
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
                        "ctx": "Load"
                      }
                    },
                    "args": [
                      {
                        "Constant": {
                          "value": "Hello World!"
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
                  "ctx": "Load"
                }
              },
              "ops": [
                "Eq"
              ],
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
                        "ctx": "Load"
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
