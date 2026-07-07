import tkinter as tk
from tkinter import ttk, messagebox
from datos import productos


def cargar_tabla(tabla):
    """Carga los productos en la tabla."""

    for item in tabla.get_children():
        tabla.delete(item)

    for producto in productos:
        tabla.insert(
            "",
            "end",
            values=(
                producto["codigo"],
                producto["nombre"],
                producto["cantidad"],
                producto["precio"]
            )
        )


def eliminar_producto(tabla):

    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showwarning(
            "Aviso",
            "Seleccione un producto."
        )
        return

    indice = tabla.index(seleccionado)

    respuesta = messagebox.askyesno(
        "Confirmar",
        "¿Desea eliminar este producto?"
    )

    if respuesta:
        productos.pop(indice)
        cargar_tabla(tabla)

        messagebox.showinfo(
            "Éxito",
            "Producto eliminado correctamente."
        )
        
def crear_pantalla_eliminar(root, volver):

    frame = tk.Frame(root, bg="#F4F6F8")

    titulo = tk.Label(
        frame,
        text="🗑️ Eliminar Producto",
        font=("Segoe UI", 24, "bold"),
        bg="#F4F6F8",
        fg="#E74C3C"
    )
    titulo.pack(pady=20)

    tabla = ttk.Treeview(
        frame,
        columns=("Código", "Nombre", "Cantidad", "Precio"),
        show="headings",
        height=12
    )

    tabla.heading("Código", text="Código")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Precio", text="Precio")

    tabla.column("Código", width=120, anchor="center")
    tabla.column("Nombre", width=250, anchor="center")
    tabla.column("Cantidad", width=120, anchor="center")
    tabla.column("Precio", width=120, anchor="center")

    tabla.pack(pady=20)

    # Cargar los productos registrados
    cargar_tabla(tabla)

    botones = tk.Frame(frame, bg="#F4F6F8")
    botones.pack(pady=15)

    btn_eliminar = tk.Button(
        botones,
        text="Eliminar",
        bg="#E74C3C",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        cursor="hand2",
        command=lambda: eliminar_producto(tabla)
    )
    btn_eliminar.grid(row=0, column=0, padx=10)

    btn_volver = tk.Button(
        botones,
        text="Volver",
        bg="#2980B9",
        fg="white",
        font=("Segoe UI", 12, "bold"),
        cursor="hand2",
        command=volver
    )
    btn_volver.grid(row=0, column=1, padx=10)

    return frame