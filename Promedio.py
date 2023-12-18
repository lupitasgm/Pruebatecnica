from tkinter import *
from tkinter import ttk
import subprocess
from SqlCon import connectDB

#conexión con la bd
conn = connectDB() 
cursor = conn.cursor()

def promedio():
    departamento = entradadepartamento.get()
    iddepartamento = departamentos.get(departamento)
    #query
    cursor.execute('''
        SELECT AVG(Salario) FROM Empleados WHERE IdDepartamento = ?
    ''', (iddepartamento))

    promediosalario = cursor.fetchone()[0]
    conn.commit()

    if promediosalario == None:
        txt.config(text=f"No hay empleados en esta área")
    else:
        promediosalario = round(promediosalario, 2)
        txt.config(text=f"El salario promedio en el departamento es: {promediosalario}")

def abrir_menu():
    subprocess.Popen(["python", "Menu.py"])
    ventana.destroy()

#query para combobox
cursor.execute('SELECT * FROM Departamentos')
departamentos = {nombre: id_departamento for id_departamento, nombre in cursor.fetchall()}

# vista del promedio de salarios 
ventana = Tk()
ventana.title("Promedio de salarios por departamento")

departamento = Label(ventana, text="Departamento:")
departamento.grid(row= 0, column=0, padx=5, pady=5, sticky="e")

entradadepartamento = ttk.Combobox(ventana, state="readonly", values=list(departamentos.keys()))
entradadepartamento.grid(row = 0, column=1, padx=5, pady=5, sticky="w")

btn2 = Button(ventana, text="Calcular", command=promedio, justify = "center", width=20, height=1)
btn2.grid( row= 0, column = 2, padx = 5, pady = 5, sticky = "w")

txt = Label(ventana, text="", justify="left")
txt.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

btnregresar = Button(ventana, text="Regresar al menu", command=abrir_menu, justify = "center", width=25, height=1)
btnregresar.grid(columnspan=2, pady=5)

ventana.mainloop()