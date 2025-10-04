import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
def saludo():
    print("hola mundo")
caja = tkinter.Entry(ventana, font="Arial")
caja.pack()
def texto():
    caja.get()
boton = tkinter.Button(ventana, text= "presiona", command=texto)
boton.pack()
ventana.mainloop()