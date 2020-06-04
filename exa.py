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

AApellido = Label(text="Apellido:",font=("Agency FB", 14)).place(x=125,y=110)
#Creando la entrada de texto del Apellido
entradaA = StringVar()
txtUsuario = Entry(root,textvariable=entradaA).place(x=180,y=118)

DDia = Label(text="Día:",font=("Agency FB", 14)).place(x=150,y=140)
#Creando la entrada de texto del Día de nacimiento
entradaD = StringVar()
txtUsuario = Entry(root,textvariable=entradaD).place(x=180,y=148)

MMes = Label(text="Mes:",font=("Agency FB", 14)).place(x=146,y=170)
#Creando la entrada de texto del Mes de nacimiento
entradaM = StringVar()
txtUsuario = Entry(root,textvariable=entradaM).place(x=180,y=178)

AAño = Label(text="Año:",font=("Agency FB", 14)).place(x=146,y=200)
#Creando la entrada de texto del Año de nacimiento
entradaAA = StringVar()
txtUsuario = Entry(root,textvariable=entradaAA).place(x=180,y=208)

#Creación de los botones, servirán para formar funciones.
btnFuncion1 = Button(root, text = "Función 1",font=("Agency FB", 8), width=10).place(x=90,y=240)

btnFuncion2 = Button(root, text = "Función 2",font=("Agency FB", 8), width=10).place(x=140,y=240)

btnFuncion3 = Button(root, text = "Función 3",font=("Agency FB", 8), width=10).place(x=190,y=240)



root.mainloop()