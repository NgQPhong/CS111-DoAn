from genericScanner import *


class LexerError(Exception):
    pass


class Token:
    def __init__(self, startChar):
        self.cargo = startChar.cargo
        self.sourceText = startChar.sourceText
        self.lineIndex = startChar.lineIndex
        self.colIndex = startChar.colIndex
        self.type = None

    def show(self, showLineNumbers=False, **kwargs):
        align = kwargs.get("align", True)
        if align:
            tokenTypeLen = 12
            space = " "
        else:
            tokenTypeLen = 0
            space = ""

        if showLineNumbers:
            s = str(self.lineIndex).rjust(6) + str(self.colIndex).rjust(4) + "  "
        else:
            s = ""

        if self.type == self.cargo:
            s = s + "Symbol".ljust(tokenTypeLen, ".") + ":" + space + self.type
        elif self.type == "Whitespace":
            s = s + "Whitespace".ljust(tokenTypeLen, ".") + ":" + space + repr(self.cargo)
        else:
            s = s + self.type.ljust(tokenTypeLen, ".") + ":" + space + self.cargo
        return s

    guts = property(show)

    def abort(self, msg):
        lines = self.sourceText.split("\n")
        sourceLine = lines[self.lineIndex]
        raise LexerError("\nIn line " + str(self.lineIndex + 1) + " near column " + str(self.colIndex + 1) +
                         ":\n\n" + sourceLine.replace("\t", " ") + "\n" + " " * self.colIndex + "^\n\n" + msg)
