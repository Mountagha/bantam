from expressions.expression import Expression
from lexer import TokenType

"""
A postfix unary arithmetic expression like "a!".
"""

class PostfixExpression(Expression):
    def __init__(self, operator: TokenType, left: Expression) -> None:
        super().__init__()
        self.mOperator = operator
        self.mLeft = left
    
    def __repr__(self) -> str:
        return f" {self.mLeft.__repr__()} {str(self.mOperator)} "
 
