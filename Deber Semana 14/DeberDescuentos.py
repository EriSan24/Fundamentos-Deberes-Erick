def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento y el total a pagar después del descuento.

    Parámetros:
    monto_total (float): Monto total de la compra.
    porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar (10% por defecto).

    Retorna:
    tuple: Monto del descuento y total a pagar después del descuento.
    """
    if monto_total < 0:
        return "Error: El monto total no puede ser negativo."

    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        return "Error: El porcentaje de descuento debe estar entre 0 y 100."

    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final


# Función para ejecutar pruebas con diferentes valores
def ejecutar_pruebas():
    print("Prueba 1: Monto 100 con descuento por defecto (10%)")
    descuento1, total1 = calcular_descuento(100)
    print(f"Descuento aplicado: ${descuento1:.2f}, Total a pagar: ${total1:.2f}\n")

    print("Prueba 2: Monto 250 con 20% de descuento")
    descuento2, total2 = calcular_descuento(250, 20)
    print(f"Descuento aplicado: ${descuento2:.2f}, Total a pagar: ${total2:.2f}\n")

    print("Prueba 3: Monto negativo (-50) [Debe mostrar error]")
    print(calcular_descuento(-50))

    print("\nPrueba 4: Descuento inválido (110%) [Debe mostrar error]")
    print(calcular_descuento(200, 110))


# Función para interacción con el usuario
def ejecutar_interactivo():
    try:
        monto = float(input("Ingrese el monto total de la compra: "))
        porcentaje = input("Ingrese el porcentaje de descuento (presione Enter para usar 10% por defecto): ")

        if porcentaje.strip() == "":
            descuento, total = calcular_descuento(monto)
        else:
            descuento, total = calcular_descuento(monto, float(porcentaje))

        print(f"\nResumen:")
        print(f"Monto total: ${monto:.2f}")
        print(f"Descuento aplicado: ${descuento:.2f}")
        print(f"Monto final a pagar: ${total:.2f}")

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


# Ejecutar pruebas automatizadas
ejecutar_pruebas()

# Ejecutar versión interactiva con el usuario
ejecutar_interactivo()
