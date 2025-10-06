import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    """Muestra un mensaje emergente con los datos ingresados."""
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()
    
    mensaje = (f"Registro Exitoso:\n"
               f"Nombre: {nombre}\n"
               f"Edad: {edad}\n"
               f"Correo: {correo}")
    
    # Muestra el mensaje emergente
    messagebox.showinfo("Datos Ingresados", mensaje)

app1 = tk.Tk()
app1.title("1. Formulario de Registro")

# Nombre
tk.Label(app1, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_nombre = tk.Entry(app1, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Edad
tk.Label(app1, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_edad = tk.Entry(app1, width=30)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Correo Electrónico
tk.Label(app1, text="Correo:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_correo = tk.Entry(app1, width=30)
entry_correo.grid(row=2, column=1, padx=5, pady=5)

# Botón Guardar
tk.Button(app1, text="Guardar", command=guardar_datos).grid(row=3, column=0, columnspan=2, pady=10)

# app1.mainloop() # Descomentar para ejecutar solo este ejercicio