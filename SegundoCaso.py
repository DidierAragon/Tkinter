import tkinter as tk
def calcular():
    comida = float(entry_comida.get())
    musica = float(entry_musica.get())
    decoracion = float(entry_decoracion.get())
    transporte = float(transporte.get())
    total= comida + musica + decoracion + transporte
    total_config= f"total: {total}"
    total_config(text ="total")
    total.pack(pady=10)
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

tk.Button(app1, text="calcular", command=calcular).grid(row=4, column=0,)
app1.mainloop()
