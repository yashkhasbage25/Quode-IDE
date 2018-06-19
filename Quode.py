from tkinter import Tk
from tkinter import Menu
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import _tkinter
from tkinter import Image
from tkinter import Frame
from tkinter import Toplevel
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
# from tkinter.ttk import Style
from tkinter import filedialog as fd
# from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring
from tkinter.font import Font
import os
from sys import argv

from pygments.lexers.c_cpp import CFamilyLexer
from pygments.lexers.c_cpp import CLexer
from pygments.lexers.c_cpp import CppLexer
from pygments.lexers.css import CssLexer
from pygments.lexers.css import SassLexer
from pygments.lexers.data import YamlLexer
from pygments.lexers.data import JsonLexer
from pygments.lexers.dotnet import CSharpLexer
from pygments.lexers.dotnet import FSharpLexer
from pygments.lexers.eiffel import EiffelLexer
from pygments.lexers.erlang import ErlangLexer
from pygments.lexers.fortran import FortranLexer
from pygments.lexers.go import GoLexer
from pygments.lexers.haskell import HaskellLexer
from pygments.lexers.hdl import VhdlLexer
from pygments.lexers.hdl import VerilogLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.html import XmlLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.javascript import TypeScriptLexer
from pygments.lexers.javascript import CoffeeScriptLexer
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.jvm import ScalaLexer
from pygments.lexers.jvm import KotlinLexer
from pygments.lexers.lisp import CommonLispLexer
from pygments.lexers.make import MakefileLexer
from pygments.lexers.make import CMakeLexer
from pygments.lexers.matlab import MatlabLexer
from pygments.lexers.pascal import DelphiLexer
from pygments.lexers.perl import PerlLexer
from pygments.lexers.php import PhpLexer
from pygments.lexers.prolog import PrologLexer
from pygments.lexers.python import PythonLexer
from pygments.lexers.python import Python3Lexer
from pygments.lexers.ruby import RubyLexer
from pygments.lexers.shell import BashLexer
from pygments.lexers.sql import MySqlLexer
from pygments.lexers.tcl import TclLexer
from pygments.lexers.textedit import AwkLexer

from pygments.styles import get_style_by_name


class SearchWindow(Toplevel):

    def __init__(self, master, found):
        Toplevel.__init__(self)
        self.master = master
        self.height = '100'
        self.width = '200'
        self.found = found
        self.config(bg="green")

        self.geometry(self.width+"x"+self.height+"+300+300")
        self.title("Search")
        self.configure(bg="yellow")

        self.search_img = PhotoImage(file='img/notebook/glass.png')
        self.next_img = PhotoImage(file='img/notebook/next.png')

        self.start_index = "1.0"
        self.stop_index = "end"

        self.entry = Entry(self)
        self.search_img_button = Button(self, image=self.search_img, bg="white", command=self.searchText)
        self.found_label = Label(self, text=("Found "+str(self.found)+"\ninstances"), bg="yellow")
        self.next_button = Button(self, image=self.next_img, bg='white', command=self.showNextSearch)

        self.entry.place_configure(relx=0.1, rely=0.15, relheight=0.25, relwidth=0.5)
        self.search_img_button.place_configure(relx=0.65, rely=0.0, relheight=0.5, relwidth=0.3)
        self.found_label.place_configure(relx=0.1, rely=0.5, relheight=0.4, relwidth=0.4)
        self.next_button.place_configure(relx=0.65, rely=0.5, relheight=0.5, relwidth=0.3)

        self.protocol("WM_DELETE_WINDOW", self.closeSearchWindow)

        self.mainloop()

    def searchText(self):

        curr_editor = self.master._getCurrentEditor()
        start = "1.0"
        text = self.entry.get()
        if text != '':

            curr_editor.tag_config('highlight', background='green', foreground='red')
            curr_editor.tag_config('highlight_next', background='blue', foreground='purple')
            pos = curr_editor.search(text, start, stopindex="end")

            while pos != '':
                length = len(text)
                row, col = pos.split('.')
                end = int(col) + length
                end = row + '.' + str(end)
                curr_editor.tag_add('highlight', pos, end)
                # curr_editor.see(pos)
                start = end
                pos = curr_editor.search(text, start, stopindex="end")

            pos = curr_editor.search(text, "1.0", stopindex='end')
            length = len(text)
            row, col = pos.split('.')
            end = int(col) + length
            end = row + '.' + str(end)
            curr_editor.tag_add('highlight_next', pos, end)

    def showNextSearch(self):
        """curr_editor = self.master._getCurrentEditor()
        start = "1.0"
        text = self.entry.get()
        if text != '':
            pos = curr_editor.search(text, start, stopindex="end")

            while pos != '':
                length = len(text)
                row, col = pos.split('.')
                end = int(col) + length
                end = row + '.' + str(end)
                curr_editor.tag_add('highlight', pos, end)
                curr_editor.see(pos)
                start = end
                pos = curr_editor.search(text, start, stopindex="end")
                curr_editor.tag_config('highlight', background='green', foreground='red')"""

        curr_editor = self.master._getCurrentEditor()
        # start = "1.0"
        text = self.entry.get()
        if text != '':
            pos = curr_editor.search(text, self.start_index, stopindex="end")
            if pos == '':

                self.start_index = "1.0"
                pos = curr_editor.search(text, self.start_index, stopindex="end")
            length = len(text)
            row, col = pos.split('.')
            self.stop_index = int(col) + length
            self.stop_index = row + '.' + str(self.stop_index)
            curr_editor.tag_delete('highlight_next')
            curr_editor.tag_add('highlight_next', pos, self.stop_index)
            curr_editor.tag_config('highlight_next', background='blue', foreground='purple')
            curr_editor.see(pos)
            self.start_index = self.stop_index
            pos = curr_editor.search(text, self.start_index, stopindex="end")

    def closeSearchWindow(self):

        self.master.removeAllTags()
        self.master.createTags()
        self.master.recolorize(None)
        self.destroy()


