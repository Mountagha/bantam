from enum import Enum

class TokenType(Enum):
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    COMMA = 3
    ASSIGN = 4
    PLUS = 5
    MINUS = 6
    ASTERIK = 7
    SLASH = 8
    CARET = 9
    TILDE = 10
    BANG = 11
    QUESTION = 12
    COLON = 13
    NAME= 14
    EOF= 15

    def __str__(self):
        return str(self.name)