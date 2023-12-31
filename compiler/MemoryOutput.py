from tkinter import *
from Textbase import Textbase


class MemoryOutput(Textbase):
    def __init__(self, app):
        self.frame = Frame(app.app)

        self.text = Text(self.frame, wrap=WORD, font=app.font, background=app.color["bg"], foreground=app.color["fg"],
                         width=50, height=2, highlightthickness=0, bd=0)
        self.text.insert(1.0, "Your Memory output will be displayed here")
        self.text.config(tabs=4, insertofftime=0, insertbackground="Red", insertwidth=4, state=DISABLED)
        self.text.pack(side=LEFT, fill=X, pady=(4, 0), expand=True)

    def render(self):
        self.frame.pack(side=RIGHT, fill=BOTH)