from re import match
from lpp.token import (
    Token,
    TokenType,
)

class Lexer:

    def __init__(self, source: str) -> None:
        self._source: str = source
        self._character: str = ''
        self._read_position: int = 0
        self._position: int = 0

        self._read_character()

    def next_token(self) -> Token:
        token_dict = {
            "^=$": TokenType.ASSIGN,
            "^\+$": TokenType.PLUS,
            "^\($": TokenType.LPAREN,
            "^\)$": TokenType.RPAREN,
            "^{$": TokenType.LBRACE,
            "^}$": TokenType.RBRACE,
            "^,$": TokenType.COMMA,
            "^;$": TokenType.SEMICOLON,
            "^$": TokenType.EOF,
        }
        token = None

        for regex, token_type in token_dict.items():
            if match(regex, self._character):
                token = Token(token_type, self._character)
                break
        
        if token is None:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()

        return token
    
    def _read_character(self) -> None:
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]

        self._position = self._read_position
        self._read_position += 1