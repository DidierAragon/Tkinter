import tkinter as tk

def convertir_temperatura():
    """Realiza la conversión C a F o F a C."""
    try:
        valor = float(entry_valor.get())
        conversion = var_conversion.get()
        resultado = ""

        if conversion == "C a F":
            # Fórmula: F = C * 9/5 + 32
            resultado = (valor * 9/5) + 32
            etiqueta_resultado.config(text=f"Resultado: {resultado:.2f} °F")
        elif conversion == "F a C":
           
            resultado = (valor - 32) * 5/9
            etiqueta_resultado.config(text=f"Resultado: {resultado:.2f} °C")
        else:
            etiqueta_resultado.config(text="Seleccione un tipo de conversión.")

    except ValueError:
        etiqueta_resultado.config(text="Error: Ingrese un número válido.")

app2 = tk.Tk()
app2.title("2. Conversor de Temperaturas")

tk.Label(app2, text="Valor:").pack(pady=5)
entry_valor = tk.Entry(app2, width=15)
entry_valor.pack(pady=5)


var_conversion = tk.StringVar(value="C a F") 


tk.Radiobutton(app2, text="Celsius a Fahrenheit", variable=var_conversion, value="C a F").pack()
tk.Radiobutton(app2, text="Fahrenheit a Celsius", variable=var_conversion, value="F a C").pack()

tk.Button(app2, text="Convertir", command=convertir_temperatura).pack(pady=10)


etiqueta_resultado = tk.Label(app2, text="Resultado: ")
etiqueta_resultado.pack(pady=10)

app2.mainloop()