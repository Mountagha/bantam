from typing import List
from expressions.expression import Expression

"""
A function call like "a(b, c, d)"
"""

class CallExpression(Expression):
    def __init__(self, function: Expression, args: List[Expression]) -> None:
        super().__init__()
        self.mFunction = function
        self.mArgs = args
    
    def __repr__(self) -> str:
        args = ", ".join(arg.__repr__() for arg in self.mArgs)
        return f"{self.mFunction.__repr__()}({args})"