from tkinter import *

root = Tk()

ancho = 400
alto = 400

root.geometry(str(ancho)+'x'+str(alto))
root.title('Examen Final')

Magua = Label(text="GitHub: Bradleyivme",font=("Agency FB",8)).place(x=20,y=10)
Saludo = Label(text="Bienvenido",font=("Agency FB",25)).place(x=150,y=20)

NNombre = Label(text="Nombre:",font=("Agency FB", 14)).place(x=125,y=80)
#Creando la entrada de texto de Nombre
entradaN = StringVar()
txtUsuario = Entry(root,textvariable=entradaN).place(x=180,y=88)

root.mainloop()