import bbParser as parser
from bbSymbols import Assignment
from random import choice
from ValueMemory import LoadValues


class BuiltinError(Exception):
    pass


class Builtin:
    def __init__(self, sourceTextArg):
        self.ast = parser.parse(sourceTextArg)
        self.values = set()
        self.headfile = ''
        self.pycode = ''
        self.comment = ''
        self.tailfile = ''

    def initialize(self):
        self.LookupVaribale(self.ast)
        mapping = self.BuiltHeadFile()
        self.BuiltPythonCode(self.ast)
        self.BuiltComment(mapping)
        self.BuiltTailFile(mapping)

    def LookupVaribale(self, node):
        if node.token == None:
            for i in node.children:
                self.LookupVaribale(i)
        elif node.token.cargo == 'while':
            identifierNode = node.children[0]
            self.values.add(identifierNode.token.cargo)
            for i in identifierNode.children:
                self.LookupVaribale(i)
        elif node.token.cargo in Assignment:
            identifierNode = node.children[0]
            self.values.add(identifierNode.token.cargo)
        else:
            BuiltinError("Varibale Error")

    def BuiltPythonCode(self, node):
        if node.token == None:
            self.pycode += '\n'
            for i in node.children:
                self.BuiltPythonCode(i)
        elif node.token.cargo == 'while':
            identifierNode = node.children[0]
            self.pycode += '\t' * (node.level // 2) + 'while ' + identifierNode.token.cargo + ' != 0:\n'
            for i in identifierNode.children:
                self.BuiltPythonCode(i)
        elif node.token.cargo == 'clear':
            identifierNode = node.children[0]
            self.pycode += '\t' * (node.level // 2) + identifierNode.token.cargo + ' = 0\n'
        elif node.token.cargo == 'incr':
            identifierNode = node.children[0]
            self.pycode += '\t' * (
                        node.level // 2) + identifierNode.token.cargo + ' = ' + identifierNode.token.cargo + ' + 1\n'
        elif node.token.cargo == 'decr':
            identifierNode = node.children[0]
            self.pycode += '\t' * (node.level // 2) + identifierNode.token.cargo + ' = ' \
                           + identifierNode.token.cargo + ' - 1 if ' + identifierNode.token.cargo + ' > 0 else 0\n'
        else:
            BuiltinError("Builtin Error")

    def MappingValue(self):
        keys = set(LoadValues().keys())
        mapping = dict()
        for v in self.values:
            if len(keys) == 0:
                BuiltinError("Memory Full Error")
            random_key = choice(list(keys))
            mapping[v] = random_key
            keys.remove(random_key)
        return mapping

    def BuiltHeadFile(self):
        self.headfile += '\n'.join(["from ValueMemory import LoadValues, WriteValues", "value = LoadValues()"])
        mapping = self.MappingValue()
        for k, v in mapping.items():
            self.headfile += '\n' + k + " = " + "value['" + v + "']"
        return mapping

    def BuiltComment(self, mapping):
        self.comment += "'''"
        for k, v in mapping.items():
            self.comment += '\n' + k + ": " + v
        self.comment += '\n' + "'''"

    def BuiltTailFile(self, mapping):
        for k, v in mapping.items():
            self.tailfile += "value['" + v + "']" + " = " + k + '\n'
        self.tailfile += "WriteValues(value)"

    def ToPython(self):
        fullpycode = '\n'.join([self.headfile, self.pycode, self.comment, self.tailfile])
        return fullpycode
