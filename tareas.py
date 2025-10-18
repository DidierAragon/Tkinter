import tkinter as tk

def agregar_tarea():
    """Añade el texto de la entrada a la Listbox."""
    tarea = entry_tarea.get()
    if tarea:
        listbox_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)

def eliminar_tarea():
    """Elimina la tarea seleccionada de la Listbox."""
    try:
     
        indice_seleccionado = listbox_tareas.curselection()
        
        listbox_tareas.delete(indice_seleccionado)
    except:
        
        pass

app3 = tk.Tk()
app3.title("3. Lista de Tareas")


entry_tarea = tk.Entry(app3, width=50)
entry_tarea.pack(pady=10, padx=10)


frame_botones = tk.Frame(app3)
frame_botones.pack(pady=5)

tk.Button(frame_botones, text="Agregar", command=agregar_tarea).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea).pack(side=tk.LEFT, padx=5)


listbox_tareas = tk.Listbox(app3, width=50, height=10)
listbox_tareas.pack(pady=10, padx=10)
app3.mainloop()
