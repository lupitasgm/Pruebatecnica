from tkinter import *
from tkinter import ttk, messagebox
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

#funciones 
def guardar():
    nombreempleado = entradanombre.get()
    apellidoempleado = entradaapellido.get()
    cargoempleado = entradacargo.get()
    fechacontratacion = entradafechacontratacion.get()
    salarioempleado = entradasalario.get()
    departamento = entradadepartamento.get()
    iddepartamento = departamentos.get(departamento)

    #query
    cursor.execute('''
        INSERT INTO Empleados (Nombre, Apellido, Cargo, FechaContratacion, Salario, IdDepartamento)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nombreempleado, apellidoempleado, cargoempleado, fechacontratacion, salarioempleado, iddepartamento))

    conn.commit()
    messagebox.showinfo("Guardado", "Los datos han sido guardados exitosamente.")

    entradanombre.delete(0, 'end')
    entradaapellido.delete(0, 'end')
    entradacargo.delete(0, 'end')
    entradafechacontratacion.delete(0, 'end')
    entradasalario.delete(0, 'end')
    entradadepartamento.set("")

def menu():
    subprocess.Popen(["python", "Menu.py"])
    ingresarEmpleado.destroy()

#query para combobox
cursor.execute('SELECT * FROM Departamentos')
departamentos = {nombre: id_departamento for id_departamento, nombre in cursor.fetchall()}

#vista para ingresar empleado
ingresarEmpleado = Tk()
ingresarEmpleado.title("Ingresar nuevo empleado")

nombre = Label(ingresarEmpleado, text="Nombre:")
nombre.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
entradanombre = Entry(ingresarEmpleado)
entradanombre.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "w")

apellido = Label(ingresarEmpleado, text="Apellido:")
apellido.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")
entradaapellido = Entry(ingresarEmpleado)
entradaapellido.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")

cargo = Label(ingresarEmpleado, text="Cargo:")
cargo.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "e")
entradacargo = Entry(ingresarEmpleado)
entradacargo.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "w")

fechacontratacion = Label(ingresarEmpleado, text="Fecha de contratación (YY-MM-DD):")
fechacontratacion.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "e")
entradafechacontratacion = Entry(ingresarEmpleado)
entradafechacontratacion.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "w")

salario = Label(ingresarEmpleado, text="Salario:")
salario.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "e")
entradasalario = Entry(ingresarEmpleado)
entradasalario.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "w")

departamento = Label(ingresarEmpleado, text="Departamento:")
departamento.grid(row=5, column=0, padx=5, pady=5, sticky="e")
entradadepartamento = ttk.Combobox(ingresarEmpleado, state="readonly", values=list(departamentos.keys()))
entradadepartamento.grid(row=5, column=1, padx=5, pady=5, sticky="w")

btnagregar = Button(ingresarEmpleado, text="Agregar empleados", command=guardar, justify = "center", width=25, height=1)
btnagregar.grid(row=6, columnspan=2, pady=5)

btnregresar = Button(ingresarEmpleado, text="Regresar al menu", command=menu, justify = "center", width=25, height=1)
btnregresar.grid(row=7, columnspan=2, pady=5)

ingresarEmpleado.mainloop()