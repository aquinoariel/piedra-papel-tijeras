
edad = int(input("Por favor, ingrese su edad: "))

#if edad >= 18 and edad <= 30:
#    print("Podes entrar al bar")
#else:
#    print("Perdón, pero no podes entrar al bar")


permitido = True if edad >= 18 and edad <= 30 else False # Ternario

if permitido:
    print("Podes ingresar al bar")
else:
    print("No podes ingresar al bar")