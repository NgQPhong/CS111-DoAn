from tkinter import *
from Textbase import Textbase
from RunCode import RunCode
from Output import Output
from CodeOutput import CodeOutput
from MemoryOutput import MemoryOutput


class FullOutput(Textbase):
    def __init__(self, app):
        self.app = Frame(app.app)
        self.font = app.font
        self.color = app.color
        self.output = Output(self)
        self.code = CodeOutput(self)
        self.memory = MemoryOutput(self)
        self.run = RunCode(self)

    def render(self):
        self.run.render()
        self.code.render()
        self.memory.render()
        self.output.render()
        self.app.pack(side=TOP, fill=BOTH, expand=True, pady=(2, 0))
