from parselets.assign_parselet import AssignParselet
from parselets.call_parselet import CallParselet
from parselets.conditional_parselet import ConditionalParselet
from parselets.group_parselet import GroupParselet
from parselets.name_parselet import NameParselet
from parselets.binary_operator_parselet import BinaryOperatorParselet
from parselets.postfix_operator_parselet import PostfixOperatorParselet
from parselets.prefix_operator_parselet import PrefixOperatorParselet
from precedence import Precedence
from token_type import TokenType
from parser import Parser

"""
Extends the generic Parser class with support for parsing the actual
bantam grammar.
"""
class BantamParser(Parser):
    def __init__(self, tokens) -> None:
        super().__init__(tokens)

        # Register all of the parselets for the grammar.

        # Register the ones that need special parselets
        super().registerPrefix(TokenType.NAME, NameParselet())
        super().registerInfix(TokenType.ASSIGN, AssignParselet())
        super().registerInfix(TokenType.QUESTION, ConditionalParselet())
        super().registerPrefix(TokenType.LEFT_PAREN, GroupParselet())
        super().registerInfix(TokenType.LEFT_PAREN, CallParselet())

        # Register the simple operator parselets
        self.prefix(TokenType.PLUS, Precedence.PREFIX)
        self.prefix(TokenType.MINUS, Precedence.PREFIX)
        self.prefix(TokenType.TILDE, Precedence.PREFIX)
        self.prefix(TokenType.BANG, Precedence.PREFIX)

        # for kicks, we'll make "!" both prefix and postfix, kind of line ++
        self.postfix(TokenType.BANG, Precedence.POSTFIX)

        self.infixLeft(TokenType.PLUS, Precedence.SUM)
        self.infixLeft(TokenType.MINUS, Precedence.SUM)
        self.infixLeft(TokenType.ASTERIK, Precedence.PRODUCT)
        self.infixLeft(TokenType.SLASH, Precedence.EXPONENT)
        self.infixRight(TokenType.CARET, Precedence.EXPONENT)



    """
    Registers a postfix unary operator parselet for  the given token
    and precedence.
    """
    def postfix(self, token:TokenType, precedence: Precedence):
        super().registerInfix(token, PostfixOperatorParselet(precedence))

    """
    Registers a prefix unary operator parselet for the given token
    and precedence.
    """
    def prefix(self, token:TokenType, precedence: Precedence):
        super().registerPrefix(token, PrefixOperatorParselet(precedence))

    """
    Registers a left-associative binary operator parselet for the given
    token and precedence
    """
    def infixLeft(self, token:TokenType, precedence: Precedence):
        super().registerInfix(token, BinaryOperatorParselet(precedence, False))

    """
    Registers a right-associative binary operator parselet for the given
    token and precedence
    """
    def infixRight(self, token:TokenType, precedence: Precedence):
        super().registerInfix(token, BinaryOperatorParselet(precedence, True))
