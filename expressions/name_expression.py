# from expression import Expression
from expressions.expression import Expression

"""
A simple variable name expression like "abc"
"""

class NameExpression(Expression):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.mName = name
    
    @property
    def name(self):
        return self.mName
    
    def __repr__(self) -> str:
        return self.mName
