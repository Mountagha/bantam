from bantam_parser import BantamParser
from lexer import Lexer

# some turn-around to avoid creating fixtures for pytest.

def parse_string(source: str) -> str:
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

def test_unary_precedence():
    # Unary precedence.
    assert parse_string("~!-+a") == "(~(!(-(+a))))"
    assert parse_string("a!!!") == "(((a!)!)!)"

def test_unary_and_binary_precedence():
    # Unary and binary precedence.
    assert parse_string("-a * b") == "((-a) * b)"
    assert parse_string("!a + b") == "((!a) + b)"
    assert parse_string("~a ^ b") == "((~a) ^ b)"
    assert parse_string("-a!") ==  "(-(a!))"
    assert parse_string("!a!") ==  "(!(a!))"  

def test_binary_precedence():
    # binary precedence.
    assert parse_string("a = b + c * d ^ e - f / g") == "(a = ((b + (c * (d ^ e))) - (f / g)))"

def test_binary_associativity():
    # binary associativity.
    assert parse_string("a = b = c") == "(a = (b = c))"
    assert parse_string("a + b - c") == "((a + b) - c)"
    assert parse_string("a * b / c") == "((a * b) / c)"
    assert parse_string("a ^ b ^ c") == "(a ^ (b ^ c))"

def test_conditional_operator():
    # Conditional operator.
    assert parse_string("a ? b : c ? d : e") == "(a ? b : (c ? d : e))"
    assert parse_string("a ? b ? c : d : e") == "(a ? (b ? c : d) : e)"
    assert parse_string("a + b ? c * d : e / f") == "((a + b) ? (c * d) : (e / f))"

def test_grouping():
    # Grouping.
    assert parse_string("a + (b + c) + d") == "((a + (b + c)) + d)"
    assert parse_string("a ^ (b + c)") == "(a ^ (b + c))"
    assert parse_string("(!a)!") == "((!a)!)"

if __name__ == "__main__":
    test_call()
    test_unary_precedence()
    test_unary_and_binary_precedence()
    test_binary_precedence()
    test_binary_associativity()
    test_conditional_operator()
    test_grouping()
