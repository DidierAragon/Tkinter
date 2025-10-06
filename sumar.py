# Importar Tkinter como tk
import tkinter as tk

# ----------------- Funciones -----------------
def Sumar():
    try:
        # Obtener los valores de las entradas y convertirlos a flotante
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        # Realizar la suma
        resultado.set(n1 + n2) 
        
    except ValueError:
        # En caso de que la entrada no sea un número
        resultado.set("Error") 

# ----------------- Ventana principal -----------------
# Crear la ventana principal de la aplicación
Ventana = tk.Tk()
Ventana.title("Calculadora básica")

# Definir el tamaño de la ventana
Ventana.geometry("250x180") # Tamaño

# Variable especial de Tkinter para almacenar el resultado
resultado = tk.StringVar() 

# ----------------- WIDGETS -----------------
# Etiqueta para el Número 1
tk.Label(Ventana, text="Numero 1:").pack(padx=5) 
# Campo de entrada para el primer número
entrada1 = tk.Entry(Ventana)
entrada1.pack() 

# Etiqueta para el Número 2
tk.Label(Ventana, text="Numero 2:").pack(padx=5)
# Campo de entrada para el segundo número
entrada2 = tk.Entry(Ventana)
entrada2.pack()

# Botón para Sumar, que llama a la función Sumar
tk.Button(Ventana, text="Sumar", command=Sumar).pack()

# Etiqueta para mostrar la palabra "Resultado:"
tk.Label(Ventana, text="Resultado:").pack()
# Etiqueta para mostrar el resultado, enlazada a la variable 'resultado'
tk.Label(Ventana, textvariable=resultado, fg="blue").pack()

# ----------------- Loop Principal -----------------
# Iniciar el bucle de eventos de la ventana
Ventana.mainloop()