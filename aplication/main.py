from tabla_transiciones import tabla
import ui as ui

# Automata###########################################
def Automata(cadena):                               #
    estado = 0                                      #
    for character in cadena:                        #
        if (estado, character) in tabla:            #
            estado = tabla[(estado, character)]     #
        else:                                       #
            return False  # qe                      #
    return estado == 17   # qf                      #
#####################################################

def procesar_archivo(archivo):
    with open(archivo, 'r') as f:
        cadenas = f.read().splitlines()
    
    cadenas_validas = []
    for cadena in cadenas:
        if Automata(cadena):
            cadenas_validas.append(cadena)
    
    if cadenas_validas:
        resultado = "\n".join(cadenas_validas)
    else:
        resultado = "No se encontraron cadenas válidas."
    
    # reporte
    with open("report.txt", "a") as report_file:
        for cadena in cadenas_validas:
            report_file.write(cadena + "\n")

    # imprimir
    mostrar_resultado_callback(resultado)

root, mostrar_resultado_callback = ui.crear_interfaz(procesar_archivo)

root.mainloop()
