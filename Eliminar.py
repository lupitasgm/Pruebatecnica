from tkinter import *
from tkinter import ttk, messagebox
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

#funciones
def eliminar():
    idEmpleado = entradaid.get()

    cursor.execute('''
        SELECT * FROM Empleados WHERE IdEmpleado = ?
    ''', (idEmpleado))

    empleado = cursor.fetchone()

    if empleado:
        cursor.execute('''
        DELETE FROM Empleados WHERE IdEmpleado = ?
        ''', (idEmpleado))

        conn.commit()
        messagebox.showinfo("Eliminado", "Los datos del empleado han sido eliminados.")

        id.delete(0, 'end')

    else:
        messagebox.showinfo("Error", "No se encontró al empleado.")

def menu():
    subprocess.Popen(["python", "Menu.py"])
    eliminarempleado.destroy()

#vista para eliminar empleados 
eliminarempleado = Tk()
eliminarempleado.title("Eliminar empleado")

id = Label(eliminarempleado, text = "Id del empleado:", justify = "center")
id.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entradaid = Entry(eliminarempleado)
entradaid.grid( row= 1, column = 1, padx = 5, pady = 5, sticky = "w")

btneliminarempleado = Button(eliminarempleado, text="Eliminar", command=eliminar, justify = "center", width=20, height=1)
btneliminarempleado.grid( row= 1, column = 2, padx = 5, pady = 5, sticky = "w")

btnregresar = Button(eliminarempleado, text="Regresar al menu", command=menu, justify = "center", width=25, height=1)
btnregresar.grid(columnspan=2, pady=5)

eliminarempleado.mainloop()