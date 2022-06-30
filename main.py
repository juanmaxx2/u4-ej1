from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
class Aplicacion:
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __composicion = None

    def __init__(self):
        #Ventana
        self.__ventana=Tk()
        self.__ventana.geometry("395x185")
        self.__ventana.title("Calcular IMC")
        self.__ventana.resizable(0, 0)
        self.__peso = StringVar()
        self.__altura = StringVar()
        self.__imc = StringVar()
        self.__composicion = StringVar()
        ttk.Label(text="calculadora de IMC").grid(column=0, row=0,columnspan=2)
        mainframe = ttk.Frame(self.__ventana)
        mainframe.grid(column=0, row=1, columnspan=2)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe["borderwidth"]=2
        mainframe["relief"]="groove"
        #Altura
        ttk.Label(mainframe, text="Altura").grid(column=0, row=0)
        self.alturaEntry=ttk.Entry(mainframe, width=50, textvariable=self.__altura)
        self.alturaEntry.grid(column=1,row=0,sticky=(W, E))
        ttk.Label(mainframe, text="cm").grid(column=2, row=0)
        #Peso
        ttk.Label(mainframe, text="Peso").grid(column=0, row=1)
        self.pesoEntry=ttk.Entry(mainframe, width=50, textvariable=self.__peso)
        self.pesoEntry.grid(column=1,row=1,sticky=(W, E))
        ttk.Label(mainframe, text="Kg").grid(column=2, row=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        #Botones
        tk.Button(self.__ventana, text="calcular", bg='green', fg='white', command=self.calcular).grid(column=1,row=2)
        tk.Button(self.__ventana, text="limpiar", bg='green', fg='white', command=self.limpiar).grid(column=0,row=2)
        #Resultados
        Resultados = ttk.Frame(self.__ventana, padding="3 3 12 12")
        Resultados.grid(column=0,row=3,columnspan=2)
        Resultados.columnconfigure(0,weight = 1)
        Resultados.rowconfigure(0,weight = 1)
        tk.Label(Resultados, text="Tu Indice de Masa Corporal (IMC) se:"). grid(column=0, row=0)
        tk.Label(Resultados, textvariable=self.__imc).grid(column=1, row=0)
        tk.Label(Resultados, textvariable=self.__composicion).grid(column=0,row=1)
        ttk.Button(Resultados, text="salir", command=self.__ventana.destroy).grid(column=0, row=2, columnspan=2)
        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__imc.set('')

    def calcular(self):
        if self.pesoEntry.get()!='':
            try:
                altura = float(self.alturaEntry.get())
                peso = float(self.pesoEntry.get())
                imc = peso/((altura/100)**2)
                if imc<18.5:
                    composicion="Peso inferior al normal"
                elif imc>=18.5 and imc<=24.9:
                    composicion="Normal"
                elif imc>25.0 and imc<=29.9:
                    composicion="Peso superior al normal"
                elif imc>=30:
                    composicion="Obesidad"
                self.__imc.set(str(imc)+"Kg/m2")
                self.__composicion.set(composicion)
            except ValueError:
                messagebox.showerror(tittle="Error de tipo", message="debe ingresar un valor numerico")
                self.__altura.set('')
                self.__peso.set('')
                self.alturaEntry.focus()
        else:
            self.__imc.set('')

def testAPP():
    mi_app = Aplicacion()

if __name__=='__main__':
    testAPP()