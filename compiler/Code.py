from tkinter import *
from Textbase import Textbase
from Input import Input
from Memory import Memory


class Code(Textbase):
    def __init__(self, app):
        self.app = Frame(app.app)
        self.font = app.font
        self.color = app.color
        self.input = Input(self)
        self.memory = Memory(self)

    def render(self):
        self.input.render()
        self.memory.render()
        self.app.pack(side=TOP, fill=BOTH, expand=True, pady=(2, 0))
