import tkinter
from tkinter import *
from tkinter import ttk, messagebox
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

#funciones
def guardar():
    ndepartamento = entradanombre.get()

    cursor.execute('''
        INSERT INTO Departamentos (NombreDepartamento) 
        VALUES (?)
    ''', (ndepartamento))

    conn.commit()
    messagebox.showinfo("Guardado", "Los datos han sido guardados exitosamente.")

    nombre.delete(0, 'end')

def menu():
    subprocess.Popen(["python", "Menu.py"])
    departamentos.destroy()

#vista de ingreso de departamentos
departamentos = Tk()
departamentos.title("Ingresar nuevo Departamento")

nombre = Label(departamentos, text = "Nombre del nuevo departamento:", justify = "center")
nombre.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entradanombre = Entry(departamentos)
entradanombre.grid( row= 1, column = 1, padx = 5, pady = 5, sticky = "w")

btnagregar = Button(departamentos, text="Agregar departamento", command=guardar, justify = "center", width=25, height=1)
btnagregar.grid(columnspan=2, pady=5)

btnegresar = Button(departamentos, text="Regresar al menu", command=menu, justify = "center", width=25, height=1)
btnegresar.grid(columnspan=2, pady=5)

departamentos.mainloop()