from parselets.prefix_parselet import PrefixParselet
from expressions.expression import Expression
from expressions.call_expression import CallExpression
from parser import Parser
from Token import Token
from token_type import TokenType

"""
Parses parentheses used to group an expression, like "a * (b + c)
"""

class GroupParselet(PrefixParselet):
    def parse(self, parser: Parser, token: Token) -> Expression:
        expression = parser.parseExpression()
        parser.consume(TokenType.RIGHT_PAREN)
        return expression

