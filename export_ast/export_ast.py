import ast
import json
import re


def _enclosed_calls(parsed_ast: str) -> str:
    """Wraps ast function-type calls in braces.
       FunctionCall(...) => {FunctionCall(...)}
       Excludes leaf node calls  with no content (e.g. Load(), Store()).
       Results in the creation of JSON object elements within lists.

       Input:
           body=[
               ImportFrom(
                   module='pprint',
                   names=[
                       alias(name='pprint')],
                       level=0),
               Import(
                   names=[
                       alias(name='ast')])
           ]
       Output:
           body=[
               {ImportFrom(
                   module='pprint',
                   names=[
                       {alias(name='pprint')}],
                   level=0)},
               {Import(
                   names=[
                       {alias(name='ast')}])}
           ]
    """
    while (match := re.search(r'[ =]\w+\([^\)]', parsed_ast)):
        start_idx = match.start(0)+1
        depth = 1
        for i in range(match.end(0), len(parsed_ast)):
            char = parsed_ast[i]
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth == 0:
                    end_idx = i
                    break

        parsed_ast = parsed_ast[:start_idx] + \
            '{' + parsed_ast[start_idx:end_idx+1] + '}' + \
            parsed_ast[end_idx+1:]

    # Finally, wrap entire Module(...) call (uncaught by regex)
    parsed_ast = '{' + parsed_ast + '}'

    return parsed_ast


def value_placeholders(parsed_ast: str) -> tuple[str, list[str]]:
    """Replace multi-word strings with placeholders $str0$, $str1$, $str2$,..."""
    strings = []
    # while (match := re.search(r'\'(.*)\'', parsed_ast)):
    while (match := re.search(r'{value:([^\(][^}]*)}', parsed_ast)):
        parsed_ast = parsed_ast[:match.start(0)+7] + f'({len(strings)})' + parsed_ast[match.end(0)-1:]
        value = match.group(1)
        # If string, use double quotation marks
        if value[0] == '\'' and value[-1] == '\'':
            value = f'\"{value[1:-1]}\"'
        strings.append(value)

    return parsed_ast, strings


def replace_values(parsed_ast: str, strings: list[str]) -> str:
    """Replace string placeholders with their original strings."""
    for i, string in enumerate(strings):
        parsed_ast = re.sub(f'"\({i}\)"', string, parsed_ast)
    return parsed_ast


def _ast_to_dict(parsed_ast: str) -> str:
    parsed_ast = _enclosed_calls(parsed_ast)

    parsed_ast = re.sub(r'=', r':', parsed_ast)
    parsed_ast = re.sub(r'\(', r'{', parsed_ast)
    parsed_ast = re.sub(r'\)', r'}', parsed_ast)
    parsed_ast = re.sub(r'{}', r'', parsed_ast)
    # Temp extract any literal values
    parsed_ast, values = value_placeholders(parsed_ast)
    parsed_ast = re.sub('\'', '', parsed_ast)
    # Apply double quotation marks to all words
    parsed_ast = re.sub(r'([\w.\(\)]+)', r'"\1"', parsed_ast)
    # Replace extracted literal values
    parsed_ast = replace_values(parsed_ast, values)
    parsed_ast = re.sub(r'"{', r'":{', parsed_ast)

    return parsed_ast


def ast_to_dict(node_or_string) -> dict:
    """Converts an AST in node or string format into a dictionary."""
    if type(node_or_string) != str:
        node_or_string = ast.dump(node_or_string, indent=1)
    
    node_or_string = _ast_to_dict(node_or_string)
    
    try:
        d = json.loads(node_or_string)
    except json.decoder.JSONDecodeError:
        raise ValueError('Input code invalid')
    return d
