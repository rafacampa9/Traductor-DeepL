import tkinter as tk
from tkinter import ttk, scrolledtext
from Constantes.constantes import BACKGROUND, STYLE, IDIOMAS, STYLE2
from web_scraping.web_scraping import traductor


class Pantalla(tk.Frame):
    

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=BACKGROUND)
        self.controller=controller
        self.message = tk.StringVar(self, value='')
        self.answer = tk.StringVar(self, value='')
        self.language = tk.StringVar(self, value='español')
        self.trad = tk.StringVar(self, value='inglés')
        
        
        self.init_widgets()

    
    

        
    
    def init_widgets(self):
        
        
        
        def get_text():
            cuadro2.delete('1.0', 'end')
            text = cuadro1.get('1.0', 'end-1c')
            self.message.set(text)
            #message = self.message.get()
            self.answer = traductor(self.message.get(), self.language.get(), self.trad.get())
            cuadro2.insert('1.0', self.answer)

        def on_enter(event):
            get_text()


        def on_select(event):
            self.language.set(combo1.get())
       

        def on_select2(event):
            self.trad.set(combo2.get())
           
        

        
            

        label1 = tk.Label(
            self,
            text = 'Selecciona un idioma',
            justify=tk.CENTER,
            **STYLE
        ).grid(
            row=0,
            column=0,
            padx=22,
            pady=11,
            sticky='w'
        )

        label2 = tk.Label(
            self,
            text = 'Selecciona un idioma',
            justify=tk.CENTER,
            **STYLE
        ).grid(
            row=0,
            column=1,
            padx=22,
            pady=11,
            sticky='w'
        )

        
        combo1 = ttk.Combobox(
            self,
            values=IDIOMAS
        )

        combo1.set('español')

        combo1.bind(
            '<<ComboboxSelected>>',
            on_select
        )
        combo1.grid(
            row=1,
            column = 0,
            padx = 22,
            pady = 11,
            sticky='w'
        )

        combo2 = ttk.Combobox(
            self,
            values=IDIOMAS,
            
        )

        combo2.set('inglés')

        combo2.bind(
            '<<ComboboxSelected>>',
            on_select2
        )

        combo2.grid(
            row=1,
            column = 1,
            padx = 22,
            pady = 11,
            sticky='w'
        )


        cuadro1 = scrolledtext.ScrolledText(
            self, 
            wrap='word',
            height=4, 
            width=20,
            **STYLE2
        )

        
        cuadro1.grid(
                    row=2, 
                     column=0, 
                     padx=10, 
                     pady=10,
                     sticky='w'
                     )


        cuadro1.bind('<Return>', on_enter)
        button = tk.Button(
            self, 
            text='Enviar', 
            command = get_text,
            relief=tk.FLAT
            )
        
        button.configure(
            **STYLE
        )
        
        button.grid(
            row=3, 
            column=0, 
            padx=10, 
            pady=2,
            sticky='w'
            )


        cuadro2 = scrolledtext.ScrolledText(
            self, 
            wrap = 'word',
            height=4,
            width=20,
            **STYLE2
            )
        
        cuadro2.grid(
            row = 2,
            column = 1,
            padx=10,
            pady = 10,
            sticky='w'
        )