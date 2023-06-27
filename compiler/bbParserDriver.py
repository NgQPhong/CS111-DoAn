import bbParser as parser


if __name__ == "__main__":
	outputFilename = "bbParserDriver_output.txt"
	sourceFilename = "bbExample.txt"
	sourceText = open(sourceFilename).read()
	ast = parser.parse(sourceText)
	with open(outputFilename, 'w') as f:
		f.write(ast.toString())
	print(open(outputFilename).read())
