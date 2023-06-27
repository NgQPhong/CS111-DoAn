import genericScanner as scanner


def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")


def main(sourceText):
	global f
	f = open(outputFilename, "w")

	writeln("Here are the characters returned by the scanner:")
	writeln("  line col  character")

	scanner.initialize(sourceText)

	character = scanner.get()

	while True:
		writeln(character)
		if character.cargo == scanner.ENDMARK: break
		character = scanner.get()

	f.close()


if __name__ == "__main__":
	outputFilename = "bbgenericScannerDriver_output.txt"
	sourceText = open("bbExample.txt").read()
	main(sourceText)
	print(open(outputFilename).read())
