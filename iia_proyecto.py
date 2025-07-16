import tkinter as tk
from tkinter import messagebox

def ventana_reinas():
    ventana_reinas = tk.Toplevel()
    ventana_reinas.title("9 Reinas")
    ventana_reinas.geometry("400x300")
    ventana_reinas.configure(bg="#f0f8ff")

    tk.Label(ventana_reinas, text="Seleccione método para 9 Reinas", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=15)

    def ejecutar_tabú():
        messagebox.showinfo("9 Reinas - Búsqueda Tabú", "Ejecutando Búsqueda Tabú...")

    def ejecutar_recocido():
        messagebox.showinfo("9 Reinas - Recocido Simulado", "Ejecutando Recocido Simulado...")

    def ejecutar_genetico():
        messagebox.showinfo("9 Reinas - Algoritmo Genético", "Ejecutando Algoritmo Genético...")

    tk.Button(ventana_reinas, text="Búsqueda Tabú", command=ejecutar_tabú, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Recocido Simulado", command=ejecutar_recocido, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Algoritmos Genéticos", command=ejecutar_genetico, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Cerrar", command=ventana_reinas.destroy, width=25, bg="#ff6666").pack(pady=20)


def ventana_tsp():
    ventana_tsp = tk.Toplevel()
    ventana_tsp.title("Agente Viajero (TSP)")
    ventana_tsp.geometry("400x250")
    ventana_tsp.configure(bg="#f0fff0")

    tk.Label(ventana_tsp, text="Seleccione método para TSP", font=("Arial", 14, "bold"), bg="#f0fff0").pack(pady=15)

    def ejecutar_tabú():
        messagebox.showinfo("TSP - Búsqueda Tabú", "Ejecutando Búsqueda Tabú...")

    def ejecutar_recocido():
        messagebox.showinfo("TSP - Recocido Simulado", "Ejecutando Recocido Simulado...")

    tk.Button(ventana_tsp, text="Búsqueda Tabú", command=ejecutar_tabú, width=25).pack(pady=5)
    tk.Button(ventana_tsp, text="Recocido Simulado", command=ejecutar_recocido, width=25).pack(pady=5)
    tk.Button(ventana_tsp, text="Cerrar", command=ventana_tsp.destroy, width=25, bg="#ff6666").pack(pady=20)


def ventana_funcion():
    ventana_funcion = tk.Toplevel()
    ventana_funcion.title("Optimización de f(x)")
    ventana_funcion.geometry("400x250")
    ventana_funcion.configure(bg="#fff0f5")

    tk.Label(ventana_funcion, text="Seleccione método para f(x)", font=("Arial", 14, "bold"), bg="#fff0f5").pack(pady=15)

    def ejecutar_busqueda_local():
        messagebox.showinfo("Optimización - Búsqueda Local", "Ejecutando Búsqueda Local...")

    def ejecutar_genetico():
        messagebox.showinfo("Optimización - Algoritmo Genético", "Ejecutando Algoritmo Genético...")

    tk.Button(ventana_funcion, text="Búsqueda Local", command=ejecutar_busqueda_local, width=25).pack(pady=5)
    tk.Button(ventana_funcion, text="Algoritmo Genético", command=ejecutar_genetico, width=25).pack(pady=5)
    tk.Button(ventana_funcion, text="Cerrar", command=ventana_funcion.destroy, width=25, bg="#ff6666").pack(pady=20)

# Ventana principal
ventana = tk.Tk()
ventana.title("Proyecto IA - Menú Principal")
ventana.geometry("450x350")
ventana.configure(bg="#e6f2ff")

tk.Label(ventana, text="MENÚ PRINCIPAL", font=("Arial", 18, "bold"), bg="#e6f2ff").pack(pady=20)

tk.Button(ventana, text="1. Problema de las 9 Reinas", font=("Arial", 14), command=ventana_reinas, width=35).pack(pady=10)
tk.Button(ventana, text="2. Problema del Agente Viajero (TSP)", font=("Arial", 14), command=ventana_tsp, width=35).pack(pady=10)
tk.Button(ventana, text="3. Optimización de f(x)", font=("Arial", 14), command=ventana_funcion, width=35).pack(pady=10)
tk.Button(ventana, text="Salir", font=("Arial", 14), command=ventana.destroy, width=35, bg="#ff9999").pack(pady=15)

ventana.mainloop()
