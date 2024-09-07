lista_compras = []

while True:
    print("\nMenú de opciones:")
    print("1 - Agregar artículo")
    print("2 - Eliminar artículo")
    print("3 - Mostrar lista")
    print("4 - Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        articulo = input("Ingresa el nombre del artículo que desaes agregar: ")
        lista_compras.append(articulo)
        print(f"'{articulo}' El articículo ha sido agregado a la lista.")
    
    elif opcion == "2":
        articulo = input("Ingrese el nombre del artículo que deseas eliminar: ")
        if articulo in lista_compras:
            lista_compras.remove(articulo)
            print(f"'{articulo}'El artículo ha sido eliminado de la lista.")
        else:
            print(f"'{articulo}' no se encuentra en la lista.")
    
    elif opcion == "3":
        if lista_compras:
            print("\n Lista de compras:")
            for item in lista_compras:
                print(f"- {item}")
        else:
            print("NO hay artículos en la lista de compras")
    
    elif opcion == "4":
        print("...Saliendo del programa...")
        break
    
    else:
        print("La opción seleccionada no es valida, por favor elige una opción entre 1 y 4")
