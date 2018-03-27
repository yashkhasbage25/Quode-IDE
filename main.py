from tkinter import Tk, Menu, PhotoImage, messagebox, _tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, Style
import tkinter.filedialog as fd
from tkinter.simpledialog import askinteger, askstring
import os

global BASE_DIR, IMG_DIR, IMG_FILEEXT_DIR
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, 'img')
IMG_FILEEXT_DIR = os.path.join(IMG_DIR, 'file_extensions')

global normal_text_font
normal_text_font = ('arial', 12)

global default_file_path
default_file_path = None


def createNewTab(self):

    new_tab_id = top_tab_id[-1]+1
    top_tab_id.append(new_tab_id)
    new_tab_name = askstring('New Tab', 'Enter name of new tab')
    c_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                          'c.gif')).subsample(
        x=90, y=90)
    cpp_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                            'cpp.png')).subsample(
        x=15, y=15)
    css_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                            'css.png')).subsample(
        x=70, y=70)
    html_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                             'html.png')).subsample(
        x=45, y=45)
    java_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                             'java.gif')).subsample(
        x=15, y=15)
    javascript_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                   'javascript.png')).subsample(x=15, y=15)
    python_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                               'python.png')).subsample(x=35, y=35)
    txt_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                            'txt.png')).subsample(x=13, y=13)
    tab_image = txt_logo
    if(new_tab_name == ''):
        new_tab_name = 'Tab '+str(new_tab_id)
    else:
        file_ext = os.path.splitext(new_tab_name)[1]
        if(file_ext == '.c'):
            tab_image = c_logo
        elif(file_ext == '.cpp'):
            tab_image = cpp_logo
        elif(file_ext == '.css'):
            tab_image = css_logo
        elif(file_ext == '.html'):
            tab_image = html_logo
        elif(file_ext == '.java'):
            tab_image = java_logo
        elif(file_ext == '.js'):
            tab_image = javascript_logo
        elif(file_ext == '.py'):
            tab_image = python_logo

    tab_name = new_tab_name
    file_path = default_file_path
    scrolled_text = ScrolledText(font=normal_text_font)

    file_ext = os.path.splitext(new_tab_name)[1]
    if(file_ext == '.c'):
        commonSyntaxBindings(scrolled_text)
        cSyntaxBindings(scrolled_text)
    elif(file_ext == '.cpp'):
        commonSyntaxBindings(scrolled_text)
        cppSyntaxBindings(scrolled_text)
    elif(file_ext == '.css'):
        commonSyntaxBindings(scrolled_text)
        cssSyntaxBindings(scrolled_text)
    elif(file_ext == '.html'):
        commonSyntaxBindings(scrolled_text)
        htmlSyntaxBindings(scrolled_text)
    elif(file_ext == '.java'):
        commonSyntaxBindings(scrolled_text)
        javaSyntaxBindings(scrolled_text)
    elif(file_ext == '.js'):
        commonSyntaxBindings(scrolled_text)
        jsSyntaxBindings(scrolled_text)
    elif(file_ext == '.py'):
        commonSyntaxBindings(scrolled_text)
        pySyntaxBindings(scrolled_text)

    scrolled_text.focus_set()
    Tabs.append([tab_name, scrolled_text, tab_image, normal_text_font, file_path])
    notebook.add(Tabs[-1][1], text=Tabs[-1][0],
                 image=Tabs[-1][2], compound='left')


