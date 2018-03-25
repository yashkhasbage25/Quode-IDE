from tkinter import Tk, Menu, PhotoImage, messagebox, _tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook, Style
from tkinter.font import Font
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

    tab_name = new_tab_name
    file_path = default_file_path
    scrolled_text = ScrolledText(font=normal_text_font)
    #scrolled_text.bind('<Tab>', lambda x: scrolled_text.insert('current', ' '*4))
    #scrolled_text.bind('<Button-3>', func=lambda event: popUpMenu(event))
    Tabs.append([tab_name, scrolled_text, tab_image, normal_text_font, file_path])
    notebook.add(Tabs[-1][1], text=Tabs[-1][0],
                 image=Tabs[-1][2], compound='left')
    print('Tabs = ', Tabs)


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
        #scrolled_text.bind('<Tab>', lambda x: scrolled_text.insert('current', ' '*4))
        #scrolled_text.bind('<Button-3>', func=lambda event: popUpMenu(event))
        Tabs.append([tab_name, scrolled_text, tab_image, normal_text_font, file_path])
        notebook.add(Tabs[-1][1], text=Tabs[-1][0],
                     image=Tabs[-1][2], compound='left')

        # opened_file = open(self.opened_file_name, 'r')
        Tabs[-1][1].insert('current', open(opened_file_name, 'r+').read())
        scrolled_text.focus_set()
        scrolled_text.mark_set('insert', '0.0')


def saveFile(self):
    print(Tabs)

    current_tab = notebook.index('current')
    txt = Tabs[current_tab-1][1].get('1.0', 'end')
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
    p = list(Tabs[index][3])
    p[1] = p[1]+1
    Tabs[index][3] = tuple(p)
    Tabs[index][1].config(font=Tabs[index][3])
    popup_menu.unpost()


def decreaseFontSize(root, popup_menu):
    index = notebook.index('current')
    p = list(Tabs[index][3])
    p[1] = p[1]-1
    Tabs[index][3] = tuple(p)
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


def hello():
    pass


def Quode():

    global root
    root = Tk()
    root.geometry('1200x720+0+0')
    root.configure(background='#ffffff')
    root.title('Quode')

    global notebook
    notebook = Notebook(root)
    notebook.place_configure(relheight=0.95, relwidth=1, relx=0, rely=0.05)
    """
    s = ScrolledText(notebook, height=720, width=1200)
    s.insert('current', 'kfksegksjbkzsjh')
    s.focus_set()
    notebook.add(s, text='temp')"""
    notebook.enable_traversal()

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New Tab', font='arial 12',
                          command=lambda: createNewTab(root))
    file_menu.add_command(label="Open", font='arial 12',
                          command=lambda: openFile(root))
    file_menu.add_command(label="Save", font='arial 12',
                          command=lambda: saveFile(root))
    file_menu.add_command(label='Remove Tab', font='arial 12',
                          command=lambda: removeCurrentTab(root))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", font='arial 12',
                          command=lambda: root.quit())
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

    root.bind('<Control-n>', func=lambda x: createNewTab(root))
    root.bind('<Control-o>', func=lambda x: openFile(root))
    root.bind('<Control-s>', func=lambda x: saveFile(root))
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
    root.bind('<Button-3>', func=lambda event: popUpMenu(event, popup_menu))
    root.bind('<Button-1>', func=lambda event: removePopUpMenu(root, popup_menu))
    root.bind('<Key>', func=lambda event: removePopUpMenu(root, popup_menu))
    global Tabs, top_tab_id
    Tabs = []

    top_tab_id = [0]
    root.mainloop()


if __name__ == '__main__':

    Quode()
