from parselets.infix_parselet import InfixParselet
from expressions.expression import Expression
from expressions.operator_expression import OperatorExpression
from precedence import Precedence
from parser import Parser
from token import Token

"""
Generic infix parselet for a binary arithmetic operator. The only
difference when parsing, "+", "-", "*", "/", and "^" is precedence and
associativity, so we can use a single parselet class for all of those.
"""

class BinaryOperatorParselet(InfixParselet):
    def __init__(self, precedence: Precedence, mIsRight: bool) -> None:
        super().__init__()
        self.mPrecedence = precedence
        self.mIsRight = mIsRight
    
    def parse(self, parser: Parser, left: Expression, token: Token) -> Expression:
        """
        To handle right-associative operators like "^", we allow a slightly 
        lower precedence when parsing the right hand side. this will let
        a parselet with the same precedence appear on the right, which will
        then take *this* parselet's result as its left-hand argument.
        """ 
        right = parser.parseExpression(self.mPrecedence - (1 if self.mIsRight else 0))
        return OperatorExpression(left, token.mtype, right)

    def getPrecedence(self):
        return self.mPrecedence
