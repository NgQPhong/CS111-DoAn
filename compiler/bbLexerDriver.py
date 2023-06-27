import bbLexer as lexer
from bbSymbols import EOF


def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")


def main(sourceText):
	global f
	f = open(outputFilename, "w")
	writeln("Here are the tokens returned by the lexer:")

	lexer.initialize(sourceText)

	while True:
		token = lexer.get()
		writeln(token.show(True))
		if token.type == EOF:
			break
	f.close()


if __name__ == "__main__":
	outputFilename = "bbLexerDriver_output.txt"
	sourceFilename = "bbExample.txt"
	sourceText = open(sourceFilename).read()
	main(sourceText)
	print(open(outputFilename).read())
