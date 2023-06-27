from bbBuiltin import Builtin
from os.path import isfile, isdir


class CompilerError(Exception):
    pass


def Compiler(filepath, outputpath, filename):
    if not isfile(filepath):
        raise CompilerError("File Path Error")
    compiler = Builtin(open(filepath, 'r').read())
    compiler.initialize()
    output = '\n'.join([compiler.headfile, compiler.pycode, compiler.comment, compiler.tailfile])
    if not isdir(outputpath):
        raise CompilerError("Output Path Error")
    outputfile = outputpath + '/' + filename + ".py"
    with open(outputfile, 'w') as f:
        f.write(output)
    return outputfile, '\n'.join([compiler.pycode, compiler.comment])
