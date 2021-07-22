import webbrowser
from tkinter import *

raiz = Tk( )
raiz.title('Abrir Browser')
raiz.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

my_google = Button(raiz, text='Abrir o site do Google.', command=google).pack(pady=20)

raiz.mainloop()

