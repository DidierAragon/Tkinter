import tkinter as tk
from tkinter import messagebox

app1 = tk.Tk()
app1.title("Calcular")

tk.Label(app1, text="comida:").grid(row=0, column=0, padx=5)
entry_comida = tk.Entry(app1, width=30)
entry_comida.grid(row=0, column=1, padx=5, pady=5)

tk.Label(app1, text="musica:").grid(row=1, column=0, padx=5)
entry_musica = tk.Entry(app1, width=30)
entry_musica.grid(row=1, column=1, padx=5, pady=5)

tk.Label(app1, text="decoracion:").grid(row=2, column=0, padx=5)
entry_decoracion = tk.Entry(app1, width=30)
entry_decoracion.grid(row=2, column=1, padx=5, pady=5)

tk.Label(app1, text="transporte:").grid(row=3, column=0, padx=5)
entry_transporte = tk.Entry(app1, width=30)
entry_transporte.grid(row=3, column=1, padx=5, pady=5)

def calcular():
    try:
        comida = float(entry_comida.get() or 0)
        musica = float(entry_musica.get() or 0)
        decoracion = float(entry_decoracion.get() or 0)
        transporte = float(entry_transporte.get() or 0)
        total = comida + musica + decoracion + transporte
        result_label.config(text=f"Total: {total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Introduce números válidos en los campos")

tk.Button(app1, text="calcular", command=calcular).grid(row=4, column=0, padx=5, pady=5)
result_label = tk.Label(app1, text="Total: 0.00", font=("Arial",12))
result_label.grid(row=4, column=1, padx=5)
app1.mainloop()