def openFile(self):

    opened_file_name = fd.askopenfilename(initialdir="/home/dell/",
                                          title="Select file",
                                          filetypes=(('all files', '*.*'),))
    if not isinstance(opened_file_name, tuple):
        new_tab_id = top_tab_id[-1]+1
        top_tab_id.append(new_tab_id)
        new_tab_name = os.path.split(opened_file_name)[1]
        file_ext = os.path.splitext(new_tab_name)[1]
        c_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                              'c.gif')).subsample(
            x=90, y=90)
        cpp_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                'cpp.png')).subsample(
            x=15, y=15)
        css_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                'css.png')).subsample(
            x=70, y=70)
        html_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                 'html.png')).subsample(
            x=45, y=45)
        java_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                 'java.gif')).subsample(
            x=15, y=15)
        javascript_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                       'javascript.png')).subsample(x=15, y=15)
        python_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                   'python.png')).subsample(x=35, y=35)
        txt_logo = PhotoImage(file=os.path.join(IMG_FILEEXT_DIR,
                                                'txt.png')).subsample(x=13, y=13)

        tab_image = txt_logo

        if(file_ext == '.c'):
            tab_image = c_logo
        elif(file_ext == '.cpp'):
            tab_image = cpp_logo
        elif(file_ext == '.java'):
            tab_image = java_logo
        elif(file_ext == '.js'):
            tab_image = javascript_logo
        elif(file_ext == '.html'):
            tab_image = html_logo
        elif(file_ext == '.css'):
            tab_image = css_logo
        elif(file_ext == '.py'):
            tab_image = python_logo

        tab_name = opened_file_name
        file_path = opened_file_name
        scrolled_text = ScrolledText(font=normal_text_font)

        file_ext = os.path.splitext(new_tab_name)[1]
        if(file_ext == '.c'):
            commonSyntaxBindings(scrolled_text)
            cSyntaxBindings(scrolled_text)
        elif(file_ext == '.cpp'):
            commonSyntaxBindings(scrolled_text)
            cppSyntaxBindings(scrolled_text)
        elif(file_ext == '.css'):
            commonSyntaxBindings(scrolled_text)
            cssSyntaxBindings(scrolled_text)
        elif(file_ext == '.html'):
            commonSyntaxBindings(scrolled_text)
            htmlSyntaxBindings(scrolled_text)
        elif(file_ext == '.java'):
            commonSyntaxBindings(scrolled_text)
            javaSyntaxBindings(scrolled_text)
        elif(file_ext == '.js'):
            commonSyntaxBindings(scrolled_text)
            jsSyntaxBindings(scrolled_text)
        elif(file_ext == '.py'):
            commonSyntaxBindings(scrolled_text)
            pySyntaxBindings(scrolled_text)

        Tabs.append([tab_name, scrolled_text, tab_image, normal_text_font, file_path])
        notebook.add(Tabs[-1][1], text=Tabs[-1][0],
                     image=Tabs[-1][2], compound='left')
        Tabs[-1][1].insert('insert', open(opened_file_name, 'r+').read())
        scrolled_text.focus_set()
        scrolled_text.mark_set('insert', '0.0')


def saveFile(self):

    current_tab = notebook.index('current')
    txt = Tabs[current_tabs][1].get('1.0', 'end')
    if Tabs[current_tab-1][4] is not None:
        with open(Tabs[current_tab-1][4], 'r+') as f:
            f.write(txt)
    else:
        new_file_path = fd.asksaveasfilename(parent=root, filetypes=[("All files", "*")])
        if not isinstance(new_file_path, tuple):
            new_file = open(new_file_path, 'w+')
            new_file.close()

            new_file = open(new_file_path, 'r+')
            new_file.write(txt)
            messagebox.showinfo('Save', 'File Saved!!!')


def removeCurrentTab(root):

    try:
        index = notebook.index('current')
        if messagebox.askquestion('Remove Current Tab', 'Are you sure you want to remove this tab?', icon='warning') == 'yes':
            notebook.forget(index)
            Tabs.remove(Tabs[index])
    except _tkinter.TclError:
        messagebox.showerror('Remove Tab', 'Oops!! No tabs to remove!!')


def removeCurrentTabUsingPopup(self, popup_menu):

    removeCurrentTab(root)
    popup_menu.unpost()
    popup_menu = None


def popUpMenu(event, popup_menu):

    if notebook.index('end') == 0:
        popup_menu.entryconfig('Increase font size', state='disabled')
        popup_menu.entryconfig('Decrease font size', state='disabled')
        popup_menu.entryconfig('Set font size manually', state='disabled')
    else:
        popup_menu.entryconfig('Increase font size', state='normal')
        popup_menu.entryconfig('Decrease font size', state='normal')
        popup_menu.entryconfig('Set font size manually', state='normal')
    popup_menu.post(event.x_root, event.y_root)


def removePopUpMenu(event, popup_menu):

    popup_menu.unpost()
    popup_menu = Menu(notebook, tearoff=0)
    popup_menu.add_command(label='New Tab', command=lambda: createNewTab(root))
    popup_menu.add_separator()
    popup_menu.add_command(
        label='Remove', command=lambda: removeCurrentTabUsingPopup(root, popup_menu))


def increaseFontSize(root, popup_menu):

    index = notebook.index('current')
    list(Tabs[index][3])[1] += 1
    tuple(Tabs[index][3])
    Tabs[index][1].config(font=Tabs[index][3])
    popup_menu.unpost()


