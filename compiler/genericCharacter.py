ENDMARK = "\0"


class Character:
	def __init__(self, c, lineIndex, colIndex, sourceIndex, sourceText):
		self.cargo = c
		self.sourceIndex = sourceIndex
		self.lineIndex = lineIndex
		self.colIndex = colIndex
		self.sourceText = sourceText

	def __str__(self):
		cargo = self.cargo
		if cargo == " ":
			cargo = "   space"
		elif cargo == "\n":
			cargo = "   newline"
		elif cargo == "\t":
			cargo = "   tab"
		elif cargo == ENDMARK:
			cargo = "   eof"

		return str(self.lineIndex).rjust(6) + str(self.colIndex).rjust(4) + "  " + cargo
