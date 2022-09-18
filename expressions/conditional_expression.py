from expressions.expression import Expression

"""
A ternary conditional expression like "a ? b : c".
"""

class ConditionalExpression(Expression):
    def __init__(self, condition: Expression, thenArm: Expression, elseArm: Expression) -> None:
        super().__init__()
        self.mCondition = condition
        self.mThenArm = thenArm
        self.mElseArm = elseArm
    
    def __repr__(self) -> str:
        return f"({self.mCondition.__repr__()} ? {self.mThenArm.__repr__()} : {self.mElseArm.__repr__()})"
 
