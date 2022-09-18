from curses.ascii import isalnum
from Token import Token
from token_type import TokenType

class Lexer: 
    def __init__(self, mText: str) -> None:
        self.mPunctuators = [] # list of tuples
        self.mText = mText
        self.index = 0 # to go through the text.

    def get_token_name(self):
        identifer = ""
        while self.index < len(self.mText) and isalnum(self.mText[self.index]):
            identifer += self.mText[self.index]
            self.index += 1
        self.mPunctuators.append(Token(TokenType.NAME, identifer))

    def tokenize(self):
        while self.index < len(self.mText):
            char = self.mText[self.index]
            if char == '(':
                self.mPunctuators.append(Token(TokenType.LEFT_PAREN, char))
            elif char == ')':
                self.mPunctuators.append(Token(TokenType.RIGHT_PAREN, char))
            elif char == ',':
                self.mPunctuators.append(Token(TokenType.COMMA, char))
            elif char == '=':
                self.mPunctuators.append(Token(TokenType.ASSIGN, char)) 
            elif char == '+':
                self.mPunctuators.append(Token(TokenType.PLUS, char))
            elif char == '-':
                self.mPunctuators.append(Token(TokenType.MINUS, char))
            elif char == '*':
                self.mPunctuators.append(Token(TokenType.ASTERIK, char))
            elif char == '/':
                self.mPunctuators.append(Token(TokenType.SLASH, char))
            elif char == '^':
                self.mPunctuators.append(Token(TokenType.CARET, char))
            elif char == '~':
                self.mPunctuators.append(Token(TokenType.TILDE, char))
            elif char == '!':
                self.mPunctuators.append(Token(TokenType.BANG, char)) 
            elif char == '?':
                self.mPunctuators.append(Token(TokenType.QUESTION, char))
            elif char == ':':
                self.mPunctuators.append(Token(TokenType.COLON, char))
            elif isalnum(char):
                self.get_token_name()
                continue # to avoid double increment
            else:
                self.index += 1
                continue # ignore all other char
            self.index += 1

        self.mPunctuators.append(Token(TokenType.EOF, None))

    def get_tokens(self):
        return self.mPunctuators
    