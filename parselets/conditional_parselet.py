from parselets.infix_parselet import InfixParselet
from expressions.expression import Expression
from expressions.conditional_expression import ConditionalExpression
from precedence import Precedence
from parser import Parser
from token import Token
from token_type import TokenType

"""
Parselet for the condition or "ternary" operator, like "a ? b : c".
"""

class ConditionalParselet(InfixParselet):
    def __init__(self) -> None:
        super().__init__()

    def parse(self, parser: Parser, left: Expression, token: Token):
        thenArm = parser.parseExpression()
        parser.consume(TokenType.COLON)
        elseArm = parser.parseExpression(Precedence.CONDITIONAL - 1)
        return ConditionalExpression(left, thenArm, elseArm)

    def getPrecedence(self):
        return Precedence.CONDITIONAL 

