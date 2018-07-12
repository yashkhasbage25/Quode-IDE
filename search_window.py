from tkinter import Toplevel
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Button
from tkinter import Label
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
        self.search_img_button = Button(self,
                                        image=self.search_img,
                                        bg="white",
                                        command=self.searchText)
        self.found_label = Label(self,
                                text=("Found "+str(self.found)+"\ninstances"),
                                bg="yellow")
        self.next_button = Button(self,
                                image=self.next_img,
                                bg='white',
                                command=self.showNextSearch)

        self.entry.place_configure(relx=0.1,
                                rely=0.15,
                                relheight=0.25,
                                relwidth=0.5)
        self.search_img_button.place_configure(relx=0.65,
                                rely=0.0,
                                relheight=0.5,
                                relwidth=0.3)
        self.found_label.place_configure(relx=0.1,
                                rely=0.5,
                                relheight=0.4,
                                relwidth=0.4)
        self.next_button.place_configure(relx=0.65,
                                rely=0.5,
                                relheight=0.5,
                                relwidth=0.3)

        self.protocol("WM_DELETE_WINDOW", self.closeSearchWindow)

        self.mainloop()

    def searchText(self):

        curr_editor = self.master._get_current_editor()
        start = "1.0"
        text = self.entry.get()
        if text != '':

            curr_editor.tag_config('highlight',
                                    background='green',
                                    foreground='red')
            curr_editor.tag_config('highlight_next',
                                    background='blue',
                                    foreground='purple')
            pos = curr_editor.search(text, start,
                                    stopindex="end")

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

        curr_editor = self.master._get_current_editor()
        # start = "1.0"
        text = self.entry.get()
        if text != '':
            pos = curr_editor.search(text,
                                    self.start_index,
                                    stopindex="end")
            if pos == '':

                self.start_index = "1.0"
                pos = curr_editor.search(text,
                                        self.start_index,
                                        stopindex="end")
            length = len(text)
            row, col = pos.split('.')
            self.stop_index = int(col) + length
            self.stop_index = row + '.' + str(self.stop_index)
            curr_editor.tag_delete('highlight_next')
            curr_editor.tag_add('highlight_next', pos, self.stop_index)
            curr_editor.tag_config('highlight_next',
                                    background='blue',
                                    foreground='purple')
            curr_editor.see(pos)
            self.start_index = self.stop_index
            pos = curr_editor.search(text, self.start_index, stopindex="end")

    def closeSearchWindow(self):

        self.master.removeAllTags()
        self.master.createTags()
        self.master.recolorize(None)
        self.destroy()
