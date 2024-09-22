from tabla_transiciones import tabla

def evaluar_cadena(cadena):
    estado = 0
    for character in cadena:
        if (estado, character) in tabla:
            estado = tabla[(estado, character)]
        else:
            return False 
    return estado == 17

with open('test.txt', 'r') as archivo:
    cadenas = archivo.read().splitlines()

with open('report.txt', 'w') as report_file:
    for cadena in cadenas:
        if evaluar_cadena(cadena):
            report_file.write(f"{cadena}\n")
