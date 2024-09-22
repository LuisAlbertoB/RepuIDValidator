from tabla_transiciones import tabla

estado = 0

print("Ingrese una cadena a evaluar:")
cadena = input()

# Ciclo para recorrer la cadena
for character in cadena:
    if (estado, character) in tabla:
        estado = tabla[(estado, character)]
    else:
        estado = 'E'  # Estado de error
        break

# Verificación del estado final
if estado == 17:
    print("Cadena Válida")
else:
    print("Cadena No Válida")
