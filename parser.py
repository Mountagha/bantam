from __future__ import annotations
from typing import TYPE_CHECKING, Union
from token import Token, TokenType
from expressions.expression import Expression
from precedence import Precedence
from lexer import Lexer
from typing import List
if TYPE_CHECKING:   # to handle circular import.
    from parselets.prefix_parselet import PrefixParselet
    from parselets.infix_parselet import InfixParselet

class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.mTokens = tokens
        self.mPrefixParselets = {}
        self.mInfixParselets = {}
        self.index = 0
    
    def registerPrefix(self, token: TokenType, parselet: PrefixParselet) -> None:
        self.mPrefixParselets[token] = parselet
    
    def registerInfix(self, token: TokenType, parselet: InfixParselet) -> None:
        self.mInfixParselets[token] = parselet

    def parseExpression(self, precedence: Precedence = Precedence.LOWEST) -> Expression: 
        token = self.consume()
        if token.mtype not in self.mPrefixParselets.keys(): 
            raise Exception(f"Could not parse \"{str(token)}\".")

        left = self.mPrefixParselets[token.mtype].parse(self, token)

        token = self.lookAhead(0)
        while precedence <= self._getPrecedence():
            token = self.consume()
            if token.mtype not in self.mInfixParselets.keys():
                print(f"in while and cond {token}")
                left = self.mInfixParselets[token.mtype].parse(self, left, token)
        return left 

    def consume(self, expected: TokenType = None) -> Token:
        token = self.mTokens[self.index]
        if expected and token.mtype != expected:
            raise RuntimeError(f"Expected token {str(expected)} and \
            found {str(token.mtype)}")
        self.index += 1
        return token
    
    def lookAhead(self, distance: int) -> Token: 
        if self.index + distance < len(self.mTokens):
            return self.mTokens[distance + self.index]
        raise IndexError("lookahead out of range of token's sequence")
    
    def match(self, expected: TokenType) -> bool:
        token = self.consume()
        if (token.mtype != expected):
            return False
        return True 

    def _getPrecedence(self):
        current_token = self.lookAhead(0)
        if current_token.mtype in self.mInfixParselets.keys():
            x = self.mInfixParselets[current_token.mtype].getPrecedence()
            print(f"{current_token} has precedence {x}")
            return self.mInfixParselets[current_token.mtype].getPrecedence()
        print(f"{current_token} has no precedence")
        return Precedence.LOWEST
