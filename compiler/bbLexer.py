import genericScanner as sc
from genericToken import *
from bbSymbols import *


class LexerError(Exception):
    pass


def dq(s):
    return '"%s"' % s


def getChar():
    global c1, c2, character
    character = sc.get()
    c1 = character.cargo
    c2 = c1 + sc.lookahead(1)


def initialize(sourceText):
    global sc
    sc.initialize(sourceText)
    getChar()


def get():
    while c1 in WHITESPACE_CHARS or c2 == COMMENT_STARTCHARS:
        while c1 in WHITESPACE_CHARS:
            token = Token(character)
            token.type = WHITESPACE
            getChar()
            while c1 in WHITESPACE_CHARS:
                token.cargo += c1
                getChar()

        while c2 == COMMENT_STARTCHARS:
            token = Token(character)
            token.type = COMMENT
            token.cargo = c2
            getChar()
            getChar()
            while not(c1 == COMMENT_ENDCHAR) and not(c1 == ENDMARK):
                token.cargo += c1
                getChar()

    token = Token(character)

    if c1 == ENDMARK:
        token.type = EOF
        return token

    if c1 in IDENTIFIER_STARTCHARS:
        token.type = IDENTIFIER
        getChar()
        while c1 in IDENTIFIER_CHARS:
            token.cargo += c1
            getChar()
        if token.cargo in Keywords:
            if token.cargo in Assignment:
                token.type = ASSIGN
            else:
                token.type = token.cargo
        return token

    if c1 in ZERO_CHAR and c2 not in IDENTIFIER_CHARS:
        token.type = ZERO
        getChar()
        return token

    if c1 in OneCharacterSymbols:
        token.type = token.cargo
        getChar()
        return token

    token.abort("found a character or symbol that is not recognized: " + dq(c1))