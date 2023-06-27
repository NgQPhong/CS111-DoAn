from tkinter import *
from Code import Code
from FullOutput import FullOutput
from Menu import Menu
import Utilities as bbu
import os
import string
from ValueMemory import LoadValues, ValueJoin, SplitValue, WriteValues, ReWriteMemory
from bbCompiler import Compiler


class Editor:
    TITLE = "{} - Barebones IDE"
    filepath = ""
    outputfile = ""
    font = ("Courier New", 16)

    color = dict({
        "fg": "#000000",
        "bg": "#ffffff",
        "digit": "#098658",
        "control": "#af00db",
        "builtin": "#267f99",
    })

    def __init__(self) -> None:
        self.app = Tk()
        self.app.geometry("800x600")
        self.app.title(self.TITLE.format("Untitled"))

        self.code = Code(self)
        self.fulloutput = FullOutput(self)
        self.menu = Menu(self, self.code.input.text, self.code.memory.text)

        def bind_insensitive(modifier, k, callback):
            self.app.bind("<{}-{}>".format(modifier, k.upper()), callback)
            self.app.bind("<{}-{}>".format(modifier, k.lower()), callback)

        bind_insensitive("Control", "n", self.file_new)
        bind_insensitive("Control", "o", self.file_open)
        bind_insensitive("Control", "s", self.file_save)
        bind_insensitive("Control-Alt", "s", self.file_saveas)

        bind_insensitive("Control", "z", self.code_undo)
        bind_insensitive("Control-Shift", "z", self.code_redo)
        bind_insensitive("Control-Alt", "x", self.code.input.clear)
        bind_insensitive("Control", "f", self.code_find)

        bind_insensitive("Control", "l", self.load_value)
        bind_insensitive("Control", "w", self.write_value)
        bind_insensitive("Control-Shift", "w", self.rewrite_value)

        self.app.bind("<Key>", self.code_colidx)
        self.app.bind("<Control-F9>", self.code_compile)
        self.app.bind("<Control-F10>", self.Run)
        self.app.bind("<F9>", self.code_execute)
        self.app.bind("<F10>", self.run_load)
        self.app.bind("<Control-F11>", self.write_run_load)
        self.app.bind("<F11>", self.write_built_run_load)

    def code_colidx(self, event=None):
        self.code_color(event)
        self.code_index(event)
        self.code_memory_index(event)

    def code_color(self, event=None):
        def config_color(words, clr):
            self.code.input.text.tag_delete(clr)

            for word in words:
                start_pos = "1.0"
                while True:
                    start_pos = self.code.input.text.search(word, start_pos, stopindex=END)
                    if not start_pos:
                        break
                    end_pos = f"{start_pos}+{len(word)}c"
                    row, column = start_pos.split(".")

                    if "#" not in self.code.input.text.get(f"{row}.0", start_pos):
                        prev_char = self.code.input.text.get(f"{start_pos}-1c", start_pos).upper()
                        next_char = self.code.input.text.get(end_pos, f"{end_pos}+1c").upper()
                        if prev_char not in string.ascii_uppercase and next_char not in string.ascii_uppercase or \
                                start_pos == "1.0":
                            self.code.input.text.tag_add(clr, start_pos, end_pos)
                    start_pos = end_pos

            self.code.input.text.tag_config(clr, foreground=clr)

        digit_word = list(map(str, range(10)))
        control_word = ("while", "do", "not", "end")
        builtin_word = ("incr", "decr", "clear")

        config_color(digit_word, self.color["digit"]  )
        config_color(control_word, self.color["control"])
        config_color(builtin_word, self.color["builtin"])

        self.code.input.text.tag_delete("comment")

        start_pos = "1.0"
        while True:
            start_pos = self.code.input.text.search("#", start_pos, stopindex=END)
            if not start_pos:
                break
            row, column = start_pos.split(".")
            end_pos = f"{row}.end"
            self.code.input.text.tag_add("comment", start_pos, end_pos)
            start_pos = end_pos

        self.code.input.text.tag_config("comment", foreground="#828c9b")

    def code_index(self, event=None):
        num_lines = max(1, self.code.input.get().count('\n'))
        self.code.input.index.configure(state=NORMAL)
        self.code.input.index.delete(1.0, END)
        self.code.input.index.insert(END, ''.join(map(lambda i: "{:3d} ".format(i+1), range(num_lines))))
        self.code.input.index.configure(state=DISABLED)

        Y, _ = self.code.input.text.yview()
        self.code.input.index.yview_moveto(Y)

    def code_memory_index(self, event=None):
        num_lines = max(1, self.code.memory.get().count('\n'))
        self.code.memory.index.configure(state=NORMAL)
        self.code.memory.index.delete(1.0, END)
        self.code.memory.index.insert(END, ''.join(map(lambda i: "{:3d} ".format(i+1), range(num_lines))))
        self.code.memory.index.configure(state=DISABLED)

        Y, _ = self.code.memory.text.yview()
        self.code.memory.index.yview_moveto(Y)

    def code_output_index(self, event=None):
        num_lines = max(1, self.fulloutput.code.get().count('\n'))
        self.fulloutput.code.index.configure(state=NORMAL)
        self.fulloutput.code.index.delete(1.0, END)
        self.fulloutput.code.index.insert(END, ''.join(map(lambda i: "{:3d} ".format(i+1), range(num_lines))))
        self.fulloutput.code.index.configure(state=DISABLED)

        Y, _ = self.fulloutput.code.text.yview()
        self.fulloutput.code.index.yview_moveto(Y)

    def file_new(self, event=None):
        self.code.input.clear()
        self.code_index(event)
        self.app.title(self.TITLE.format("Untitiled"))

    def file_open(self, event=None):
        def callback(filepath, content):
            self.code.input.set(content)
            self.code_colidx()

            self.filepath = filepath
            filename = os.path.basename(self.filepath)

            self.app.title(self.TITLE.format(filename))
            self.fulloutput.output.text.config(state=NORMAL)
            self.fulloutput.output.set("LOADED::{}".format(filename))
            self.fulloutput.output.text.config(state=DISABLED)
        try:
            bbu.AskOpenFile(callback)
            return True
        except:
            return False

    def file_saveas(self, event=None):
        def callback(filepath):
            self.filepath = filepath
            self.app.title(self.TITLE.format(os.path.basename(filepath)))

        try:
            bbu.AskSaveFile(self.code.input.get(), callback)
        except:
            return False
        return True

    def file_save(self, event=None):
        try:
            if self.filepath:
                bbu.SaveFile(self.filepath, self.code.input.get())
            else: self.file_saveas(event)
        except:
            return False
        return True

    def code_undo(self, event=None):
        self.code.input.text.edit_undo()
        self.code_colidx(event)

    def code_redo(self, event=None):
        self.code.input.text.edit_redo()
        self.code_colidx(event)

    def code_find(self, event=None):
        def find():
            word = find_input.get()
            self.code.input.text.tag_remove("match", "1.0", END)
            matches = 0
            if word:
                start_pos = "1.0"
                while True:
                    start_pos = self.code.input.text.search(word, start_pos, stopindex=END)
                    if not start_pos:
                        break
                    end_pos = f"{start_pos}+{len(word)}c"
                    self.code.input.text.tag_add("match", start_pos, end_pos)
                    matches +=  1
                    start_pos = end_pos
                    self.code.input.text.tag_config("match", foreground="red", background="yellow")

        def replace():
            word = find_input.get()
            replace_text = replace_input.get()
            content = self.code.input.text.get(1.0, END)
            new_content = content.replace(word, replace_text)
            self.code.input.text.delete(1.0, END)
            self.code.input.text.insert(1.0, new_content)
            self.code_color()

        find_dialogue = Toplevel()
        find_dialogue.geometry("450x250+500+200")
        find_dialogue.title("Find")
        find_dialogue.resizable(0, 0)

        find_frame = LabelFrame(find_dialogue, text="Find/Replace")
        find_frame.pack(pady=20)

        text_find_label = Label(find_frame, text="Find : ")
        text_replace_label = Label(find_frame, text= "Replace")

        find_input = Entry(find_frame, width=30)
        replace_input = Entry(find_frame, width=30)

        find_button = Button(find_frame, text="Find", command=find)
        replace_button = Button(find_frame, text= "Replace", command=replace)

        text_find_label.grid(row=0, column=0, padx=4, pady=4)
        text_replace_label.grid(row=1, column=0, padx=4, pady=4)

        find_input.grid(row=0, column=1, padx=4, pady=4)
        replace_input.grid(row=1, column=1, padx=4, pady=4)

        find_button.grid(row=2, column=0, padx=8, pady=4)
        replace_button.grid(row=2, column=1, padx=8, pady=4)

        find_dialogue.mainloop()

    def load_value(self):
        try:
            value = LoadValues()
            text = ValueJoin(value)
            self.code.memory.number.delete(1.0, END)
            self.code.memory.number.insert(END, str(len(value)))
            self.code.memory.set(text)
            self.code_memory_index()
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set("Load Value Complete")
            self.fulloutput.memory.text.config(state=DISABLED)
        except Exception as E:
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set(str(E))
            self.fulloutput.memory.text.config(state=DISABLED)

    def write_value(self):
        try:
            WriteValues(SplitValue(self.code.memory.get()))
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set("Write Value Complete")
            self.fulloutput.memory.text.config(state=DISABLED)
        except Exception as E:
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set(str(E))
            self.fulloutput.memory.text.config(state=DISABLED)

    def rewrite_value(self):
        try:
            n = int(self.code.memory.number.get(1.0, END))
            ReWriteMemory(n)
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set("ReWrite Value Complete")
            self.fulloutput.memory.text.config(state=DISABLED)
        except Exception as E:
            self.fulloutput.memory.text.config(state=NORMAL)
            self.fulloutput.memory.set(str(E))
            self.fulloutput.memory.text.config(state=DISABLED)

    def code_compile(self):
        try:
            filename = os.path.basename(self.filepath)[:-3]
            outputfile, text = Compiler(self.filepath, "OutputFiles", filename)
            self.outputfile = outputfile
            self.fulloutput.code.text.config(state=NORMAL)
            self.fulloutput.code.set(text)
            self.fulloutput.code.text.config(state=DISABLED)
        except Exception as E:
            self.fulloutput.code.text.config(state=NORMAL)
            self.fulloutput.code.set(str(E))
            self.fulloutput.code.text.config(state=DISABLED)
        self.code_output_index()

    def Run(self):
        if not os.path.isfile(self.outputfile):
            self.fulloutput.run.text.config(state=NORMAL)
            self.fulloutput.run.set("File is not built yet")
            self.fulloutput.run.text.config(state=DISABLED)
        else:
            try:
                pycode = open(self.outputfile, 'r').read()
                exec(pycode)
                self.fulloutput.run.text.config(state=NORMAL)
                self.fulloutput.run.set("Running Success")
                self.fulloutput.run.text.config(state=DISABLED)
            except Exception as E:
                self.fulloutput.run.text.config(state=NORMAL)
                self.fulloutput.run.set(str(E))
                self.fulloutput.run.text.config(state=DISABLED)

    def code_execute(self):
        self.code_compile()
        self.Run()

    def run_load(self):
        self.Run()
        self.load_value()

    def write_run_load(self):
        self.write_value()
        self.Run()
        self.load_value()

    def write_built_run_load(self):
        self.write_value()
        self.code_compile()
        self.Run()
        self.load_value()

    def render(self) -> None:
        self.code.render()
        self.fulloutput.render()

        self.menu.render(self.app)
        self.app.mainloop()

