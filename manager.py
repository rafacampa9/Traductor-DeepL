import tkinter as tk
from Constantes.constantes import BACKGROUND
from screen import Pantalla


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Traductor DeepL')
        
        self.maxsize(560,280)
        self.minsize(560,280)   
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        

        container.configure(background=BACKGROUND)
        

        """container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)"""


        self.frame = {}
        frame = Pantalla(container, self)
        self.frame[Pantalla] = frame
        frame.grid(row=0, column = 0, sticky=tk.NSEW)
        self.show_frame(Pantalla)

    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()
