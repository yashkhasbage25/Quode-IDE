from tkinter import Tk
from tkinter import Menu
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import _tkinter
from tkinter import Image
from tkinter import Frame
from tkinter import Label
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
from tkinter import filedialog as fd
from tkinter import simpledialog
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

from file_tree import FileTree
from search_window import SearchWindow
from replace_text_window import ReplaceTextWindow

class App(Tk):

    def __init__(self, args):
        Tk.__init__(self)
        self.height = '720'
        self.width = '1280'
        self.Editors = []
        self.Filenames = {}
        self.lexer_selector = self.createLexers()
        self.Lexers = dict()
        self._icon = Image("photo", file='img/notebook/icon.png')

        self.code_font = Font(family="Latin Modern Mono", size=15)
        self.title_font = Font(family="Ubuntu Mono", size=15)
        self.underline_font = Font(underline=True)

        self.MainWindow = Frame(self, background='#282c34')
        self.notebook = Notebook(self)
        self.configureUI()
        self.args = args

        self.awk_img = PhotoImage(file='img/fext/awk.png')
        self.bash_img = PhotoImage(file='img/fext/bash.png')
        self.c_img = PhotoImage(file='img/fext/c.png')
        self.cs_img = PhotoImage(file='img/fext/c#.png')
        self.cmake_img = PhotoImage(file='img/fext/cmake.png')
        self.coffee_img = PhotoImage(file='img/fext/coffee.png')
        self.cpp_img = PhotoImage(file='img/fext/cpp.png')
        self.css_img = PhotoImage(file='img/fext/css.png')
        self.delphi_img = PhotoImage(file='img/fext/delphi.png')
        self.eiffel_img = PhotoImage(file='img/fext/eiffel.png')
        self.erlang_img = PhotoImage(file='img/fext/erlang.png')
        self.fs_img = PhotoImage(file='img/fext/f#.png')
        self.fortran_img = PhotoImage(file='img/fext/fortran.png')
        self.go_img = PhotoImage(file='img/fext/golang.png')
        self.haskell_img = PhotoImage(file='img/fext/haskell.png')
        self.html_img = PhotoImage(file='img/fext/html.png')
        self.java_img = PhotoImage(file='img/fext/java.png')
        self.js_img = PhotoImage(file='img/fext/js.png')
        self.json_img = PhotoImage(file='img/fext/json.png')
        self.kotlin_img = PhotoImage(file='img/fext/kotlin.png')
        self.lisp_img = PhotoImage(file='img/fext/lisp.png')
        self.makefile_img = PhotoImage(file='img/fext/makefile.png')
        self.matlab_img = PhotoImage(file='img/fext/matlab.png')
        self.mysql_img = PhotoImage(file='img/fext/mysql.png')
        self.perl_img = PhotoImage(file='img/fext/perl.png')
        self.php_img = PhotoImage(file='img/fext/php.png')
        self.prolog_img = PhotoImage(file='img/fext/prolog.png')
        self.python_img = PhotoImage(file='img/fext/python.png')
        self.ruby_img = PhotoImage(file='img/fext/ruby.png')
        self.sass_img = PhotoImage(file='img/fext/sass.png')
        self.scala_img = PhotoImage(file='img/fext/scala.png')
        self.swift_img = PhotoImage(file='img/fext/swift.png')
        self.tcl_img = PhotoImage(file='img/fext/tcl.png')
        self.ts_img = PhotoImage(file='img/fext/ts.png')
        self.txt_img = PhotoImage(file='img/fext/txt.png')
        self.verilog_img = PhotoImage(file='img/fext/verilog.png')
        self.vhdl_img = PhotoImage(file='img/fext/vhdl.png')
        self.xml_img = PhotoImage(file='img/fext/xml.png')
        self.yaml_img = PhotoImage(file='img/fext/yaml.png')

        for file_name in self.args:
            self.openFileByName(file_name)

        self.mainloop()

    def configureUI(self):

        self.configureWindow()
        self.configureMenu()
        self.configureNotebook()
        self.contextualMenu()
        self.bindWindowEvents()
        self.configureStatusBar()

    def configureWindow(self):

        self.geometry(self.width+'x'+self.height+'+0+0')
        self.title("Quode-IDE")
        self.wm_iconphoto(False, self._icon)
        self.MainWindow.pack()

    def configureMenu(self):

        self.menu_bar = Menu(self, background='#21252b', foreground='#ffffff')
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New Tab',
                                font=self.title_font,
                                command=self.createNewEditor,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator='Ctrl + N')
        self.file_menu.add_command(label="Open",
                                font=self.title_font,
                                command=self.openFile,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator='Ctrl + O')
        self.file_menu.add_command(label="Save",
                                font=self.title_font,
                                command=self.saveFile,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator='Ctrl + S')
        self.file_menu.add_command(label='Remove Tab',
                                font=self.title_font,
                                command=self.removeCurrentEditor,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator='Ctrl + R')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",
                                font=self.title_font,
                                command=self.askQuit,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator='Ctrl + Q')
        self.menu_bar.add_cascade(label="File",
                                font=self.title_font,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                menu=self.file_menu)

        self.edit_menu = Menu(self.menu_bar,
                                tearoff=0,
                                activebackground='#123456')
        self.edit_menu.add_command(label="Cut",
                                font=self.title_font,
                                command=self.cutSelection,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + X")
        self.edit_menu.add_command(label="Copy",
                                font=self.title_font,
                                command=self.copySelection,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + C")
        self.edit_menu.add_command(label="Paste",
                                font=self.title_font,
                                command=self.pasteSelection,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + V")
        self.edit_menu.add_command(label="Replace (All)",
                                font=self.title_font,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                command=self.replaceAllWindow)
        self.menu_bar.add_cascade(label="Edit",
                                font=self.title_font,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                menu=self.edit_menu)

        self.view_menu = Menu(self.menu_bar, tearoff=0)
        self.view_menu.add_command(label="Increase Font Size",
                                font=self.title_font,
                                command=self.increaseFontSize,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + +/=")
        self.view_menu.add_command(label="Decrease Font Size",
                                font=self.title_font,
                                command=self.decreaseFontSize,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + -/_")
        self.view_menu.add_command(label="Find",
                                font=self.title_font,
                                command=self.searchWindow,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + f")
        self.view_menu.add_command(label="File tree",
                                font=self.title_font,
                                command=self.showFileTree,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                accelerator="Ctrl + t")
        self.menu_bar.add_cascade(label="View",
                                font=self.title_font,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                menu=self.view_menu)

        self.run_menu = Menu(self.menu_bar, tearoff=0)
        self.run_menu.add_command(label='Run',
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                command=self.runCurrentEditor,
                                font=self.title_font)
        self.menu_bar.add_cascade(label='Run',
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                font=self.title_font,
                                menu=self.run_menu)

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About",
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                font=self.title_font,
                                command=self.printAbout)
        self.menu_bar.add_cascade(label="Help",
                                font=self.title_font,
                                activebackground='#123456',
                                activeforeground='#ffffff',
                                menu=self.help_menu)
        self.config(menu=self.menu_bar)

    def configureNotebook(self):

        self.notebook.place_configure(relx=0, rely=0, relheight=0.97, relwidth=1)
        self.notebook.enable_traversal()

    def configureStatusBar(self):

        self.status_bar_label = Label(self)
        self.status_bar_label.place_configure(relx=0,
                                            rely=0.97,
                                            relheight=0.03,
                                            relwidth=1)
        self.status_bar_label.config(text=self.getStatusText())


    def langImg(self, ext):

        img = None
        if (ext == '.c'): img = self.c_img
        elif(ext == '.h'): img = self.c_img
        elif(ext == '.cpp'): img = self.cpp_img
        elif(ext == '.hpp'): img = self.cpp_img
        elif(ext == '.css'): img = self.css_img
        elif(ext == '.sass'): img = self.sass_img
        elif(ext == '.yaml'): img = self.yaml_img
        elif(ext == '.yml'): img = self.yaml_img
        elif(ext == '.json'): img = self.json_img
        elif(ext == '.cs'): img = self.cs_img
        elif(ext == '.fs'): img = self.fs_img
        elif(ext == '.e'): img = self.eiffel_img
        elif(ext == '.erl'): img = self.erlang_img
        elif(ext == '.hrl'): img = self.erlang_img
        elif(ext == '.es'): img = self.erlang_img
        elif(ext == '.f03'): img = self.fortran_img
        elif(ext == '.f90'): img = self.fortran_img
        elif(ext == '.F03'): img = self.fortran_img
        elif(ext == '.F90'): img = self.fortran_img
        elif(ext == '.go'): img = self.go_img
        elif(ext == '.hs'): img = self.haskell_img
        elif(ext == '.v'): img = self.verilog_img
        elif(ext == '.vhdl'): img = self.vhdl_img
        elif(ext == '.vhd'): img = self.vhdl_img
        elif(ext == '.html'): img = self.html_img
        elif(ext == '.htm'): img = self.html_img
        elif(ext == '.xhtml'): img = self.html_img
        elif(ext == '.xml'): img = self.xml_img
        elif(ext == '.js'): img = self.js_img
        elif(ext == '.tex'): img = self.ts_img
        elif(ext == '.coffee'): img = self.coffee_img
        elif(ext == '.java'): img = self.java_img
        elif(ext == '.scala'): img = self.scala_img
        elif(ext == '.kt'): img = self.kotlin_img
        elif(ext == '.ktm'): img = self.kotlin_img
        elif(ext == '.kts'): img = self.kotlin_img
        elif(ext == '.lisp'): img = self.lisp_img
        elif(ext == 'make'): img = self.makefile_img
        elif(ext == 'Make'): img = self.makefile_img
        elif(ext == 'cmake'): img = self.cmake_img
        elif(ext == 'CMake'): img = self.cmake_img
        elif(ext == '.m'): img = self.matlab_img
        elif(ext == '.mat'): img = self.matlab_img
        elif(ext == '.dpr'): img = self.delphi_img
        elif(ext == '.perl'): img = self.perl_img
        elif(ext == '.php'): img = self.php_img
        elif(ext == '.pr'): img = self.prolog_img
        elif(ext == '.py'): img = self.python_img
        elif(ext == '.rb'): img = self.ruby_img
        elif(ext == '.sh'): img = self.bash_img
        elif(ext == '.sql'): img = self.mysql_img
        elif(ext == '.mysql'): img = self.mysql_img
        elif(ext == '.tcl'): img = self.tcl_img
        elif(ext == '.awk'): img = self.awk_img
        else: img = self.txt_img

        return img

    def _get_current_editor(self):
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
            scrolled_text = ScrolledText(font=self.code_font,
                                        undo=True, tabs=('2c'),
                                        background='#282c34',
                                        insertbackground='#ffffff',
                                        foreground='#abb2a4')

            self.Editors.append(scrolled_text)
            self.Filenames[scrolled_text] = None
            try :
                lexer = self.lexer_selector[ext]
            except KeyError:
                lexer = None
            self.Lexers[scrolled_text] = lexer
            self.notebook.add(scrolled_text,
                            image=self.langImg(ext),
                            text=os.path.split(new_tab_name)[1],
                            compound='left')
            self.notebook.select(scrolled_text)
            self.createTags()
            self.recolorize(None)
            self.setStatusText(self.getStatusText())

            self.miscBindings(scrolled_text)
            scrolled_text.focus_set()
            scrolled_text.edit_reset()

    def openFile(self):

        opened_file_name = fd.askopenfilename(initialdir=".",
                                              title="Select file",
                                              filetypes=(('all files', '*.*'),))
        if not isinstance(opened_file_name, tuple):
            ext = os.path.splitext(opened_file_name)[1]
            scrolled_text = ScrolledText(font=self.code_font,
                                        undo=True, tabs=('2c'),
                                        background='#282c34',
                                        insertbackground='#ffffff',
                                        foreground='#abb2a4')
            self.Editors.append(scrolled_text)
            self.Filenames[scrolled_text] = opened_file_name
            self.notebook.add(scrolled_text,
                                image=self.langImg(ext),
                                text=os.path.split(opened_file_name)[1],
                                compound='left')
            with open(opened_file_name) as f:
                file_text = f.read()
                f.close()
                scrolled_text.insert('end', file_text)

            self.notebook.select(scrolled_text)
            try :
                lexer = self.lexer_selector[ext]
            except KeyError:
                lexer = None
            self.Lexers[scrolled_text] = lexer
            self.createTags()
            self.recolorize(None)
            scrolled_text.focus_set()
            scrolled_text.edit_reset()
            self.miscBindings(scrolled_text)
            self.setStatusText(self.getStatusText())

    def openFileByName(self, path):

        opened_file_name = path
        if opened_file_name[0] != '/':
            opened_file_name  = os.path.dirname(os.path.abspath(__file__)) + '/' + path
        if not os.path.isdir(opened_file_name):
            ext = os.path.splitext(opened_file_name)[1]
            scrolled_text = ScrolledText(font=self.code_font,
                                        undo=True, tabs=('1.28c'),
                                        background='#282c34',
                                        insertbackground='#ffffff',
                                        foreground='#abb2a4')
            self.Editors.append(scrolled_text)
            self.Filenames[scrolled_text] = opened_file_name
            print(opened_file_name)
            self.notebook.add(scrolled_text,
                                image=self.langImg(ext),
                                text=os.path.split(opened_file_name)[1],
                                compound='left')
            with open(opened_file_name) as f:
                file_text = f.read()
                f.close()
                scrolled_text.insert('end', file_text)

            self.notebook.select(scrolled_text)
            try:
                lexer = self.lexer_selector[ext]
            except KeyError:
                lexer = None
            self.Lexers[scrolled_text] = lexer
            self.createTags()
            self.recolorize(None)
            scrolled_text.focus_set()
            scrolled_text.edit_reset()
            self.miscBindings(scrolled_text)
            self.setStatusText(self.getStatusText())

    def saveFile(self):
        try:
            editor_index = self.notebook.index('current')
            curr_editor = self.Editors[editor_index]
            curr_text = curr_editor.get("1.0", "end")
            if self.Filenames[curr_editor] is not None:
                with open(self.Filenames[curr_editor], 'r+') as f:
                    f.write(curr_text)
                    messagebox.showinfo('Save', 'File Saved!!!')
                    curr_editor.edit_reset()

            else:
                new_file_path = fd.asksaveasfilename(initialdir='.',
                                                filetypes=[("All files", "*")])
                if not isinstance(new_file_path, tuple):

                    self.Filenames[curr_editor] = new_file_path
                    new_file = open(new_file_path, 'w+')
                    new_file.close()

                    new_file = open(new_file_path, 'r+')
                    new_file.write(curr_text)
                    messagebox.showinfo('Save', 'File Saved!!!')
                    self.Filenames[curr_editor] = new_file_path
                    curr_editor.edit_reset()

        except _tkinter.TclError:
            messagebox.showerror("Save File", "No file to save")

    def removeCurrentEditor(self):

        try:
            curr_editor = self._get_current_editor()
            if messagebox.askyesno('Remove Current Tab',
                                'Are you sure you want to remove this Editor?',
                                icon='warning'):
                index = self.notebook.select('current')
                self.notebook.forget(index)
                self.Editors.remove(curr_editor)
                self.Filenames.pop(curr_editor, None)
                self.Lexers.pop(curr_editor, None)

        except _tkinter.TclError:
            messagebox.showerror('Remove Tab', 'Oops!! No tabs to remove!!')


    def askQuit(self):

        if messagebox.askyesno('Remove Current Tab',
                            'Do you really wanna Exit?',
                            icon='warning'):
            self.destroy()

    def bindWindowEvents(self):

        self.bind('<Control-n>', func=lambda e:self.createNewEditor())
        self.bind('<Control-o>', func=lambda e:self.openFile())
        self.bind('<Control-s>', func=lambda e:self.saveFile())
        self.bind('<Control-r>', func=lambda e:self.removeCurrentEditor())
        self.bind('<Control-q>', func=lambda e:self.askQuit())
        self.bind('<Control-x>', func=lambda e:self.cutSelection())
        self.bind('<Control-c>', func=lambda e:self.copySelection())
        self.bind('<Control-v>', func=lambda e:self.pasteSelection())
        self.bind('<Control-a>', func=lambda e:self.selectAll())
        self.bind('<Control-f>', func=lambda e:self.searchWindow())
        self.bind('<Control-z>', func=lambda e:self.undoChange())
        self.bind('<Control-y>', func=lambda e:self.redoChange())
        self.bind('<Control-t>', func=lambda e:self.showFileTree())

        self.bind('<Control-N>', func=lambda e:self.createNewEditor())
        self.bind('<Control-O>', func=lambda e:self.openFile())
        self.bind('<Control-S>', func=lambda e:self.saveFile())
        self.bind('<Control-R>', func=lambda e:self.removeCurrentEditor())
        self.bind('<Control-Q>', func=lambda e:self.askQuit())
        self.bind('<Control-X>', func=lambda e:self.cutSelection())
        self.bind('<Control-C>', func=lambda e:self.copySelection())
        self.bind('<Control-V>', func=lambda e:self.pasteSelection())
        self.bind('<Control-A>', func=lambda e:self.selectAll())
        self.bind('<Control-F>', func=lambda e:self.searchWindow())
        self.bind('<Control-Z>', func=lambda e:self.undoChange())
        self.bind('<Control-Y>', func=lambda e:self.redoChange())
        self.bind('<Control-T>', func=lambda e:self.showFileTree())

        self.bind('<Control-plus>', func=lambda e:self.increaseFontSize())
        self.bind('<Control-minus>', func=lambda e:self.decreaseFontSize())
        self.bind('<Control-KP_Add>', func=lambda e:self.increaseFontSize())
        self.bind('<Control-KP_Subtract>', func=lambda e:self.decreaseFontSize())

        self.bind("<Key>", func=lambda e:self.anyKeyBindings(e))
        # self.bind("<Key>", func=lambda e:self.setStatusText(self.getStatusText()))

        self.bind('<Button>', func=lambda e: self.anyButtonBindings(e))
        self.bind('<Button-3>',
                func=lambda e: self.contextual_menu.post(e.x_root, e.y_root))

    def anyKeyBindings(self, event):

        self.recolorize(None)
        self.setStatusText(self.getStatusText())

    def anyButtonBindings(self, event):

        self.contextual_menu.unpost()
        self.setStatusText(self.getStatusText())

    def cutSelection(self):

        curr_editor = self._get_current_editor()
        curr_editor.event_generate('<<Cut>>')

    def copySelection(self):

        curr_editor = self._get_current_editor()
        curr_editor.event_generate('<<Copy>>')

    def pasteSelection(self):

        curr_editor = self._get_current_editor()
        curr_editor.event_generate('<<Paste>>')

    def contextualMenu(self):

        self.contextual_menu = Menu(self, tearoff=False)

        self.contextual_menu.add_command(label='New Editor',
                                        command=self.createNewEditor)
        self.contextual_menu.add_command(label='Open File',
                                        command=self.openFile)
        self.contextual_menu.add_command(label='Save Editor',
                                        command=self.saveFile)
        self.contextual_menu.add_separator()
        self.contextual_menu.add_command(label='Remove Editor',
                                        command=self.removeCurrentEditor)
        self.contextual_menu.add_command(label='Change title',
                                        command=self.changeEditorTitle)

    def unpostContextMenu(self):

        self.contextual_menu.unpost()

    def changeEditorTitle(self):

        curr_editor = self._get_current_editor()
        new_title = askstring('New Editor', "Enter new title")
        new_ext = os.path.splitext(new_title)[1]
        self.notebook.tab(curr_editor,
                        text=new_title,
                        image=self.langImg(new_ext))
        try :
            new_lexer = self.lexer_selector[new_ext]
        except KeyError:
            new_lexer = None
        self.Lexers[curr_editor] = new_lexer
        self.recolorize(None)

    def increaseFontSize(self):

        curr_editor = self._get_current_editor() # FIXME
        curr_font = Font(curr_editor, curr_editor.cget("font"))
        curr_size = curr_font.cget('size')
        new_size = curr_size+1
        curr_font.configure(size=new_size)
        new_font = curr_font
        curr_editor.configure(font=new_font)

        # print(Font(curr_editor, curr_editor.cget("font")).cget("size"))

    def decreaseFontSize(self):

        curr_editor = self._get_current_editor() # FIXME
        curr_font = Font(curr_editor, curr_editor.cget("font"))
        curr_size = curr_font.cget('size')
        if curr_size > 1:
            new_size = curr_size-1
            curr_font.configure(size=new_size)

    def undoChange(self):
        try:

            curr_editor = self._get_current_editor()
            curr_editor.edit_undo()
            self.createTags()
            self.recolorize(None)
        except _tkinter.TclError:
            pass

    def redoChange(self):
        try:
            curr_editor = self._get_current_editor()
            curr_editor.edit_redo()
        except _tkinter.TclError:
            pass

    def selectAll(self):
        curr_editor = self._get_current_editor()
        curr_editor.tag_add('sel', '1.0', 'end')
        return "break"

    def searchWindow(self):

        self.search_window = SearchWindow(self, 0)

    def removeAllTags(self):

        curr_editor = self._get_current_editor()
        for tag in curr_editor.tag_names():
            curr_editor.tag_delete(tag)

    def replaceAllWindow(self):

        self.replace_window = ReplaceTextWindow(self)

    def replaceAll(self, a, b):

        curr_editor = self._get_current_editor()
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
                start = end
                pos = curr_editor.search(a, start, stopindex="end")
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
        curr_editor = self._get_current_editor()
        bold_font = Font(curr_editor, curr_editor.cget("font"))
        bold_font.configure(weight='bold')

        italic_font = Font(curr_editor, curr_editor.cget("font"))
        italic_font.configure(slant='italic')

        bold_italic_font = Font(curr_editor, curr_editor.cget("font"))
        bold_italic_font.configure(weight='bold', slant='italic')

        style = get_style_by_name('default')
        for ttype, ndef in style:
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

            curr_editor.tag_configure(str(ttype),
                                    foreground=foreground,
                                    font=tag_font)

    def recolorize(self, event):

        if len(self.Editors) != 0:
            curr_editor = self._get_current_editor()
            code = curr_editor.get("1.0", "end-1c")
            lexer = self.Lexers[curr_editor]
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

                    for tagname in curr_editor.tag_names(index1):
                        curr_editor.tag_remove(tagname, index1, index2)

                    curr_editor.tag_add(str(ttype), index1, index2)

                start_line = end_line
                start_index = end_index

            # self.underlineComplement()

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
        lex['.xml'] = XmlLexer()
        lex['.js'] = JavascriptLexer()
        lex['.tex'] = TypeScriptLexer()
        lex['.coffee'] = CoffeeScriptLexer()
        lex['.java'] = JavaLexer()
        lex['.scala'] = ScalaLexer()
        lex['.kt'] = KotlinLexer()
        lex['.ktm'] = KotlinLexer()
        lex['.kts'] = KotlinLexer()
        lex['.lisp'] = CommonLispLexer()
        lex['make'] = MakefileLexer()
        lex['Make'] = MakefileLexer()
        lex['CMake'] = CMakeLexer()
        lex['cmake'] = CMakeLexer()
        lex['.m'] = MatlabLexer()
        lex['.mat'] = MatlabLexer()
        lex['.dpr'] = DelphiLexer()
        lex['.perl'] = PerlLexer()
        lex['.php'] = PhpLexer()
        lex['.pr'] = PrologLexer()
        lex['.py'] = Python3Lexer()
        lex['.rb'] = RubyLexer()
        lex['.sh'] = BashLexer()
        lex['.sql'] = MySqlLexer()
        lex['.mysql'] = MySqlLexer()
        lex['.tcl'] = TclLexer()
        lex['.awk'] = AwkLexer()

        return lex

    def getStatusText(self):

        if len(self.Editors):
            curr_editor = self._get_current_editor()
            cursor_position = curr_editor.index('insert')
            if cursor_position is not None:
                row, col = cursor_position.split('.')
                return "Row: %s Col: %s"%(row, col)
            else:
                return "Quode-IDE"
        else:
            return "Quode-IDE"

    def setStatusText(self, text):

        if len(self.Editors):
            self.status_bar_label.config(text=text)
        else:
            self.status_bar_label.config(text="Quode-IDE")

    def miscBindings(self, scrolled_text):

        scrolled_text.bind('<Control-z>', func=self.undoChange)
        scrolled_text.bind('<Control-y>', func=self.redoChange)
        scrolled_text.bind('<KeyRelease-quoteright>',
                           func=lambda e: self.completeQuoteright(scrolled_text))
        scrolled_text.bind('<KeyRelease-quotedbl>',
                           func=lambda e: self.completeQuotedbl(scrolled_text))
        scrolled_text.bind('<KeyRelease-parenleft>',
                           func=lambda e: self.completeParen(scrolled_text))
        scrolled_text.bind('<KeyRelease-bracketleft>',
                           func=lambda e: self.completeBracket(scrolled_text))
        scrolled_text.bind('<KeyRelease-braceleft>',
                           func=lambda e: self.completeBrace(scrolled_text))
        scrolled_text.bind('<KeyRelease-less>',
                           func=lambda e: self.completeAngles(scrolled_text))
        scrolled_text.bind('<KeyRelease-Return>',
                           func=lambda e: self.returnNewLine(scrolled_text))

        scrolled_text.bind('<parenright>',
                           func=lambda e: self.skipRParen(scrolled_text))
        scrolled_text.bind('<bracketright>',
                           func=lambda e: self.skipRBracket(scrolled_text))
        scrolled_text.bind('<braceright>',
                           func=lambda e: self.skipRBrace(scrolled_text))
        scrolled_text.bind('<greater>',
                           func=lambda e: self.skipRAngle(scrolled_text))
        scrolled_text.bind('<BackSpace>',
                           func=lambda e: self.erasePair(scrolled_text))

    def completeParen(self, scrolled_text):
        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', ')')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def completeBracket(self, scrolled_text):

        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', ']')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def completeBrace(self, scrolled_text):

        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', '}')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def completeQuoteright(self, scrolled_text):

        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', '\'')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def completeQuotedbl(self, scrolled_text):

        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', '"')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def completeAngles(self, scrolled_text):

        scrolled_text.mark_gravity('insert', 'left')
        scrolled_text.insert('insert', '>')
        scrolled_text.mark_gravity('insert', 'right')
        self.recolorize(None)

    def returnNewLine(self, scrolled_text):

        curr_editor = self._get_current_editor()
        cursor_position = curr_editor.index('insert')

        row_index = int(cursor_position.split('.')[0])
        prev_row_index = str(row_index - 1) + '.0'
        prev_line = curr_editor.get(prev_row_index, prev_row_index + ' lineend')
        this_line = curr_editor.get(cursor_position + ' linestart', cursor_position + ' lineend')
        if(len(prev_line) > 1):
            left_char = prev_line[-1]

            new_line = ''.join(self.notAlphaLine(prev_line))

            if len(this_line) > 0:
                right_char = this_line[0]
                if self._are_braces_paired(left_char, right_char):
                    curr_editor.insert('insert', new_line + '\t')
                    curr_editor.mark_gravity('insert', 'left')
                    curr_editor.insert('insert', '\n\t')
                    curr_editor.mark_gravity('insert', 'right')
            else:
                curr_editor.insert('insert', new_line)
        elif(len(prev_line) == 1):
            if(len(this_line) == 0):
                if (prev_line == '\t'):
                    curr_editor.insert('insert', '\t')
            if(len(this_line) > 0):
                left_char = prev_line[0]
                right_char = this_line[0]
                if self._are_braces_paired(left_char, right_char):
                    curr_editor.insert('insert', '\t')
                    curr_editor.mark_gravity('insert', 'left')
                    curr_editor.insert('insert', '\n')
                    curr_editor.mark_gravity('insert', 'right')

    def _are_braces_paired(self, lchar, rchar):

        if(lchar == '(' and rchar == ')'):
            return True
        if(lchar == '[' and rchar == ']'):
            return True
        if(lchar == '{' and rchar == '}'):
            return True
        return False

    def notAlphaLine(self, line):

        new_line = []
        line = ''.join(line)
        for char in line:
            if (char == ' ' or char == '\t'):
                new_line.append(char)
            else:
                return new_line
        return new_line

    def skipRParen(self, scrolled_text):
        try:
            cursor_position = scrolled_text.index('insert')
            row, col = map(int, cursor_position.split('.'))
            next_position = str(row) + '.' + str(col+1)
            if scrolled_text.get(cursor_position, next_position) == ')':
                scrolled_text.delete(cursor_position, next_position)
        except:
            pass

    def skipRBracket(self, scrolled_text):
        try:
            cursor_position = scrolled_text.index('insert')
            row, col = map(int, cursor_position.split('.'))
            next_position = str(row) + '.' + str(col+1)
            if scrolled_text.get(cursor_position, next_position) == ']':
                scrolled_text.delete(cursor_position, next_position)
        except:
            pass

    def skipRBrace(self, scrolled_text):
        try:
            cursor_position = scrolled_text.index('insert')
            row, col = map(int, cursor_position.split('.'))
            next_position = str(row) + '.' + str(col+1)
            if scrolled_text.get(cursor_position, next_position) == '}':
                scrolled_text.delete(cursor_position, next_position)
        except:
            pass

    def skipRAngle(self, scrolled_text):
        try:
            cursor_position = scrolled_text.index('insert')
            row, col = map(int, cursor_position.split('.'))
            next_position = str(row) + '.' + str(col+1)
            if scrolled_text.get(cursor_position, next_position) == '>':
                scrolled_text.delete(cursor_position, next_position)
        except:
            pass

    def erasePair(self, scrolled_text):

        try:
            cursor_position = scrolled_text.index('insert')
            row, col = map(int, cursor_position.split('.'))
            prev_position = str(row) + '.' + str(col-1)
            next_position = str(row) + '.' + str(col+1)
            curr_char = scrolled_text.get(cursor_position, next_position)
            prev_char = scrolled_text.get(prev_position, cursor_position)
            if curr_char == ')' and prev_char == '(':
                scrolled_text.delete(cursor_position, next_position)
            if curr_char == ']' and prev_char == '[':
                scrolled_text.delete(cursor_position, next_position)
            if curr_char == '}' and prev_char == '{':
                scrolled_text.delete(cursor_position, next_position)
            if curr_char == '>' and prev_char == '<':
                scrolled_text.delete(cursor_position, next_position)
        except:
            pass

    def runCurrentEditor(self):
        if len(self.Editors):
            curr_editor = self._get_current_editor()
            if self.Filenames[curr_editor] is not None:
                os.system('gnome-terminal --working-directory=%s' % os.path.dirname(self.Filenames[curr_editor]))
            else:
                messagebox.showerror(title="Could Not Open Terminal",
                                    message="Please save the File to run it")

    def showFileTree(self):

        if len(self.Editors):
            curr_editor = self._get_current_editor()
            directory = os.path.dirname(self.Filenames[curr_editor])
            FileTree(curr_editor, directory)

    def printAbout(self):

        about = """


   qqqqq                           dd                    ii  ddddddd     eeeeeee
  qqq qqq                          dd                    ii  dd     dd   ee
 qqq   qqq                         dd                    ii  dd      dd  ee
qqq     qqq                        dd                    ii  dd      dd  ee
qqq     qqq uu    uu    oo      ddddd   eeeee            ii  dd      dd  eeeeeee
qqq     qqq uu    uu  oo  oo   dd  dd  ee   ee           ii  dd      dd  ee
qqq     qqq uu    uu oo    oo dd   dd ee     ee  zzzzz   ii  dd      dd  ee
 qqq   qqq  uu    uu oo    oo dd   dd eeeeeeeee          ii  dd      dd  ee
  qqq qqq   uu    uu  oo  oo  dd   dd  ee                ii  dd    dd    ee
   qqqqq      uuuu      oo      ddddd   eeeeee           ii  dddddd      eeeeeee
       qqqqqq


       Quode-IDE(Integrated Development Environment)

       Author : Yash Khasbage


DISCLAIMER:

    Identifiers used in this software are purely fictious and bear no
    resembalance to any person living or dead. Any resembalace is purely
    co-incidental.

    No animals were harmed in coding of this software.

        """
        print(about)
        messagebox.showinfo(title="About", message="Check terminal")

    def _get_int_row_col(self):

        curr_editor = self._get_current_editor()
        return list(map(int, curr_editor.index('insert').split('.')))

    def _get_str_row_col(self):

        curr_editor = self._get_current_editor()
        return curr_editor.index('insert')

    def _str_to_int(self, pos):

        return list(map(int, pos.split('.')))

    def _get_current_char(self):

        row, col = self._get_int_row_col()
        curr_pos = str(row)+'.'+str(col)
        next_pos = str(row)+'.'+str(col+1)
        curr_editor = self._get_current_editor()
        return curr_editor.get(curr_pos, next_pos)

    def _next_position(self, pos):
        row, col = list(map(int, pos.split('.')))
        return '%d.%d'%(row, col+1)

    def underlineComplement(self):

        if len(self.Editors):

            pos = self._get_str_row_col()
            curr_char = self._get_current_char()
            if(curr_char == '('):
                self.underlineRParen(pos)
            elif(curr_char == ')'):
                self.underlineLParen(pos)
            elif(curr_char == '['):
                self.underlineRBracket(pos)
            elif(curr_char == ']'):
                self.underlineLBracket(pos)
            elif(curr_char == '{'):
                self.underlineRBrace(pos)
            elif(curr_char == '}'):
                self.underlineLBrace(pos)
            elif(curr_char == '<'):
                self.underlineRAngle(pos)
            elif(curr_char == '>'):
                self.underlineLAngle(pos)

    def underlineRParen(self, l_pos):
        return
        curr_editor = self._get_current_editor()
        text = curr_editor.get(l_pos, 'end')
        count = 0
        index = 0
        for i in range(len(text)):
            if(text[i] == ')' and count == 0):
                index = i
            elif(text[i] == '('):
                count += 1
            elif(text[i] == ')'):
                count -= 1
        j = 0
        line = self._str_to_int(l_pos)[0]
        line_number = 0
        start = l_pos
        end = '%d.end' % line
        j_prev = 0
        while(index > j):
            j_prev = j
            j += len(curr_editor.get(start, end)) - 1
            line_number += 1
            start = "%d.0" % (line+line_number)
        r_paren_index = '%d.%d' % (line+line_number, index-j_prev)
        print("index", index)
        print("j", j)
        print("linenumber", line_number)
        print("r_paren_index", r_paren_index)
        curr_editor.tag_add('underline',
                            l_pos,
                            self._next_position(l_pos))
        curr_editor.tag_add('underline',
                            r_paren_index,
                            self._next_position(r_paren_index))
        curr_editor.tag_configure('underline', underline=True)


    def underlineLParen(self, r_pos):

        pass

    def underlineRBracket(self, l_pos):

        pass

    def underlineLBracket(self, r_pos):

        pass

    def underlineRbrace(self, l_pos):

        pass

    def underlineLBrace(self, r_pos):

        pass

    def underlineRAngle(self, l_pos):

        pass

    def underlineLAngle(self, r_pos):

        pass


def main(args):

    App(args)


if __name__ == '__main__':

    main(argv[1:])
