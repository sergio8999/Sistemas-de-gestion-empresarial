import pickle
from dataclasses import dataclass
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

@dataclass
class Alumno:
    nombre: str
    apellidos : str
    edad: int
    nota: float

listaAlumnos =[]

def anadirAlumno():
    nombre = txtNombre.get()
    apellidos = txtApellidos.get()
    edad = txtEdad.get()
    nota = txtNota.get()
    try:
        alumno = Alumno(nombre, apellidos, int(edad), float(nota))
        listaAlumnos.append(alumno)
        guardarCambios()
        borrarCampos()
        rellenarTabla()
    except:
        messagebox.showinfo(message="Escriba los datos correctamente", title="Error datos añadir")

def guardarCambios():
    datos = open("datos", "wb")
    pickle.dump(listaAlumnos, datos)
    datos.close()
    del (datos)

def leerArchivo():
    try:
        with open("datos","rb") as datos:
            listaAlumnos = pickle.load(datos)

            print(listaAlumnos)
            return listaAlumnos
    except:
        return []

def listarAlumnos():
    print(listaAlumnos)

def modificarAlumno():
    nombre = txtNombre.get()
    apellidos = txtApellidos.get()
    edad = txtEdad.get()
    nota = txtNota.get()
    try:
        alumno = Alumno(nombre, apellidos, int(edad), float(nota))
        listaAlumnos[tree.selection()[0]] = alumno
        guardarCambios()
        borrarCampos()
        rellenarTabla()
    except:
        messagebox.showinfo(message="Escriba los datos correctamente", title="Error datos modificar")

def borrarAlumno():
    if(len(tree.selection())):
        if(messagebox.askyesno(message="¿Desea borrarlo?", title="Borrar alumno")):
            del listaAlumnos[int(tree.selection()[0])]
            guardarCambios()
            borrarCampos()
            rellenarTabla()
    else:
        messagebox.showinfo(message="Selecciona fila", title="Error selección fila")


def borrarCampos():
    txtNombre.delete(0,"end")
    txtApellidos.delete(0,"end")
    txtEdad.delete(0,"end")
    txtNota.delete(0,"end")

def rellenarTabla():
    tree.delete(*tree.get_children())

    for indice,alumno in enumerate(listaAlumnos):
        tree.insert('', index=indice, id= indice,values=(alumno.nombre,alumno.apellidos,alumno.edad,alumno.nota))


def itemSeleccionado(event):
    print()
    if(len(tree.selection())):
        borrarCampos()
        item = tree.item(tree.selection()[0])
        alumno = item['values']
        txtNombre.insert(0,alumno[0])
        txtApellidos.insert(0,alumno[1])
        txtEdad.insert(0,alumno[2])
        txtNota.insert(0,alumno[3])



if __name__ == '__main__':

    listarAlumnos()
    listaAlumnos = leerArchivo()

    # Añadir ventana con titulo
    window = tk.Tk()
    window.title("Alumnos")
    window.configure(padx=10, pady=10)
    window.geometry("900x400")

    lblNombre = Label(window, text="Nombre", font=("Arial Bold", 10))
    lblNombre.grid(column=0, row=0, pady=10)

    txtNombre = Entry(window, width=10)
    txtNombre.grid(column=1, row=0, pady=10)
    txtNombre.configure(width=20)

    lblApellidos = Label(window, text="Apellidos", font=("Arial Bold", 10))
    lblApellidos.grid(column=2, row=0, pady=10)

    txtApellidos = Entry(window, width=10)
    txtApellidos.grid(column=3, row=0, pady=10)
    txtApellidos.configure(width=20)

    lblEdad = Label(window, text="Edad", font=("Arial Bold", 10))
    lblEdad.grid(column=0, row=1,pady=10)

    txtEdad = Entry(window, width=10)
    txtEdad.grid(column=1, row=1, pady=10)
    txtEdad.configure(width=20)

    lblNota = Label(window, text="Nota", font=("Arial Bold", 10))
    lblNota.grid(column=2, row=1, pady=10)

    txtNota = Entry(window, width=10)
    txtNota.grid(column=3, row=1, pady=10)
    txtNota.configure(width=20)

    btnAnadir = Button(window, text="Añadir", command=anadirAlumno)
    btnAnadir.grid(column=1, row=2, pady=10)

    btnModificar = Button(window, text="Modificar", command=modificarAlumno)
    btnModificar.grid(column=2, row=2, pady=10)

    btnBorrar = Button(window, text="Borrar", command=borrarAlumno)
    btnBorrar.grid(column=3, row=2, pady=10)

    columnas = ('Nombre', 'Apellidos', 'Edad', "Nota")

    tree = ttk.Treeview(window, columns=columnas, show='headings')

    # define headings
    tree.heading('Nombre', text='Nombre')
    tree.heading('Apellidos', text='Apellidos')
    tree.heading('Edad', text='Edad')
    tree.heading('Nota', text='Nota')

    tree.bind('<<TreeviewSelect>>', itemSeleccionado)
    tree.grid(column=0, columnspan =4, row=3, sticky='nsew')
    rellenarTabla()
    # add a scrollbar
    scrollbar = ttk.Scrollbar(window, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=3, column=5, sticky='ns')

    # Final
    window.mainloop()
