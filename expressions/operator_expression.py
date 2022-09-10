from lexer import TokenType
from expression import Expression


class OperatorExpression(Expression):
    def __init__(self, left: Expression, operator: TokenType, right: Expression) -> None:
        super().__init__()
        self.mLeft = left
        self.mOperator = operator
        self.mRight = right

    def __repr__(self) -> str:
        return f"({self.mLeft.__repr__()} {str(self.mOperator)} {self.mRight.__repr__()})"