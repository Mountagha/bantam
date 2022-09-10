from expressions.expression import Expression, PrefixExpression
from prefix_parselet import PrefixParselet
from parser import Parser
from token import Token


"""
Generic prefix parselet for an unary arithmetic operator. Parses prefix
unary "-", "+", "~", "!" expressions.
"""

class PrefixOperatorParselet(PrefixParselet):
    def __init__(self, precedence: int) -> None:
        super().__init__()
        self.mPrecedence = precedence

    @property
    def precedence(self):
        return self.mPrecedence
    
    def parse(self, parser: Parser, token: Token) -> Expression:
        """
        To handle right-associative operators like "^", we allow a slightly 
        lower precedence when parsing the right hand side. this will let
        a parselet with the same precedence appear on the right, which will
        then take *this* parselet's result as its left-hand argument.
        """ 
        right = parser.parseExpression(self.mPrecedence)
        return PrefixExpression(token.mtype, right)


