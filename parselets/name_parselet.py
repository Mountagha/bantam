from expressions.expression import Expression, NameExpression
from prefix_parselet import PrefixParselet
from parser import Parser
from token import Token


class NameParselet(PrefixParselet):
    """
    Simple parselet for a named variable like "abc".
    """
    def __init__(self) -> None:
        super().__init__()
    
    def parse(self, parser: Parser, token: Token) -> Expression:
        return NameExpression(token.mtype) 


