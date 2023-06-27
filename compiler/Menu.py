import tkinter

from Icon import Icon
from tkinter import LEFT


class Menu:
    def __init__(self, app, text_editor, memory_editor):
        self.icon = Icon()
        self.menu = tkinter.Menu(app.app, bd=0)
        theme_choice = tkinter.StringVar()

        sub_file = tkinter.Menu(self.menu, tearoff=False)
        sub_edit = tkinter.Menu(self.menu, tearoff=False)
        sub_memory = tkinter.Menu(self.menu, tearoff=False)
        sub_theme = tkinter.Menu(self.menu, tearoff=False)
        sub_go = tkinter.Menu(self.menu, tearoff=False)

        def change_theme():
            chosen_theme = theme_choice.get()
            color_tuple = color_dict.get(chosen_theme)
            fg_color, bg_color = color_tuple[0], color_tuple[1]
            text_editor.config(background=bg_color, fg=fg_color)

        color_icons = (self.icon.get("light_default"), self.icon.get("light_plus"), self.icon.get("dark"),
                       self.icon.get("red"), self.icon.get("monokai"), self.icon.get("night"))

        color_dict = {
            "Light Default": ("#000000", "#ffffff"),
            "Light Plus": ("#474747", "#e0e0e0"),
            "Dark": ("#FFFFFF", "#2d2d2d"),
            "Pink": ("#2d2d2d", "#ffe8e8"),
            "Monokai": ("#474747", "#d3b774"),
            "Night Blue": ("#ededed", "#6b9dc2")
        }

        count = 0
        for i in color_dict:
            sub_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=LEFT,
                                      command=change_theme)
            count += 1

        sub_file.add_command(label="New", image=self.icon.get("new"), compound=LEFT, accelerator="Ctrl+N",
                             command=app.file_new)
        sub_file.add_command(label="Open", image=self.icon.get("open"), compound=LEFT, accelerator="Ctrl+O",
                             command=app.file_open)
        sub_file.add_command(label="Save", image=self.icon.get("save"), compound=LEFT, accelerator="Ctrl+S",
                             command=app.file_save)
        sub_file.add_command(label="Save as", image=self.icon.get("save_as"), compound=LEFT, accelerator="Ctrl+Alt+S",
                             command=app.file_saveas)

        sub_edit.add_command(label="Copy", image=self.icon.get("copy"), compound=LEFT, accelerator="Ctrl+C",
                             command=app.code.input.text.event_generate("<Control C>"))
        sub_edit.add_command(label="Paste", image=self.icon.get("paste"), compound=LEFT, accelerator="Ctrl+V",
                             command=app.code.input.text.event_generate("<Control V>"))
        sub_edit.add_command(label="Cut", image=self.icon.get("cut"), compound=LEFT, accelerator="Ctrl+X",
                             command=app.code.input.text.event_generate("<Control X>"))
        sub_edit.add_command(label="Clear all", image=self.icon.get("clear_all"), compound=LEFT,
                             accelerator="Ctrl+Alt+X", command=app.code.input.clear)
        sub_edit.add_command(label="Undo", image=self.icon.get("undo"), compound=LEFT, accelerator="Ctrl+Z",
                             command=app.code_undo)
        sub_edit.add_command(label="Redo", image=self.icon.get("redo"), compound=LEFT, accelerator="Ctrl+Shift+Z",
                             command=app.code_redo)
        sub_edit.add_command(label="Find", image=self.icon.get("find"), compound=LEFT, accelerator="Ctrl+F",
                             command=app.code_find)

        sub_memory.add_command(label="Load", image=self.icon.get("load_memory"), compound=LEFT, accelerator="Ctrl+L",
                               command=app.load_value)
        sub_memory.add_command(label="Write", image=self.icon.get("write_value"), compound=LEFT, accelerator="Ctrl+W",
                               command=app.write_value)
        sub_memory.add_command(label="ReWrite", image=self.icon.get("rewrite_value"), compound=LEFT,
                               accelerator="Ctrl+Shift+W", command=app.rewrite_value)

        sub_go.add_command(label="Built", image=self.icon.get("built"), compound=LEFT, accelerator="Ctrl+F9",
                           command=app.code_compile)
        sub_go.add_command(label="Run", image=self.icon.get("run"), compound=LEFT, accelerator="Ctrl+F10",
                           command=app.Run)
        sub_go.add_command(label="Built&Run", image=self.icon.get("run"), compound=LEFT, accelerator="F9",
                           command=app.code_execute)
        sub_go.add_command(label="Run&Load", image=self.icon.get("run"), compound=LEFT, accelerator="F10",
                           command=app.run_load)
        sub_go.add_command(label="Write&Run&Load", image=self.icon.get("run"), compound=LEFT, accelerator="Ctrl+F11",
                           command=app.write_run_load)
        sub_go.add_command(label="Write&Built&Run&Load", image=self.icon.get("run"), compound=LEFT, accelerator="F11",
                           command=app.write_built_run_load)

        self.menu.add_cascade(label="File", menu=sub_file)
        self.menu.add_cascade(label="Edit", menu=sub_edit)
        self.menu.add_cascade(label="Memory", menu=sub_memory)
        self.menu.add_cascade(label="Theme", menu=sub_theme)
        self.menu.add_cascade(label="Go", menu=sub_go)

    def render(self, app) -> None:
        app.config(menu=self.menu)
