from parselets.infix_parselet import InfixParselet
from expressions.expression import Expression
from expressions.name_expression import NameExpression
from expressions.assign_expression import AssignExpression
from precedence import Precedence
from parser import Parser
from token import Token
from token_type import TokenType

"""
Parses assignment expression like "a = b". The left side of an assignment
expression must be a simple name like "a", and expressions are right-associative.
(In other words, "a = b = c" is parsed as "a = (b = c)")
"""

class AssignParselet(InfixParselet):

    def parse(parser: Parser, left: Expression, token: Token) -> Expression:
        right = parser.parseExpression(Precedence.ASSIGNMENT - 1)
        if not isinstance(left, NameExpression):
            raise Exception("the left hand side of an assignment must be a name.")
        
        return AssignExpression(str(left), right) 
    
    def getPrecedence(self):
        return Precedence.ASSIGNMENT