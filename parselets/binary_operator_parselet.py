from infix_parselet import InfixParselet
from expressions.expression import Expression
from expressions.operator_expression import OperatorExpression
from parser import Parser
from token import Token

"""
Generic infix parselet for a binary arithmetic operator. The only
difference when parsing, "+", "-", "*", "/", and "^" is precedence and
associativity, so we can use a single parselet class for all of those.
"""

class BinaryOperatorParselet(InfixParselet):
    def __init__(self, precedence: int, mIsRight: bool) -> None:
        super().__init__()
        self.mPrecedence = precedence
        self.mIsRight = mIsRight

    @property
    def precedence(self):
        return self.mPrecedence
    
    def parse(self, parser: Parser, left: Expression, token: Token) -> Expression:
        """
        To handle right-associative operators like "^", we allow a slightly 
        lower precedence when parsing the right hand side. this will let
        a parselet with the same precedence appear on the right, which will
        then take *this* parselet's result as its left-hand argument.
        """ 
        right = parser.parseExpression(self.mPrecedence)
        return OperatorExpression(left, token.mtype, right)

 
