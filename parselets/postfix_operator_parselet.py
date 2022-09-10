from expressions.expression import Expression
from expressions.postfix_expression import PostfixExpression
from parselets.infix_parselet import InfixParselet
from precedence import Precedence
from parser import Parser
from token import Token


"""
Generic infix parselet for an unary arithmetic operator. Parses postfix
unary "?" expressions.
"""

class PostfixOperatorParselet(InfixParselet):
    def __init__(self, precedence: Precedence) -> None:
        super().__init__()
        self.mPrecedence = precedence

    def parse(self, parser: Parser, left: Expression, token: Token) -> Expression:
        return PostfixExpression(token.mtype, left)

    def getPrecedence(self):
        return self.mPrecedence

