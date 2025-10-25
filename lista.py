import tkinter as tk
ventana = tk.Tk
ventana.title("lista")
ventana.geometry("400x500")
productos = [{"nombre":"arroz","precio":"2500","stock":"100"},
             {"nombre":"leche","precio":"2500","stock":"30"},
             {"nombre":"azucar","precio":"1200","stock":"35"},
             {"nombre":"huevo","precio":"500","stock":"60"}
            ]
def mostrar_productos():
    boton_mostrar.pack_forget()
    for producto in productos:
        etiqueta = tk.Label(ventana, text=producto, font=("Arial",12))
        etiqueta.pack(pady=3)
boton_mostrar = tk.Button(ventana, text="mostrar productos", font=("Arial",14),command=mostrar_productos)
boton_mostrar.pack(expand=True)
ventana.mainloop()