def decreaseFontSize(root, popup_menu):

    index = notebook.index('current')
    list(Tabs[index][3])[1] -= 1
    tuple(Tabs[index][3])
    Tabs[index][1].config(font=Tabs[index][3])
    popup_menu.unpost()


def setFontSizeManually(root, popup_menu):

    popup_menu.unpost()
    index = notebook.index('current')
    p = list(Tabs[index][3])
    ans = askinteger('Font size', 'Set font size manually')
    p[1] = ans
    Tabs[index][3] = tuple(p)
    Tabs[index][1].config(font=Tabs[index][3])


def commonSyntaxBindings(scrolled_text):

    scrolled_text.bind('<KeyRelease-quoteright>',
                       func=lambda x: scrolledtextInsertQuoteright(scrolled_text))
    scrolled_text.bind('<KeyRelease-quotedbl>',
                       func=lambda x: scrolledtextInsertQuotedbl(scrolled_text))
    scrolled_text.bind('<KeyRelease-parenleft>',
                       func=lambda x: scrolledtextInsertParen(scrolled_text))
    scrolled_text.bind('<KeyRelease-bracketleft>',
                       func=lambda x: scrolledtextInsertBracket(scrolled_text))
    scrolled_text.bind('<KeyRelease-braceleft>',
                       func=lambda x: scrolledtextInsertBrace(scrolled_text))
    scrolled_text.bind('<KeyRelease-Return>',
                       func=lambda x: returnNewLine(scrolled_text))


def cSyntaxBindings(scrolled_text):

    default_c_text = """#include<stdio.h>

int main(void)
{
\t

\treturn 0;
}"""
    scrolled_text.insert('insert', default_c_text)
    scrolled_text.mark_set('insert', '5.1')


def cppSyntaxBindings(scrolled_text):

    default_cpp_text = """#include<bits/stdc++.h>
using namespace std;

int main( void )
{
\t
\treturn 0;
}"""
    scrolled_text.insert('insert', default_cpp_text)
    scrolled_text.mark_set('insert', '6.1')


def cssSyntaxBindings(scrolled_text):

    default_css_text = """"""
    scrolled_text.insert('insert', default_css_text)


def htmlSyntaxBindings(scrolled_text):

    default_html_text = """<!DOCTYPE html>
<title>
\t
<\\title>
<head>
\t
<\\head>
<body>
\t
<//body>
<//html>
    """
    scrolled_text.insert('insert', default_html_text)
    scrolled_text.mark_set('insert', '3.1')


def javaSyntaxBindings(scrolled_text):

    default_java_text = """public class <Class Name>
{
	public static void main(String[] args) {
\t\t
	}
}
    """
    scrolled_text.insert('insert', default_java_text)
    scrolled_text.mark_set('insert', '4.2')


def jsSyntaxBindings(scrolled_text):

    default_js_text = ''
    scrolled_text.insert('insert', default_js_text)


def pySyntaxBindings(scrolled_text):

    default_py_text = """for t in range(int(input())):
\t
    """
    scrolled_text.insert('insert', default_py_text)
    scrolled_text.mark_set('insert', '2.1')


def scrolledtextInsertParen(scrolled_text):

    scrolled_text.mark_gravity('insert', 'left')
    scrolled_text.insert('insert', ')')
    scrolled_text.mark_gravity('insert', 'right')


def scrolledtextInsertBracket(scrolled_text):

    scrolled_text.mark_gravity('insert', 'left')
    scrolled_text.insert('insert', ']')
    scrolled_text.mark_gravity('insert', 'right')


def scrolledtextInsertBrace(scrolled_text):

    scrolled_text.mark_gravity('insert', 'left')
    scrolled_text.insert('insert', '}')
    scrolled_text.mark_gravity('insert', 'right')


def scrolledtextInsertQuoteright(scrolled_text):

    scrolled_text.mark_gravity('insert', 'left')
    scrolled_text.insert('insert', '\'')
    scrolled_text.mark_gravity('insert', 'right')


def scrolledtextInsertQuotedbl(scrolled_text):

    scrolled_text.mark_gravity('insert', 'left')
    scrolled_text.insert('insert', '"')
    scrolled_text.mark_gravity('insert', 'right')


