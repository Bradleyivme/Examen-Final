from tkinter import *

root = Tk()

ancho = 400
alto = 400

root.geometry(str(ancho)+'x'+str(alto))
root.title('Examen Final')

Magua = Label(text="GitHub: Bradleyivme",font=("Agency FB",8))
Saludo = Label(text="Bienvenido",font=("Agency FB",25))

def Resultado():
    Label(root,text=""+entradaN.get()+entradaA.get(),font=("Agency FB", 14))

NNombre = Label(text="Nombre:",font=("Agency FB", 14))
#Creando la entrada de texto de Nombre
txtUsuario = Entry(root)

AApellido = Label(text="Apellido:",font=("Agency FB", 14))
#Creando la entrada de texto del Apellido
txtUsuario = Entry(root)

DDia = Label(text="Día:",font=("Agency FB", 14))
#Creando la entrada de texto del Día de nacimiento
txtUsuario = Entry(root)

MMes = Label(text="Mes:",font=("Agency FB", 14))
#Creando la entrada de texto del Mes de nacimiento
txtUsuario = Entry(root)

AAño = Label(text="Año:",font=("Agency FB", 14))
#Creando la entrada de texto del Año de nacimiento
txtUsuario = Entry(root)

#Creación de los botones, servirán para formar funciones.
btnFuncion1 = Button(root, text = "Función 1",font=("Agency FB", 8), width=10)


btnFuncion2 = Button(root, text = "Función 2",font=("Agency FB", 8), width=10)


btnFuncion3 = Button(root, text = "Función 3",font=("Agency FB", 8), width=10)


btnFuncion4 = Button(root, text = "Función 4",font=("Agency FB", 8), width=10)


btnFuncion5 = Button(root, text = "Función 5",font=("Agency FB", 8), width=10)


root.mainloop()