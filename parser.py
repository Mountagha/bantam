from __future__ import annotations
from typing import TYPE_CHECKING
from token import Token, TokenType
from expressions.expression import Expression
from lexer import Lexer
from typing import List, overload
if TYPE_CHECKING:   # to handle circular import.
    from parselets.prefix_parselet import PrefixParselet

class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.mTokens = tokens
        self.mPrefixParselets = {}
        self.mRead = []
        self.index = 0
    
    def register(self, token: TokenType, parselet: PrefixParselet) -> None:
        self.mPrefixParselets[token] = parselet
    

    # @overload
    # def register(self, token: TokenType, parselet: InfixParselet) -> None:
    #    pass
    
    def parseExpression(self, precedence: int = 0) -> Expression: 
        token = self.consume()
        if token.mtype not in self.mPrefixParselets.keys(): 
            raise Exception(f"Could not parse \"{str(token)}\".")

        left = self.mPrefixParselets[token.mtype].parse(self, token)
        return left
     
    def consume(self, expected: TokenType = None) -> Token:
        token = self.mTokens[self.index]
        if expected and token.mtype != expected:
            raise RuntimeError(f"Expected token {str(expected)} and \
            found {str(token.mtype)}")
        self.index += 1
        return token
    
    def lookAhead(self, distance: int) -> Token: 
        if distance < len(self.mTokens):
            return self.mTokens[distance]
        raise IndexError("lookahead out of range of token's sequence")
    
    def match(self, expected: TokenType) -> bool:
        token = self.consume()
        if (token.mtype != expected):
            return False
        return True 


