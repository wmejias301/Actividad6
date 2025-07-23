import tkinter as tk
from tkinter import ttk, messagebox
import os

ARCHIVO_DATOS = "amigos.txt"

def guardarDatos(nombre, telefono):
    if not nombre or not telefono:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return
    with open(ARCHIVO_DATOS, "a") as archivo:
        archivo.write(f"{nombre},{telefono}\n")
    messagebox.showinfo("Éxito", "Amigo guardado correctamente.")
    entradaNombreCrear.delete(0, tk.END)
    entradaTelefonoCrear.delete(0, tk.END)

def mostrarDatos():
    areaTextoLeer.delete(1.0, tk.END)
    if not os.path.exists(ARCHIVO_DATOS):
        return
    with open(ARCHIVO_DATOS, "r") as archivo:
        for linea in archivo:
            nombre, telefono = linea.strip().split(",")
            areaTextoLeer.insert(tk.END, f"Nombre: {nombre}, Teléfono: {telefono}\n")

def actualizarDatos(nombreAntiguo, telefonoNuevo):
    if not nombreAntiguo or not telefonoNuevo:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return

    if not os.path.exists(ARCHIVO_DATOS):
        messagebox.showwarning("Advertencia", "No hay datos guardados.")
        return

    actualizado = False
    lineasActualizadas = []
    with open(ARCHIVO_DATOS, "r") as archivo:
        for linea in archivo:
            nombre, telefono = linea.strip().split(",")
            if nombre == nombreAntiguo:
                lineasActualizadas.append(f"{nombre},{telefonoNuevo}\n")
                actualizado = True
            else:
                lineasActualizadas.append(linea)

    with open(ARCHIVO_DATOS, "w") as archivo:
        archivo.writelines(lineasActualizadas)

    if actualizado:
        messagebox.showinfo("Éxito", "Teléfono actualizado correctamente.")
    else:
        messagebox.showwarning("Error", "No se encontró el nombre ingresado.")

def eliminarDatos(nombreAEliminar):
    if not nombreAEliminar:
        messagebox.showwarning("Advertencia", "Debes ingresar un nombre.")
        return

    if not os.path.exists(ARCHIVO_DATOS):
        messagebox.showwarning("Advertencia", "No hay datos guardados.")
        return

    eliminado = False
    lineasRestantes = []
    with open(ARCHIVO_DATOS, "r") as archivo:
        for linea in archivo:
            nombre, telefono = linea.strip().split(",")
            if nombre != nombreAEliminar:
                lineasRestantes.append(linea)
            else:
                eliminado = True

    with open(ARCHIVO_DATOS, "w") as archivo:
        archivo.writelines(lineasRestantes)

    if eliminado:
        messagebox.showinfo("Éxito", "Amigo eliminado correctamente.")
    else:
        messagebox.showwarning("Error", "No se encontró el nombre ingresado.")

colorFondo = "#ffe5e5"

# Interfaz Gráfica
ventana = tk.Tk()
ventana.title("Gestor de Amigos")
ventana.geometry("400x350")
ventana.iconbitmap("Contact.ico")

pestanas = ttk.Notebook(ventana)

# Pestaña Crear
pestanaCrear = ttk.Frame(pestanas)
pestanas.add(pestanaCrear, text="Crear")


ttk.Label(pestanaCrear, text="Nombre:").pack(pady=5)
entradaNombreCrear = ttk.Entry(pestanaCrear)
entradaNombreCrear.pack()

ttk.Label(pestanaCrear, text="Teléfono:").pack(pady=5)
entradaTelefonoCrear = ttk.Entry(pestanaCrear)
entradaTelefonoCrear.pack()

ttk.Button(pestanaCrear, text="Guardar Amigo", command=lambda: guardarDatos(entradaNombreCrear.get(), entradaTelefonoCrear.get())).pack(pady=10)

# Pestaña Leer
pestanaLeer = ttk.Frame(pestanas)
pestanas.add(pestanaLeer, text="Leer")

areaTextoLeer = tk.Text(pestanaLeer, height=15)
areaTextoLeer.pack(expand=True, fill="both", padx=10, pady=10)

ttk.Button(pestanaLeer, text="Mostrar Amigos", command=mostrarDatos).pack(pady=5)

# Pestaña Actualizar
pestanaActualizar = ttk.Frame(pestanas)
pestanas.add(pestanaActualizar, text="Actualizar")

ttk.Label(pestanaActualizar, text="Nombre:").pack(pady=5)
entradaNombreActualizar = ttk.Entry(pestanaActualizar)
entradaNombreActualizar.pack()

ttk.Label(pestanaActualizar, text="Nuevo Teléfono:").pack(pady=5)
entradaTelefonoActualizar = ttk.Entry(pestanaActualizar)
entradaTelefonoActualizar.pack()

ttk.Button(pestanaActualizar, text="Actualizar Teléfono", command=lambda: actualizarDatos(entradaNombreActualizar.get(), entradaTelefonoActualizar.get())).pack(pady=10)

# Pestaña Eliminar
pestanaEliminar = ttk.Frame(pestanas)
pestanas.add(pestanaEliminar, text="Eliminar")

ttk.Label(pestanaEliminar, text="Nombre a eliminar:").pack(pady=5)
entradaNombreEliminar = ttk.Entry(pestanaEliminar)
entradaNombreEliminar.pack()

ttk.Button(pestanaEliminar, text="Eliminar Amigo", command=lambda: eliminarDatos(entradaNombreEliminar.get())).pack(pady=10)

# # Edit Pestañas
pestanas.pack(expand=True, fill="both")
estilo = ttk.Style()
estilo.theme_use("default")

# Área del Notebook
estilo.configure("TNotebook", background="#E9967A", borderwidth=0)

# Pestañas
estilo.configure("TNotebook.Tab", background="#f28c8c", foreground="black", padding=10)
estilo.map("TNotebook.Tab", background=[("selected", "#cc0000")], foreground=[("selected", "white")])

# Fondo para los frames/pestañas
estilo.configure("EstiloRojo.TFrame", background="#E9967A")

# Aplicar estilo a las pestañas
pestanaCrear.config(style="EstiloRojo.TFrame")
pestanaLeer.config(style="EstiloRojo.TFrame")
pestanaActualizar.config(style="EstiloRojo.TFrame")
pestanaEliminar.config(style="EstiloRojo.TFrame")

ventana.mainloop()
