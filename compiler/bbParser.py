import bbLexer as lexer
from bbSymbols import *
from genericAstNode import Node


class ParserError(Exception):
    pass


def dq(s):
    return '"%s"' % s


verbose = True
token = None
indent = 0


def getToken():
    global token
    if verbose:
        if token:
            print(("  " * indent) + "   (" + token.show(align=False) + ")")
    token = lexer.get()


def push(s):
    global indent
    indent += 1
    if verbose:
        print((" >" * indent) + " " + s)


def pop(s):
    global indent
    if verbose:
        print((" <" * indent) + " " + s)
    indent -= 1


def track0(func):
    def newfunc():
        push(func.__name__)
        func()
        pop(func.__name__)
    return newfunc


def track(func):
    def newfunc(node):
        push(func.__name__)
        func(node)
        pop(func.__name__)

    return newfunc


def error(msg):
    token.abort(msg)


def foundOneOf(argTokenTypes):
    for argTokenType in argTokenTypes:
        print("foundOneOf", argTokenType, token.type)
        if token.type == argTokenType:
            return True
    return False


def found(argTokenType):
    if token.type == argTokenType:
        return True
    return False


def consume(argTokenType):
    if token.type == argTokenType:
        getToken()
    else:
        error("expecting to find " + dq(argTokenType)
              + " but found " + token.show(align=False))


def parse(sourceText, **kwargs):
    global lexer, verbose
    verbose = kwargs.get("verbose",False)
    lexer.initialize(sourceText)
    getToken()
    program()
    if verbose:
        print("~"*80)
        print("Successful parse!")
        print("~"*80)
    return ast


@track0
def program():
    global ast
    node = Node()
    statement(node)
    while not found(EOF):
        statement(node)
    consume(EOF)
    ast = node


@track
def statement(node):
    if found("while"):
        loopStatement(node)
    else:
        assignmentStatement(node)
        
@track
def assignmentStatement(node):
    operatorNode = Node(token)
    consume(ASSIGN)
    
    identifierNode = Node(token)
    consume(IDENTIFIER)
    
    node.addNode(operatorNode)

    operatorNode.addNode(identifierNode)

    consume(";")


@track
def loopStatement(node):
    loopNode = Node(token)
    consume("while")

    identifierNode = Node(token)
    consume(IDENTIFIER)

    consume("not")
    consume(ZERO)
    consume("do")

    node.addNode(loopNode)
    loopNode.addNode(identifierNode)
    while not found("end"):
        statement(identifierNode)

    consume("end")
    consume(";")