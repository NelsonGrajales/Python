while True:
    print("Operaciones con cadenas")
    print("=" * 25)
    print("1) Concatenar")
    print("2) Longitud de una cadena")
    print("3) Modificar cadena")
    print("4) Comparar cadenas")
    print("5) Salir")
    print("=" * 25)
    opcion = int(input("Ingrese una opción: "))

    if opcion in (1, 4):
        cadena_1 = input("Ingrese la primera cadena: ")
        cadena_2 = input("Ingrese la segunda cadena: ")
        if opcion == 1:
            print("=" * 40)
            print("La cadena concatenada es:")
            print(cadena_1 + cadena_2)
            print("La cadena concatenada con espacio es:")
            print(cadena_1 + " " + cadena_2)
            print("=" * 40)
        else:
            if cadena_1 == cadena_2:
                print("=" * 40)
                print("Las cadenas son iguales")
                print("=" * 40)
            else:
                print("=" * 40)
                print("Las cadenas no son iguales")
                print("=" * 40)

    elif opcion in (2, 3):
        cadena = input("Ingrese su cadena: ")
        if opcion == 2:
            print("=" * 40)
            print("La longitud de la cadena es:", len(cadena))
            print("=" * 40)
        else:
            segmento = input("Ingrese el nuevo segmento de la cadena: ")
            posicion = int(input("Ingrese la posición donde lo desea agregar: "))
            parte_1 = cadena[:posicion]
            parte_2 = cadena[posicion:]
            nueva_cadena = parte_1 + segmento + parte_2
            print("=" * 40)
            print("La nueva cadena es:", nueva_cadena)
            print("=" * 40)
    else:
        break