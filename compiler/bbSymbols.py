import string

Keywords = """
clear
incr
decr
while
not
do
end
"""
Keywords = Keywords.split()


Assignment = """
clear
incr
decr
"""
Assignment = Assignment.split()


OneCharacterSymbols = """
;
"""
OneCharacterSymbols = OneCharacterSymbols.split()


COMMENT_STARTCHARS = "//"
COMMENT_ENDCHAR = '\n'

IDENTIFIER_STARTCHARS = string.ascii_letters
IDENTIFIER_CHARS = string.ascii_letters + string.digits + "_"

NUMBER_STARTCHARS = string.digits
NUMBER_CHARS = string.digits + "."

ZERO_CHAR = ['0']

WHITESPACE_CHARS = " \t\n"


IDENTIFIER = "Nonterminal"
ASSIGN = "INDECL"
WHITESPACE = "Whitespace"
ZERO = "Zero"
COMMENT = "Comment"
EOF = "Eof"
