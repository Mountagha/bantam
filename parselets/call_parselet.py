from parselets.infix_parselet import InfixParselet
from expressions.expression import Expression
from expressions.call_expression import CallExpression
from precedence import Precedence
from parser import Parser
from Token import Token
from token_type import TokenType

"""
Parselet to parse a function call like "a(b, c, d)"
"""

class CallParselet(InfixParselet):
    def __init__(self) -> None:
        super().__init__()

    def getPrecedence(self):
        return Precedence.CALL
    
    def parse(self, parser: Parser, left: Expression, token: Token):
        # parse the comma separated arguments until we hit, ")"
        args = []
        
        # There may be not arguments at all
        if not parser.peek(TokenType.RIGHT_PAREN):
            while True:
                args.append(parser.parseExpression())
                if parser.peek(TokenType.RIGHT_PAREN):
                    parser.consume(TokenType.RIGHT_PAREN)
                    break
                parser.consume(TokenType.COMMA)
        return CallExpression(left, args) 
