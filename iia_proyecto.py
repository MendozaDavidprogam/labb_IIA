import tkinter as tk
from tkinter import messagebox

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho / 2))
    y = int((pantalla_alto / 2) - (alto / 2))
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def ventana_reinas():
    ventana_reinas = tk.Toplevel()
    ventana_reinas.title("9 Reinas")
    ventana_reinas.configure(bg="#f0f8ff")
    centrar_ventana(ventana_reinas, 400, 300)

    tk.Label(ventana_reinas, text="Seleccione metodo para 9 Reinas", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=15)

    def ejecutar_tabu():
        messagebox.showinfo("9 Reinas - Busqueda Tabu", "Ejecutando Busqueda Tabu...")

    def ejecutar_recocido():
        messagebox.showinfo("9 Reinas - Recocido Simulado", "Ejecutando Recocido Simulado...")

    def ejecutar_genetico():
        messagebox.showinfo("9 Reinas - Algoritmo Genetico", "Ejecutando Algoritmo Genetico...")

    tk.Button(ventana_reinas, text="Busqueda Tabu", command=ejecutar_tabu, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Recocido Simulado", command=ejecutar_recocido, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Algoritmos Geneticos", command=ejecutar_genetico, width=25).pack(pady=5)
    tk.Button(ventana_reinas, text="Cerrar", command=ventana_reinas.destroy, width=25, bg="#ff6666").pack(pady=20)

def ventana_tsp():
    ventana_tsp = tk.Toplevel()
    ventana_tsp.title("Agente Viajero (TSP)")
    ventana_tsp.configure(bg="#f0fff0")
    centrar_ventana(ventana_tsp, 400, 250)

    tk.Label(ventana_tsp, text="Seleccione metodo para TSP", font=("Arial", 14, "bold"), bg="#f0fff0").pack(pady=15)

    def ejecutar_tabu():
        messagebox.showinfo("TSP - Busqueda Tabu", "Ejecutando Busqueda Tabu...")

    def ejecutar_recocido():
        messagebox.showinfo("TSP - Recocido Simulado", "Ejecutando Recocido Simulado...")

    tk.Button(ventana_tsp, text="Busqueda Tabu", command=ejecutar_tabu, width=25).pack(pady=5)
    tk.Button(ventana_tsp, text="Recocido Simulado", command=ejecutar_recocido, width=25).pack(pady=5)
    tk.Button(ventana_tsp, text="Cerrar", command=ventana_tsp.destroy, width=25, bg="#ff6666").pack(pady=20)

def ventana_funcion():
    ventana_funcion = tk.Toplevel()
    ventana_funcion.title("Optimizacion de f(x)")
    ventana_funcion.configure(bg="#fff0f5")
    centrar_ventana(ventana_funcion, 400, 250)

    tk.Label(ventana_funcion, text="Seleccione metodo para f(x)", font=("Arial", 14, "bold"), bg="#fff0f5").pack(pady=15)

    def ejecutar_busqueda_local():
        messagebox.showinfo("Optimizacion - Busqueda Local", "Ejecutando Busqueda Local...")

    def ejecutar_genetico():
        messagebox.showinfo("Optimizacion - Algoritmo Genetico", "Ejecutando Algoritmo Genetico...")

    tk.Button(ventana_funcion, text="Busqueda Local", command=ejecutar_busqueda_local, width=25).pack(pady=5)
    tk.Button(ventana_funcion, text="Algoritmo Genetico", command=ejecutar_genetico, width=25).pack(pady=5)
    tk.Button(ventana_funcion, text="Cerrar", command=ventana_funcion.destroy, width=25, bg="#ff6666").pack(pady=20)

# ventana principal
ventana = tk.Tk()
ventana.title("Proyecto IA - Menu Principal")
ventana.configure(bg="#e6f2ff")
centrar_ventana(ventana, 450, 350)

tk.Label(ventana, text="MENU PRINCIPAL", font=("Arial", 18, "bold"), bg="#e6f2ff").pack(pady=20)

tk.Button(ventana, text="1. Problema de las 9 Reinas", font=("Arial", 14), command=ventana_reinas, width=35).pack(pady=10)
tk.Button(ventana, text="2. Problema del Agente Viajero (TSP)", font=("Arial", 14), command=ventana_tsp, width=35).pack(pady=10)
tk.Button(ventana, text="3. Optimizacion de f(x)", font=("Arial", 14), command=ventana_funcion, width=35).pack(pady=10)
tk.Button(ventana, text="Salir", font=("Arial", 14), command=ventana.destroy, width=35, bg="#ff9999").pack(pady=15)

ventana.mainloop()