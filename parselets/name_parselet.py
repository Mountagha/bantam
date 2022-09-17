from expressions.expression import Expression
from expressions.name_expression import NameExpression
from parselets.prefix_parselet import PrefixParselet
from parser import Parser
from Token import Token


class NameParselet(PrefixParselet):
    """
    Simple parselet for a named variable like "abc".
    """
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, parser: Parser, token: Token) -> Expression:
        return NameExpression(token.text) 


