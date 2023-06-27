from genericCharacter import *


def initialize(sourceTextArg):
	global sourceText, lastIndex, sourceIndex, lineIndex, colIndex
	sourceText = sourceTextArg
	lastIndex = len(sourceText) - 1
	sourceIndex = -1
	lineIndex = 0
	colIndex = -1


def get():
	global lastIndex, sourceIndex, lineIndex, colIndex
	sourceIndex += 1
	if sourceIndex > 0:
		if sourceText[sourceIndex - 1] == "\n":
			lineIndex += 1
			colIndex = -1

	colIndex += 1

	if sourceIndex > lastIndex:
		char = Character(ENDMARK, lineIndex, colIndex, sourceIndex, sourceText)
	else:
		c = sourceText[sourceIndex]
		char = Character(c, lineIndex, colIndex, sourceIndex, sourceText)

	return char


def lookahead(offset=1):
	index = sourceIndex + offset

	if index > lastIndex:
		return ENDMARK
	else:
		return sourceText[index]
	