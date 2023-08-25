import tkinter as tk
from tkinter import ttk, scrolledtext
#from Constantes.constantes import idiomas

idiomas = [
    'alemán', 'búlgaro', 'checo', 'chino',
    'coreano', 'danés', 'eslovaco', 'esloveno',
    'español', 'estonio', 'finés', 'francés',
    'griego', 'húngaro', 'indonesio', 'inglés',
    'italiano', 'japonés', 'letón', 'lituano',
    'neerlandés', 'noruego', 'polaco', 'portugués',
    'rumano', 'ruso', 'sueco', 'turco', 'ucraniano'
]



def on_select(event):
    selected_item = combo1.get()
    label1.config('Seleccionado: ' + selected_item)

def on_select2(event):
    selected_item = combo2.get()
    label2.config('Seleccionado: ' + selected_item)

def get_text():
    text = cuadro1.get('1.0', 'end-1c')
    mensaje.set(text)


root = tk.Tk()
root.title('Traductor')

frame = tk.Frame(root)
frame.pack()

mensaje = tk.StringVar()

label1 = tk.Label(frame, text='Selecciona un idioma')
label1.grid(row = 0, column=0, padx=10, pady=10)

label2 = tk.Label(frame, text= 'Traducimos en este idioma')
label2.grid(row=0, column=1, padx=10, pady=10)

combo1 = ttk.Combobox(frame, values=idiomas)
combo1.bind('<<Selecciona Idioma>>', on_select)
combo1.grid(row=1, column=0, padx=10, pady=10)

combo2 = ttk.Combobox(frame, values=idiomas)
combo2.bind('<<Selecciona Idioma>>', on_select2)
combo2.grid(row=1, column=1, padx=10, pady=10)

#cuadro1 = tk.Text(frame, width=16, height=4)

cuadro1 = scrolledtext.ScrolledText(frame, wrap='word',
                                    height=4, width=20)
cuadro1.grid(row=2, column=0, padx=10, pady=10)


button = tk.Button(frame, text='Enviar', command = get_text)
button.grid(row=3, column=0, padx=10, pady=2)


cuadro2 = scrolledtext.ScrolledText(frame, 
                                    wrap = 'word',
                                    height=4,
                                    width=20)
cuadro2.grid(
        row = 2,
        column = 1,
        padx=10,
        pady = 10
)


root.mainloop()