class ReplaceTextWindow(Toplevel):

    def __init__(self, master):

        Toplevel.__init__(self)
        self.master = master
        self.height = '150'
        self.width = '200'
        self.replaced = 0

        self.geometry(self.width+"x"+self.height+"+300+300")
        self.title("Replace All")
        self.configure(bg="green")

        self.find_entry = Entry(self)
        self.new_str_entry = Entry(self)
        self.find_label = Label(self, text="Replace it:", bg="green")
        self.new_str_label = Label(self, text="Replace with:", bg="green")
        self.replace_button = Button(self, text="Replace All", command=self.replaceAll)

        self.find_label.place_configure(relx=0, rely=0.1, relheight=0.2, relwidth=0.4)
        self.new_str_label.place_configure(relx=0, rely=0.5, relheight=0.2, relwidth=0.4)
        self.find_entry.place_configure(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.4)
        self.new_str_entry.place_configure(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.4)
        self.replace_button.place_configure(relx=0.3, rely=0.8, relheight=0.15, relwidth=0.4)

        self.mainloop()

    def replaceAll(self):

        self.replaces = self.master.replaceAll(self.find_entry.get(), self.new_str_entry.get())
        messagebox.showinfo("Replaced", "Replaced %d occurances" % self.replaces)


class App(Tk):

    def __init__(self, args):
        Tk.__init__(self)
        self.height = '720'
        self.width = '1280'
        self.Editors = []
        self.filenames = {}
        self._icon = Image("photo", file='img/notebook/icon.png')
        self.MainImage = PhotoImage(file='img/notebook/nbimg.gif')

        self.code_font = Font(family="FreeMono", size=15)
        self.title_font = Font(family="Ubuntu Mono", size=15)

        self.MainWindow = Frame(self, background='#ee90ee')
        self.notebook = Notebook(self)
        self.configureUI()
        self.args = args

        self.bash_img = PhotoImage(file='img/fext/bash.png')
        self.c_img = PhotoImage(file='img/fext/c.png')
        self.cs_img = PhotoImage(file='img/fext/c#.png')
        self.cpp_img = PhotoImage(file='img/fext/cpp.png')
        self.css_img = PhotoImage(file='img/fext/css.png')
        self.go_img = PhotoImage(file='img/fext/golang.png')
        self.html_img = PhotoImage(file='img/fext/html.png')
        self.java_img = PhotoImage(file='img/fext/java.png')
        self.js_img = PhotoImage(file='img/fext/js.png')
        self.perl_img = PhotoImage(file='img/fext/perl.png')
        self.php_img = PhotoImage(file='img/fext/php.png')
        self.python_img = PhotoImage(file='img/fext/python.png')
        self.ruby_img = PhotoImage(file='img/fext/ruby.png')
        self.swift_img = PhotoImage(file='img/fext/swift.png')
        self.txt_img = PhotoImage(file='img/fext/txt.png')

        self.lexers = self.createLexers()

        self.mainloop()

    def configureUI(self):

        self.configureWindow()
        self.configureMenu()
        self.configureNotebook()
        self.contextualMenu()
        self.bindWindowEvents()
        # self.createTags()

    def configureWindow(self):

        self.geometry(self.width+'x'+self.height+'+0+0')
        self.title("Quode-IDE")
        self.wm_iconphoto(False, self._icon)
        self.MainWindow.pack()

    def configureMenu(self):

        self.menu_bar = Menu(self)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New Tab', font=self.title_font, command=self.createNewEditor, accelerator='Ctrl + N')
        self.file_menu.add_command(label="Open", font=self.title_font, command=self.openFile, accelerator='Ctrl + O')
        self.file_menu.add_command(label="Save", font=self.title_font, command=self.saveFile, accelerator='Ctrl + S')
        self.file_menu.add_command(label='Remove Tab', font=self.title_font, command=self.removeCurrentEditor, accelerator='Ctrl + R')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", font=self.title_font, command=self.askQuit, accelerator='Ctrl + Q')
        self.menu_bar.add_cascade(label="File", font=self.title_font, menu=self.file_menu)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", font=self.title_font, command=self.cutSelection, accelerator="Ctrl + X")
        self.edit_menu.add_command(label="Copy", font=self.title_font, command=self.copySelection, accelerator="Ctrl + C")
        self.edit_menu.add_command(label="Paste", font=self.title_font, command=self.pasteSelection, accelerator="Ctrl + V")
        self.edit_menu.add_command(label="Replace All", font=self.title_font, command=self.replaceAllWindow)
        self.menu_bar.add_cascade(label="Edit", font=self.title_font, menu=self.edit_menu)

        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Increase Font Size", font=self.title_font, command=self.increaseFontSize, accelerator="Ctrl + +/=")
        self.view_menu.add_command(label="Decrease Font Size", font=self.title_font, command=self.decreaseFontSize, accelerator="Ctrl + -/_")
        self.view_menu.add_command(label="Find", font=self.title_font, command=self.searchWindow, accelerator="Ctrl + f")
        self.menu_bar.add_cascade(label="View", font=self.title_font, menu=self.view_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About", font=self.title_font)
        self.menu_bar.add_cascade(label="Help", font=self.title_font, menu=self.help_menu)
        self.config(menu=self.menu_bar)

    def configureNotebook(self):

        self.notebook.place_configure(relx=0, rely=0, relheight=1, relwidth=1)
        self.notebook.enable_traversal()

    # print("filenames:", self.filenames)
    # print("editors:", self.Editors)

    def langImg(self, ext):

        if (ext == '.sh'):
            return self.bash_img
        elif (ext == '.c'):
            return self.c_img
        elif(ext == '.cs'):
            return self.cs_img
        elif(ext == '.cpp'):
            return self.cpp_img
        elif(ext == '.css'):
            return self.css_img
        elif(ext == '.go'):
            return self.golang_img
        elif(ext == '.html'):
            return self.html_img
        elif(ext == '.java'):
            return self.java_img
        elif(ext == '.js'):
            return self.js_img
        elif(ext == '.pl'):
            return self.perl_img
        elif(ext == '.php'):
            return self.php_img
        elif(ext == '.py'):
            return self.python_img
        elif(ext == '.rb'):
            return self.ruby_img
        elif(ext == '.swift'):
            return self.swift_img
        else:
            return self.txt_img

    def _getCurrentEditor(self):
        try:
            index = self.notebook.index('current')
            curr_editor = self.Editors[index]

            return curr_editor

        except _tkinter.TclError:
            messagebox.showerror('Error', 'No Editors Opened!!')
            return None

    def createNewEditor(self):

        new_tab_name = askstring('New Tab', 'Enter name of new tab')
        if new_tab_name:
            f_name, ext = os.path.splitext(new_tab_name)
            scrolled_text = ScrolledText(font=self.code_font, undo=True)
            self.Editors.append(scrolled_text)
            self.filenames[scrolled_text] = None
            self.lexers[scrolled_text]
            self.notebook.add(scrolled_text, image=self.langImg(ext), text=os.path.split(new_tab_name)[1], compound='left')
            self.notebook.select(scrolled_text)
            self.createTags()
            self.recolorize(None)
            # scrolled_text.edit_separator()
            scrolled_text.focus_set()
            scrolled_text.edit_reset()
            scrolled_text.bind('<Control-z>', func=self.undoChange)
            scrolled_text.bind('<Control-y>', func=self.redoChange)

        else:
            f_name = "Untitled"
            scrolled_text = ScrolledText(font=self.code_font, undo=True)
            self.Editors.append(scrolled_text)
            self.filenames[scrolled_text] = None
            self.notebook.add(scrolled_text, image=self.langImg('.txt'), text=f_name, compound='left')
            self.notebook.select(scrolled_text)
            self.createTags()
            self.recolorize(None)
            # scrolled_text.edit_separator()
            scrolled_text.focus_set()
            scrolled_text.edit_reset()

    def openFile(self):

        opened_file_name = fd.askopenfilename(initialdir="/home/dell/YK/projects/wrong/",
                                              title="Select file",
                                              filetypes=(('all files', '*.*'),))
        if not isinstance(opened_file_name, tuple):
            ext = os.path.splitext(opened_file_name)[1]
            scrolled_text = ScrolledText(font=self.code_font, undo=True)
            self.Editors.append(scrolled_text)
            self.filenames[scrolled_text] = opened_file_name
            self.notebook.add(scrolled_text, image=self.langImg(ext), text=os.path.split(opened_file_name)[1], compound='left')
            with open(opened_file_name) as f:
                file_text = f.read()
                f.close()
                scrolled_text.insert('end', file_text)

            self.notebook.select(scrolled_text)
            self.createTags()
            self.recolorize(None)
            # self.event_generate('<Control>')
            scrolled_text.focus_set()
            scrolled_text.edit_reset()
            # scrolled_text.edit_separator()
            scrolled_text.bind('<Control-z>', func=self.undoChange)
            scrolled_text.bind('<Control-y>', func=self.redoChange)
        #print("filenames:", self.filenames)
        #print("editors:", self.Editors)

    def saveFile(self):
        try:
            editor_index = self.notebook.index('current')
            curr_editor = self.Editors[editor_index]
            curr_text = curr_editor.get("1.0", "end")
            if self.filenames[curr_editor] is not None:
                with open(self.filenames[curr_editor], 'r+') as f:
                    f.write(curr_text)
                    messagebox.showinfo('Save', 'File Saved!!!')
                    curr_editor.edit_reset()

            else:
                new_file_path = fd.asksaveasfilename(initialdir='/home/dell/YK/projects/', filetypes=[("All files", "*")])
                if not isinstance(new_file_path, tuple):

                    self.filenames[curr_editor] = new_file_path
                    new_file = open(new_file_path, 'w+')
                    new_file.close()

                    new_file = open(new_file_path, 'r+')
                    new_file.write(curr_text)
                    messagebox.showinfo('Save', 'File Saved!!!')
                    self.filenames[curr_editor] = new_file_path
                    curr_editor.edit_reset()

        except _tkinter.TclError:
            messagebox.showerror("Save File", "No file to save")
        # print("filenames:", self.filenames)
        # print("editors:", self.Editors)

    def removeCurrentEditor(self):

        try:
            curr_editor = self._getCurrentEditor()
            if messagebox.askyesno('Remove Current Tab', 'Are you sure you want to remove this Editor?', icon='warning'):
                self.notebook.forget(index)
                self.Editors.remove(curr_editor)
                self.filenames.pop(curr_editor, None)

        except _tkinter.TclError:
            messagebox.showerror('Remove Tab', 'Oops!! No tabs to remove!!')

        # print("filenames:", self.filenames)
        # print("editors:", self.Editors)

    def askQuit(self):

        if messagebox.askyesno('Remove Current Tab', 'Do you really wanna Exit?', icon='warning'):
            self.destroy()

    def bindWindowEvents(self):

        self.bind('<Control-n>', func=self.createNewEditor)
        self.bind('<Control-o>', func=self.openFile)
        self.bind('<Control-s>', func=self.saveFile)
        self.bind('<Control-r>', func=self.removeCurrentEditor)
        self.bind('<Control-q>', func=self.askQuit)
        self.bind('<Control-x>', func=self.cutSelection)
        self.bind('<Control-c>', func=self.copySelection)
        self.bind('<Control-v>', func=self.pasteSelection)
        self.bind('<Control-a>', func=self.selectAll)
        self.bind('<Control-f>', func=self.searchWindow)
        self.bind('<Control-z>', func=self.undoChange)
        self.bind('<Control-y>', func=self.redoChange)

        self.bind('<Control-N>', func=self.createNewEditor)
        self.bind('<Control-O>', func=self.openFile)
        self.bind('<Control-S>', func=self.saveFile)
        self.bind('<Control-R>', func=self.removeCurrentEditor)
        self.bind('<Control-Q>', func=self.askQuit)
        self.bind('<Control-X>', func=self.cutSelection)
        self.bind('<Control-C>', func=self.copySelection)
        self.bind('<Control-V>', func=self.pasteSelection)
        self.bind('<Control-A>', func=self.selectAll)
        self.bind('<Control-F>', func=self.searchWindow)
        self.bind('<Control-Z>', func=self.undoChange)
        self.bind('<Control-Y>', func=self.redoChange)

        self.bind('<Control-plus>', func=self.increaseFontSize)
        self.bind('<Control-minus>', func=self.decreaseFontSize)
        self.bind('<Control-KP_Add>', func=self.increaseFontSize)
        self.bind('<Control-KP_Subtract>', func=self.decreaseFontSize)

        self.bind("<Key>", func=self.recolorize)

        self.bind('<Button>', func=lambda e: self.contextual_menu.unpost())
        self.bind('<Button-3>', func=lambda e: self.contextual_menu.post(e.x_root, e.y_root))

    def cutSelection(self):

        curr_editor = self._getCurrentEditor()
        curr_editor.event_generate('<<Cut>>')

    def copySelection(self):

        curr_editor = self._getCurrentEditor()
        curr_editor.event_generate('<<Copy>>')

    def pasteSelection(self):

        curr_editor = self._getCurrentEditor()
        curr_editor.event_generate('<<Paste>>')

    def contextualMenu(self):

        self.contextual_menu = Menu(self, tearoff=False)

        self.contextual_menu.add_command(label='New Editor', command=self.createNewEditor)
        self.contextual_menu.add_command(label='Open File', command=self.openFile)
        self.contextual_menu.add_command(label='Save Editor', command=self.saveFile)
        self.contextual_menu.add_separator()
        self.contextual_menu.add_command(label='Remove Editor', command=self.removeCurrentEditor)
        self.contextual_menu.add_command(label='Change title', command=self.changeEditorTitle)
        # self.contextual_menu.add_separator()
        # self.contextual_menu.add_command(label='Increase font size', command=self.increaseFontSize)
        # self.contextual_menu.add_command(label='Decrease font size')

    def unpostContextMenu(self):

        self.contextual_menu.unpost()

    def changeEditorTitle(self):

        curr_editor = self._getCurrentEditor()
        new_title = askstring('New Editor', "Enter new title")
        new_ext = os.path.splitext(new_title)[1]
        self.notebook.tab(curr_editor, text=new_title, image=self.langImg(new_ext))

    def increaseFontSize(self):

        curr_editor = self._getCurrentEditor()
        curr_font = Font(curr_editor, curr_editor.cget("font"))
        curr_size = curr_font.cget('size')
        new_size = curr_size+1
        curr_font.configure(size=new_size)
        new_font = curr_font
        curr_editor.configure(font=new_font)
        #print(new_font, new_font.cget("size"))
        print(Font(curr_editor, curr_editor.cget("font")).cget("size"))

    def decreaseFontSize(self):

        curr_editor = self._getCurrentEditor()
        curr_font = Font(curr_editor, curr_editor.cget("font"))
        curr_size = curr_font.cget('size')
        if curr_size > 1:
            new_size = curr_size-1
            curr_font.configure(size=new_size)

    def undoChange(self, event):
        try:

            curr_editor = self._getCurrentEditor()
            # curr_editor.edit_separator()
            curr_editor.edit_undo()
            self.createTags()
            self.recolorize(None)
        except _tkinter.TclError:
            pass

    def redoChange(self, event):
        try:
            curr_editor = self._getCurrentEditor()
            curr_editor.edit_redo()
        except _tkinter.TclError:
            pass

    def selectAll(self, event):
        curr_editor = self._getCurrentEditor()
        curr_editor.tag_add('sel', '1.0', 'end')
        return "break"

    def searchWindow(self):

        self.search_window = SearchWindow(self, 0)

    def removeAllTags(self):

        curr_editor = self._getCurrentEditor()
        for tag in curr_editor.tag_names():
            curr_editor.tag_delete(tag)

    def replaceAllWindow(self):

        self.replace_window = ReplaceTextWindow(self)

    def replaceAll(self, a, b):

        curr_editor = self._getCurrentEditor()
        start = "1.0"
        text = curr_editor.get(start, "end")
        if curr_editor:
            pos = curr_editor.search(a, start, stopindex="end")

            while pos:
                length = len(text)
                row, col = pos.split('.')
                end = int(col) + length
                end = row + '.' + str(end)
                curr_editor.tag_add('found', pos, end)
                # curr_editor.see(pos)
                start = end
                pos = curr_editor.search(a, start, stopindex="end")
                # curr_editor.tag_config('found', background='green', foreground='red')
            replaced = 0
            if a:
                coordinates = []
                index_list = list(curr_editor.tag_ranges("found"))
                index_list.reverse()
                while index_list:
                    coordinates.append([index_list.pop(), index_list.pop()])
                for start, end in coordinates:
                    curr_editor.delete(start, end)
                    curr_editor.insert(start, b)
                    replaced += 1
                curr_editor.tag_delete("found")
                return replaced

    def createTags(self):
        curr_editor = self._getCurrentEditor()
        bold_font = Font(curr_editor, curr_editor.cget("font"))
        bold_font.configure(weight='bold')

        italic_font = Font(curr_editor, curr_editor.cget("font"))
        italic_font.configure(slant='italic')

        bold_italic_font = Font(curr_editor, curr_editor.cget("font"))
        bold_italic_font.configure(weight='bold', slant='italic')

        style = get_style_by_name('default')
        for ttype, ndef in style:
            # print(ttype, ndef)
            tag_font = None
            if ndef['bold'] and ndef['italic']:
                tag_font = bold_italic_font
            elif ndef['bold']:
                tag_font = bold_font
            elif ndef['italic']:
                tag_font = italic_font

            if ndef['color']:
                foreground = "#%s" % ndef['color']
            else:
                foreground = None

            curr_editor.tag_configure(str(ttype), foreground=foreground, font=tag_font)

    def recolorize(self, event):
        curr_editor = self._getCurrentEditor()
        code = curr_editor.get("1.0", "end-1c")
        lexer = PythonLexer()
        tokensource = lexer.get_tokens(text=code)
        start_line = 1
        start_index = 0
        end_line = 1
        end_index = 0
        for ttype, value in tokensource:
            if "\n" in value:
                end_line += value.count("\n")
                end_index = len(value.rsplit("\n", 1)[1])
            else:
                end_index += len(value)

            if value not in (" ", "\n"):
                index1 = "%s.%s" % (start_line, start_index)
                index2 = "%s.%s" % (end_line, end_index)

                for tagname in curr_editor.tag_names(index1):  # FIXME
                    curr_editor.tag_remove(tagname, index1, index2)

                # print(ttype, repr(value), index1, index2)
                curr_editor.tag_add(str(ttype), index1, index2)

            start_line = end_line
            start_index = end_index
        self.update()
        # print(Font(curr_editor, curr_editor.cget("font")).cget("size"))

    def createLexers(self):

        lex = {}
        lex['.c'] = CFamilyLexer()
        lex['.h'] = CFamilyLexer()
        lex['.cpp'] = CppLexer()
        lex['.hpp'] = CppLexer()
        lex['.css'] = CssLexer()
        lex['.sass'] = SassLexer()
        lex['.yaml'] = YamlLexer()
        lex['.yml'] = YamlLexer()
        lex['.json'] = JsonLexer()
        lex['.cs'] = CSharpLexer()
        lex['.fs'] = FSharpLexer()
        lex['.e'] = EiffelLexer()
        lex['.erl'] = ErlangLexer()
        lex['.hrl'] = ErlangLexer()
        lex['.es'] = ErlangLexer()
        lex['.f03'] = FortranLexer()
        lex['.f90'] = FortranLexer()
        lex['.F03'] = FortranLexer()
        lex['.F90'] = FortranLexer()
        lex['.go'] = GoLexer()
        lex['.hs'] = HaskellLexer()
        lex['.v'] = VerilogLexer()
        lex['.vhdl'] = VhdlLexer()
        lex['.vhd'] = VhdlLexer()
        lex['.html'] = HtmlLexer()
        lex['.htm'] = HtmlLexer()
        lex['.xhtml'] = HtmlLexer()
        lex['.']


def main(args):

    app = App(args)


if __name__ == '__main__':

    main(argv[1:])
