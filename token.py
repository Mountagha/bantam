from token_type import TokenType

class Token:
    def __init__(self, token_type: TokenType, text: str) -> None:
        self._mtype = token_type
        self._text = text

    @property
    def mtype(self):
        return self._mtype

    @property
    def text(self):
        return self._text

    def __repr__(self) -> str:
        return f"<{self._mtype}, {self._text}>"
