from expressions.expression import Expression
from lexer import TokenType

"""
A prefix unary arithmetic expression like "!a" or "-b"
"""

class PrefixExpression(Expression):
    def __init__(self, operator: TokenType, right: Expression) -> None:
        super().__init__()
        self.mOperator = operator
        self.mRight = right
    
    def __repr__(self) -> str:
        return f"({str(self.mOperator)}{self.mRight.__repr__()})"
 
