import subprocess
from tkinter import *


class MenudeFunciones:
    # Funciones por proceso  

    def abrir_Empleados():
        subprocess.Popen(["python", "Empleados.py"])
        ventanamenu.destroy()

    def abrir_IngresarEmpleado():
        subprocess.Popen(["python", "IngresarEmpleado.py"])
        ventanamenu.destroy()

    def abrir_Modificar():
        subprocess.Popen(["python", "Modificar.py"])
        ventanamenu.destroy()

    def abrir_Eliminar():
        subprocess.Popen(["python", "Eliminar.py"])
        ventanamenu.destroy()

    def abrir_IngresarDepartamento():
        subprocess.Popen(["python", "IngresarDepartamento.py"])
        ventanamenu.destroy()

    def abrir_Promedio():
        subprocess.Popen(["python", "Promedio.py"])
        ventanamenu.destroy()

    def cerrar():
        ventanamenu.destroy()

#Vista del menú 
ventanamenu = Tk()
ventanamenu.title("Gestión de empleados")
ventanamenu.geometry("400x300")

etiqueta_mensaje = Label(ventanamenu, text="Menú de opciones", font=("", 14))
etiqueta_mensaje.pack(pady=3)

btn1 = Button(ventanamenu, text="Lista de empleados", command=MenudeFunciones.abrir_Empleados, justify = "center", width=30, height=1)
btn1.pack(pady=3)
btn2 = Button(ventanamenu, text="Ingresar empleado", command=MenudeFunciones.abrir_IngresarEmpleado, justify = "center", width=30, height=1)
btn2.pack(pady=3)
btn3 = Button(ventanamenu, text="Modificar empleado", command=MenudeFunciones.abrir_Modificar,justify = "center", width=30, height=1)
btn3.pack(pady=3)
btn4 = Button(ventanamenu, text="Eliminar empleado", command=MenudeFunciones.abrir_Eliminar,justify = "center", width=30, height=1)
btn4.pack(pady=3)
btn5 = Button(ventanamenu, text="Ingresar un nuevo departamento", command=MenudeFunciones.abrir_IngresarDepartamento, justify = "center", width=30, height=1)
btn5.pack(pady=3)
btn6 = Button(ventanamenu, text="Promedio de salarios", command=MenudeFunciones.abrir_Promedio, justify = "center", width=30, height=1)
btn6.pack(pady=3)
btn7 = Button(ventanamenu, text="Cerrar programa", command=MenudeFunciones.cerrar, justify = "center", width=30, height=1)
btn7.pack(pady=3)

ventanamenu.mainloop()