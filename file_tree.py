from tkinter import Toplevel
from tkinter.ttk import Treeview

import os


class FileTree(Toplevel):

    def __init__(self, master, path):

        self.master = master
        self.path = path
        self.fileTreeWindow = Toplevel(master=self.master)
        #self.fileTreeWindow.configure(width=200)
        self.tree = Treeview(self.fileTreeWindow, height=30)
        abspath = os.path.abspath(self.path)
        self.root_node = self.tree.insert('',
                            'end',
                            text=abspath,
                            open=True)
        self.process_directory(self.root_node,
                            abspath)
        self.tree.pack(fill='x')
        self.tree.bind('<Double-Button-1>',
                        func=self.openFile)
        self.fileTreeWindow.mainloop()

    def process_directory(self, parent, path):
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            isdir = os.path.isdir(abspath)
            oid = self.tree.insert(parent, 'end',
                                text=p,
                                open=False,
                                iid=str(abspath))
            # print(oid)
            if isdir:
                self.process_directory(oid, abspath)

    def openFile(self, e):

        file_path = self.tree.identify_row(e.y)
        self.master.master.master.openFileByName(file_path)
