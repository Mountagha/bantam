from expressions.expression import Expression 
from parser import Parser
from Token import Token
"""
One of the two parselet interfaces used by the Pratt parser. A PrefixParselet is 
associated with a token that appears at the beginning of an expression. Its
parse() method will be called with the consumed leading token, and the 
parselet is responsible for parsing anything that comes after that token.
this interface is also used for single-token expressions like variables, in
which case parse() simply doesn't consume any more tokens
original @author: rnystrom. Rewritten by @Mountagha 
"""

class PrefixParselet:
    def parse(parser: Parser, token: Token) -> Expression:
        pass
    
    def getPrecedence(self):
        pass
    

