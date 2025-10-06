import tkinter as tk


contador_clics = 0

def incrementar_contador():
    """Función que se llama al presionar el botón."""
    global contador_clics
   
    contador_clics += 1
    
    etiqueta_contador.config(text=f"Clics: {contador_clics}")

app4 = tk.Tk()
app4.title("4. Contador de Clics")
app4.geometry("250x120")

etiqueta_contador = tk.Label(app4, text="Clics: 0", font=("Arial", 16))
etiqueta_contador.pack(pady=15)

tk.Button(app4, text="¡Clic Aquí!", command=incrementar_contador).pack()
