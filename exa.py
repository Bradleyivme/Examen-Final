from tkinter import *
from datetime import date
from datetime import datetime

root = Tk()

ancho = 400
alto = 400

#Geometría de la ventana
root.geometry(str(ancho)+'x'+str(alto))
root.title('Examen Final')

#Marca de agua
Magua = Label(text="GitHub: Bradleyivme",font=("Agency FB",8))
Magua.grid(row=0, column=0)

#Título principal
Saludo = Label(text="Bienvenido",font=("Agency FB",25))
Saludo.grid(row=1, column=1, columnspan=6)

#Etiquetas principales

Nombre = Label(text="Nombre:",font=("Agency FB", 14))
Nombre.grid(row=2, column=1, columnspan=2)
#Creando la entrada de texto de Nombre
txtUsuarioN = Entry(root)
txtUsuarioN.grid(row=2, column=3, columnspan=4, sticky= W + E)

Apellido = Label(text="Apellido:",font=("Agency FB", 14))
Apellido.grid(row=3, column=1, columnspan=2)
#Creando la entrada de texto del Apellido
txtUsuarioA = Entry(root)
txtUsuarioA.grid(row=3, column=3, columnspan=4, sticky= W + E)

Dia = Label(text="Día:",font=("Agency FB", 14))
Dia.grid(row=4, column=1, columnspan=2)
#Creando la entrada de texto del Día de nacimiento
txtUsuarioD = Entry(root)
txtUsuarioD.grid(row=4, column=3, columnspan=4, sticky= W + E)

Mes = Label(text="Mes:",font=("Agency FB", 14))
Mes.grid(row=5, column=1, columnspan=2)
#Creando la entrada de texto del Mes de nacimiento
txtUsuarioM = Entry(root)
txtUsuarioM.grid(row=5, column=3, columnspan=4, sticky= W + E)

Año = Label(text="Año:",font=("Agency FB", 14))
Año.grid(row=6, column=1, columnspan=2)
#Creando la entrada de texto del Año de nacimiento
txtUsuarioAA = Entry(root)
txtUsuarioAA.grid(row=6, column=3, columnspan=4, sticky= W + E)

#Función de verifiación de número pares en el nombre y apellido del usuario
def PareImpar():
    
    NombreV = f"{txtUsuarioN.get()}"
    ApellidoV = f"{txtUsuarioA.get()}"

    NumerosofN = len(NombreV)
    NumerosofA = len(ApellidoV)
  
    if NumerosofN % 2 == 0:
        c3 = f"{NombreV} su nombre es de par"
    else:
        c3 = f"{NombreV} su nombre es de impar"

    if NumerosofA % 2 == 0:
        c4 = f"{ApellidoV} su apellido es par."
    else:
        c4 = f"{ApellidoV} su apellido es de impar."

    Salida2 = f"{c3} y  {c4} "

    Resultado["text"] = Salida2


#Función de días vividos según, la fecha que ingrese el usuario
def díasvividos():
    fechaString = f"{txtUsuarioAA.get()}-{txtUsuarioD.get()}-{txtUsuarioM.get()}"
    dato = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    c1 = today
    c2 = dato
    Salida1 = abs(c1-c2).days 

    Salida = f"Usted nacio el {dato} y ha vivido {Salida1} días."

    Resultado["text"] = Salida


#Función de reversa, el texto lo pega al revés.
def textos():
    text20 = txtUsuarioN.get()+" "+txtUsuarioA.get()
    text20 = text20[::-1]
    Resultado["text"] = txtUsuarioN.get() + " " + txtUsuarioA.get() + " al revés es: " + text20

#Creación de los botones, servirán para llamar funciones.
btnFuncion1 = Button(root, text = "Función 1",font=("Agency FB", 8), width=10)
btnFuncion1.grid(row=7, column=1)

btnFuncion2 = Button(root, text = "Función 2",command=díasvividos,font=("Agency FB", 8), width=10)
btnFuncion2.grid(row=7, column=2)

btnFuncion3 = Button(root, text = "Función 3",command=PareImpar,font=("Agency FB", 8), width=10)
btnFuncion3.grid(row=7, column=3)

btnFuncion4 = Button(root, text = "Función 4",font=("Agency FB", 8), width=10)
btnFuncion4.grid(row=7, column=4)

btnFuncion5 = Button(root, text = "Función 5",command=textos,font=("Agency FB", 8), width=10)
btnFuncion5.grid(row=7, column=5)

Resultado = Label(root,font=("Agency FB", 14))
Resultado.grid(row=8, column=1, columnspan=6)

root.mainloop()