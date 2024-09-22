import tkinter as tk
from tkinter import filedialog

# Interfaz gráfica
def crear_interfaz(procesar_archivo_callback):
    # ventana principal
    root = tk.Tk()
    root.title("Validador de Cadenas")
    root.geometry("400x300")

    def seleccionar_archivo():
        archivo = filedialog.askopenfilename(title="Selecciona el archivo", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            procesar_archivo_callback(archivo)

    btn_seleccionar = tk.Button(root, text="Seleccionar Archivo", command=seleccionar_archivo)
    btn_seleccionar.pack(pady=10)

    resultado_text = tk.Text(root, height=10, width=40)
    resultado_text.pack(pady=10)

    def mostrar_resultado(resultado):
        resultado_text.delete(1.0, tk.END) 
        resultado_text.insert(tk.END, resultado)

    return root, mostrar_resultado
