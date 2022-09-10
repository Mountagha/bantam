from bantam_parser import BantamParser
from lexer import Lexer

if __name__ == "__main__":
    # lexer = Lexer("-+~!a")
    lexer = Lexer("-a + b")
    lexer.tokenize()
    tokens = lexer.get_tokens()
    print(tokens)
    parser = BantamParser(tokens)
    print(parser.parseExpression())