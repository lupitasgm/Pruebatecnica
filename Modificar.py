from tkinter import *
from tkinter import ttk, messagebox
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

#query para combobox
cursor.execute('SELECT * FROM Departamentos')
departamentos = {nombre: id_departamento for id_departamento, nombre in cursor.fetchall()}

#funciones
def mostrar():
    idEmpleado = entradaid.get()

    cursor.execute('''
        SELECT E.IdEmpleado, E.Nombre AS NombreEmpleado, E.Apellido AS ApellidoEmpleado, E.Cargo,
        E.FechaContratacion, Salario, D.NombreDepartamento AS NombreDepartamento 
        FROM Empleados E JOIN Departamentos D ON E.IdDepartamento = D.IdDepartamento WHERE IdEmpleado = ?
    ''', (idEmpleado))

    empleado = cursor.fetchone()

    print(empleado)

    if empleado:
        entradaid.configure(state='readonly')
        nombre.set(empleado[1])
        apellido.set(empleado[2])
        cargo.set(empleado[3]) 
        fecha.set(empleado[4]) 
        salario.set(empleado[5])
        departamento.set(empleado[6])
    else:
        messagebox.showinfo("Error", "No se encontró al empleado.")

def modificar():
    idEmpleado = entradaid.get()
    nombre = entradanombre.get()
    apellido = entradaapellido.get()
    cargo = entradacargo.get()
    fecha = entradafecha.get()
    salario = entradasalario.get()
    departamento = entradadepartamento.get()
    iddepartamento = departamentos.get(departamento)

    cursor.execute('''
            UPDATE Empleados 
            SET Nombre = ?, Apellido = ?, Cargo = ?, FechaContratacion = ?, Salario = ?, IdDepartamento = ? 
            WHERE IdEmpleado = ?
    ''', (nombre, apellido, cargo, fecha, salario, iddepartamento, idEmpleado))

    conn.commit()
    messagebox.showinfo("Guardado", "Los datos han sido guardados exitosamente.")

    entradanombre.delete(0, 'end')
    entradaapellido.delete(0, 'end')
    entradacargo.delete(0, 'end')
    entradafecha.delete(0, 'end')
    entradasalario.delete(0, 'end')
    entradadepartamento.set("")

def menu():
    subprocess.Popen(["python", "Menu.py"])
    ventanamodificar.destroy()


#vista para modificar empleados
ventanamodificar = Tk()
ventanamodificar.title("Modificar")

id = Label(ventanamodificar, text = "Id del empleado:", justify = "center")
id.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entradaid = Entry(ventanamodificar)
entradaid.grid( row= 1, column = 1, padx = 5, pady = 5, sticky = "w")

btn2 = Button(ventanamodificar, text="Buscar", command=mostrar, justify = "center", width=20, height=1)
btn2.grid( row= 1, column = 2, padx = 5, pady = 5, sticky = "w")

nombre = StringVar()
apellido = StringVar()
cargo = StringVar()
fecha = StringVar()
salario = StringVar()
departamento = StringVar()

entradanombre = Entry(ventanamodificar, textvariable=nombre)
entradanombre.grid(row=2, column=1, padx=5, pady=5, sticky="w")

entradaapellido = Entry(ventanamodificar, textvariable=apellido)
entradaapellido.grid(row=3, column=1, padx=5, pady=5, sticky="w")

entradacargo = Entry(ventanamodificar, textvariable=cargo)
entradacargo.grid(row=4, column=1, padx=5, pady=5, sticky="w")

entradafecha = Entry(ventanamodificar, textvariable=fecha)
entradafecha.grid(row=5, column=1, padx=5, pady=5, sticky="w")

entradasalario = Entry(ventanamodificar, textvariable=salario)
entradasalario.grid(row=6, column=1, padx=5, pady=5, sticky="w")

entradadepartamento = Entry(ventanamodificar, textvariable=departamento)
entradadepartamento.grid(row=7, column=1, padx=5, pady=5, sticky="w")

entradadepartamento = ttk.Combobox(ventanamodificar, state="readonly", textvariable=departamento, values=list(departamentos.keys()))
entradadepartamento.grid(row=7, column=1, padx=5, pady=5, sticky="w")


editar = Button(ventanamodificar, text="Modificar", command=modificar, justify = "center", width=25, height=1)
editar.grid(columnspan=2, pady=5)

btnregresar = Button(ventanamodificar, text="Regresar al menu", command=menu, justify = "center", width=25, height=1)
btnregresar.grid(columnspan=2, pady=5)

ventanamodificar.mainloop()