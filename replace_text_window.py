from tkinter import Toplevel
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import messagebox

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
        self.replace_button = Button(self,
                                    text="Replace All",
                                    command=self.replaceAll)

        self.find_label.place_configure(relx=0,
                                        rely=0.1,
                                        relheight=0.2,
                                        relwidth=0.4)
        self.new_str_label.place_configure(relx=0,
                                        rely=0.5,
                                        relheight=0.2,
                                        relwidth=0.4)
        self.find_entry.place_configure(relx=0.5,
                                        rely=0.1,
                                        relheight=0.2,
                                        relwidth=0.4)
        self.new_str_entry.place_configure(relx=0.5,
                                        rely=0.5,
                                        relheight=0.2,
                                        relwidth=0.4)
        self.replace_button.place_configure(relx=0.3,
                                        rely=0.8,
                                        relheight=0.15,
                                        relwidth=0.4)

        self.mainloop()

    def replaceAll(self):

        self.replaces = self.master.replaceAll(self.find_entry.get(),
                                            self.new_str_entry.get())
        messagebox.showinfo("Replaced",
                            "Replaced %d occurances" % self.replaces)
