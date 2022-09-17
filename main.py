from bantam_parser import BantamParser
from lexer import Lexer
import pytest

# some turn-around to avoid creating fixtures for pytest.

def parse_string(source: str) -> None:
    lexer = Lexer(source)
    lexer.tokenize()
    parser = BantamParser(lexer.get_tokens())
    return str(parser.parseExpression())

def test_call():
    # function call
    assert parse_string("a()") == "a()"
    assert parse_string("a(b)") == "a(b)"
    assert parse_string("a(b, c)") == "a(b, c)"
    assert parse_string("a(b)(c)") == "a(b)(c)"
    assert parse_string("a(b) + c(d)") == "(a(b) + c(d))"
    assert parse_string("a(b ? c : d, e + f)") == "a((b ? c : d), (e + f))"

if __name__ == "__main__":
    lexer = Lexer("a(b)")
    #lexer = Lexer("-a + b * c")
    lexer.tokenize()
    tokens = lexer.get_tokens()
    print(tokens)
    parser = BantamParser(tokens)
    print(parser.parseExpression())
    # test_call()