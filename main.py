from tkinter import *
from PIL import Image, ImageTk

class Window (Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH,expand=1)
        '''
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

        '''
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Show Image',command=self.showImg)
        file.add_command(label='Show Text',command=self.showTxt)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo', command=self.client_undo)
        edit.add_command(label='Save', command=self.client_save)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def showImg(self):
        load = Image.open('main_pic.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text='Hello Python')
        text.pack()

    def client_undo(self):
        text = Label(self, text='Option not develop')
        text.pack()

    def client_save(self):
        text = Label(self, text='Option not develop')
        text.pack()


root = Tk()
root.geometry("700x500")

app = Window(root)

root.mainloop()
