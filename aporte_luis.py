numero = input("Ingresa tu número de celular: ")

if numero.isdigit() and len(numero) == 9:
    print("Número de celular válido")
else:
    print("Número de celular no válido")
