"""solve module"""
import ast
import operator


def solve(expr: str) -> int:
    """solve_"""
    binops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.floordiv,
        ast.Mod: operator.mod
    }
    node = ast.parse(expr, mode='eval')

    def _eval(node):
        if isinstance(node, ast.Expression):
            result = _eval(node.body)
        elif isinstance(node, ast.Str):
            result = node.s
        elif isinstance(node, ast.Num):
            result = node.n
        elif isinstance(node, ast.BinOp):
            result = binops[type(node.op)](_eval(node.left), _eval(node.right))
        else:
            raise Exception('Unsupported type {}'.format(node))
        return result

    return _eval(node)
