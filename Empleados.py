from tkinter import *
from tkinter import ttk
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

#funciones 
def replacespaces():
    for child in tabla.get_children():
        values = tabla.item(child, 'values')
        new_values = [val.replace('@@@', ' ') for val in values]
        tabla.item(child, values=new_values)

def menu():
    subprocess.Popen(["python", "Menu.py"])
    Empleados.destroy()

#query
SQL_QUERY = """
SELECT E.IdEmpleado, E.Nombre AS NombreEmpleado, E.Apellido AS ApellidoEmpleado, E.Cargo,
       E.FechaContratacion, Salario, D.NombreDepartamento AS NombreDepartamento
FROM Empleados E JOIN Departamentos D ON E.IdDepartamento = D.IdDepartamento;
"""
cursor.execute(SQL_QUERY)
records = cursor.fetchall()

#vista lista de empleados
Empleados = Tk()
Empleados.title("Empleados")

tabla = ttk.Treeview(Empleados)
columnas = [column[0] for column in cursor.description]
tabla["columns"] = tuple(columnas)
tabla.column("#0", width=0, stretch=NO)

for col in columnas:
    tabla.column(col, width=150)

for idx, col_name in enumerate(columnas):
    tabla.heading(idx, text=col_name)
    
for row in records:
    row = list(row) 
    row[5] = f"${row[5]}"
    cleaned_row = [str(field).replace(' ', '@@@') for field in row]
    tabla.insert("", "end", values=cleaned_row)

tabla.pack(expand=True, fill='both')

btnregresar = Button(Empleados, text="Regresar al menu", command=menu, justify = "center", width=30, height=1)
btnregresar.pack(pady=3)

Empleados.after(100, replacespaces)
Empleados.mainloop()