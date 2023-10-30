# Se define la lista para almacenar las compras
compras = []


def agregar_compra():
    # Función para agregar una compra a la lista.
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    print("Compra agregada correctamente.")


def mostrar_compras():
    # Función para mostrar todas las compras.
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra:.2f}")


def mostrar_total():
    # Función para mostrar el total de gasto.
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")


def main():
    # Función principal del programa.
    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra()
        elif opcion == "2":
            mostrar_compras()
        elif opcion == "3":
            mostrar_total()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecuta la función main si el script se ejecuta como programa principal

if __name__ == "__main__":
    main()