from enum import Enum

"""
Defines the different precedence levels used by the infix parsers. These
determine how a series of infix expressions will be grouped. For example,
"a + b * c - d" will be parsed as "(a + (b * c)) - d" because "*" has 
higher precedence than "+" and "-". Here, bigger numbers mean higher precedence.
"""
class Precedence(Enum):
    LOWEST=0,
    ASSIGNMENT=1,
    CONDITIONAL=2,
    SUM=3,
    PRODUCT=4,
    EXPONENT=5,
    PREFIX=6,
    POSTFIX=7,
    CALL=8