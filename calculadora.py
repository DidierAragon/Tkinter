import tkinter as tk
def click_boton(numero):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0,actual + str(numero))
    
def borrar():
    entrada.delete(0, tk.END)
    
def calcular ():
    try:
        resuelto = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resuelto))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "error")
ventana = tk.Tk() #crea la ventana principal
ventana.title("calculadora")#asigna el titulo a la ventana
ventana.geometry("300x400")#define el tamaño de la ventana  
entrada = tk.Entry(ventana,width=20,font=("Arial", 18),
justify="right")
entrada.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
botones = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,2),("=",4,3),
]
for (texto, fila, columna) in botones:
    if texto == "=":
        tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                 command=calcular).grid(row=fila, column=columna, padx=5, pady=5)
    else:
        tk.Button(ventana, text=texto, width=5, height=2, font=("Arial", 14),
                 command=lambda t=texto: click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)

# Botón para borrar
tk.Button(ventana, text='C', width=22, height=2, font=("Arial", 14),
         command=borrar).grid(row=5, column=0, columnspan=4, padx=5, pady=5)
ventana.mainloop()