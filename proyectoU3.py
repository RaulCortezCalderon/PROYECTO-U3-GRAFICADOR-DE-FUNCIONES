import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import*
import numpy as np
import math

root = Tk()
root.geometry("1150x600")
fig, ax = plt.subplots()

def graficar():
    ax.clear()
    x = np.arange(X1.get(), X2.get(), 0.1) 
    y = A.get()*(x**3)+B.get()*(x**2)+C.get()*x+D.get()
    ax.set_xlim([-10,10])
    ax.set_xlim([-10,10])
    ax.plot(x, y, color = 'black')
    ax.grid(axis = 'both', color = 'blue', linestyle = 'dashed')
    canvas.draw()

def encontrar_raices():
    coeficientes = [A.get(), B.get(), C.get(), D.get()]
    raices = np.roots(coeficientes)
    texto_raices = "Raíces:\n"
    for raiz in raices:
        texto_raices += str(raiz) + "\n"
    etiqueta_raices.config(text=texto_raices)



ax.set_xlabel("eje X")
ax.set_ylabel("eje Y")


A=IntVar()
B=IntVar()
C=IntVar()
D=IntVar()
X1=IntVar()
X2=IntVar()

frame = Frame(root)
frame.pack(fill="both", expand=1)

etiqueta_raices = Label(frame, font=("Roboto", 15))
etiqueta_raices.place(x=850,y=450)


botonRaices = Button(frame, text="BUSCAR RAÍCES", command=encontrar_raices, font=("Roboto", 10))
botonRaices.place(x=882,y=340,width=150,height=35)

titulograf = Label(frame, text="GRAFICADOR Y BUSCADOR DE RAICES  DE UNA FUNCION", font=("Roboto, 15"))
titulograf.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().grid(row=2, column=1, columnspan=4, padx=5, pady=5)

botonGraficar = Button(frame, text="GRAFICAR FUNCION", command=graficar, font=("Roboto", 10))
botonGraficar.place(x=865,y=280,width=200,height=35)

tituloecuacion = Label(frame, text="CUBICA + CUADRATICA + LINEAL + NUMERO REAL", font=("Roboto", 15)).place(x=700,y=50)
tituloA = Label(frame, text="A*X^3",  font=("Roboto", 15)).place(x=715,y=90)
tituloB = Label(frame, text="B*X^2",  font=("Roboto", 15)).place(x=845,y=90)
tituloC = Label(frame, text="C*X",  font=("Roboto", 15)).place(x=960,y=90)
tituloD = Label(frame, text="D",  font=("Roboto", 15)).place(x=1070,y=90)

coeA = Entry(frame, font=("Roboto",10), textvariable=A).place(x=730,y=120,width=25,height=20)
coeB = Entry(frame, font=("Roboto",10), textvariable=B).place(x=860,y=120,width=25,height=20)
coeC = Entry(frame, font=("Roboto",10), textvariable=C).place(x=965,y=120,width=25,height=20)
coeD = Entry(frame, font=("Roboto",10), textvariable=D).place(x=1068,y=120,width=25,height=20)

intervalo1 = Label(frame, text="VALOR INICIAL",  font=("Roboto", 15)).place(x=720,y=170,width=150,height=20)
intervalo2 = Label(frame, text="VALOR FINAL", font=("Roboto", 15)).place(x=950,y=170,width=150,height=20)

X1O = Entry(frame, font=("Roboto",10), textvariable=X1).place(x=770,y=192,width=35,height=20)
X20 = Entry(frame, font=("Roboto",10), textvariable=X2).place(x=1005,y=192,width=35,height=20)

root.mainloop()