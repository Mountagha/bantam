from expressions.expression import Expression

"""
An assignment expression lke "a = b"
"""

class AssignExpression(Expression):
    def __init__(self, name: str, left: Expression) -> None:
        super().__init__()
        self.mName = name
        self.mLeft = left
    
    def __repr__(self) -> str:
        return f"({self.mName} = {self.mLeft.__repr__()})"