def returnNewLine(scrolled_text):

    cursor_position = scrolled_text.index('insert')

    row_index = int(cursor_position.split('.')[0])
    col_index = int(cursor_position.split('.')[1])
    prev_row_index = str(row_index - 1) + '.0'
    prev_line = scrolled_text.get(prev_row_index, prev_row_index + ' lineend')
    this_line = scrolled_text.get(cursor_position + ' linestart', cursor_position + ' lineend')
    if(len(prev_line) > 1 and len(this_line) > 0):
        left_char = prev_line[-1]
        right_char = this_line[0]
        new_line = ''.join(notAlphaLine(prev_line))
        if((left_char == '(' and right_char == ')') or (left_char == '[' and right_char == ']') or (left_char == '{' and right_char == '}')):
            scrolled_text.insert('insert', new_line + '\t')
            scrolled_text.mark_gravity('insert', 'left')
            scrolled_text.insert('insert', '\n\t')
            scrolled_text.mark_gravity('insert', 'right')
    elif(prev_line == '\t' and len(this_line) == 0):
        scrolled_text.insert('insert', '\t')


def notAlphaLine(line):

    new_line = []
    line = ''.join(line)
    for char in line:
        if (char == ' ' or char == '\t'):
            new_line.append(char)
        else:
            return new_line
    return new_line


def hello():
    pass


def askQuit(root):

    if messagebox.askquestion('Quit', 'Do you really want to quit???', icon='warning') == 'yes':
        root.quit()


def Quode():

    global root
    root = Tk()
    root.geometry('1200x720+0+0')
    root.configure(background='#ffffff')
    root.title('Quode')

    global notebook
    notebook = Notebook(root)
    notebook.place_configure(relheight=0.95, relwidth=1, relx=0, rely=0.05)

    notebook.enable_traversal()

    # menu

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New Tab', font='arial 12',
                          command=lambda x: createNewTab(root))
    file_menu.add_command(label="Open", font='arial 12',
                          command=lambda x: openFile(root))
    file_menu.add_command(label="Save", font='arial 12',
                          command=lambda x: saveFile(root))
    file_menu.add_command(label='Remove Tab', font='arial 12',
                          command=lambda x: removeCurrentTab(root))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", font='arial 12',
                          command=lambda x: root.quit())
    menu_bar.add_cascade(label="File", font='arial 12', menu=file_menu)

    edit_menu = Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Cut", font='arial 12', command=lambda: hello)
    edit_menu.add_command(label="Copy", font='arial 12', command=lambda: hello)
    edit_menu.add_command(label="Paste", font='arial 12',
                          command=lambda: hello)
    menu_bar.add_cascade(label="Edit", font='arial 12', menu=edit_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="About", font='arial 12',
                          command=lambda: hello)
    menu_bar.add_cascade(label="Help", font='arial 12', menu=help_menu)
    root.config(menu=menu_bar)

    # root bindings

    root.bind('<Control-n>', func=lambda x: createNewTab(root))
    root.bind('<Control-o>', func=lambda x: openFile(root))
    root.bind('<Control-s>', func=lambda x: saveFile(root))
    root.bind('<Control-q>', func=lambda x: askQuit(root))

    # popup menu

    popup_menu = Menu(notebook, tearoff=0)
    popup_menu.add_command(label='New Tab', command=lambda: createNewTab(root))
    popup_menu.add_separator()
    popup_menu.add_command(
        label='Remove', command=lambda: removeCurrentTabUsingPopup(root, popup_menu))
    popup_menu.add_separator()
    popup_menu.add_command(label='Increase font size',
                           command=lambda: increaseFontSize(root, popup_menu))
    popup_menu.add_command(label='Decrease font size',
                           command=lambda: decreaseFontSize(root, popup_menu))
    popup_menu.add_command(label='Set font size manually',
                           command=lambda: setFontSizeManually(root, popup_menu))
    popup_menu.entryconfig('Increase font size', state='normal')
    popup_menu.entryconfig('Decrease font size', state='normal')
    popup_menu.entryconfig('Set font size manually', state='normal')

    # root bindings to popup

    root.bind('<Button-3>', func=lambda event: popUpMenu(event, popup_menu))
    root.bind('<Button-1>', func=lambda event: removePopUpMenu(root, popup_menu))
    root.bind('<Key>', func=lambda event: removePopUpMenu(root, popup_menu))

    # info of every tab

    global Tabs, top_tab_id
    Tabs = []
    top_tab_id = [0]

    root.mainloop()


if __name__ == '__main__':

    Quode()
