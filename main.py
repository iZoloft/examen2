from functions import *

while True:
    print("====== MENÚ PRINCIPAL ======")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. salir")
    opcion = leer_opcion()
    if opcion == 1:
        origen = input("Ingrese ciudad de origen: \n").title().strip()
        asientos_origen(origen)
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: \n"))
                p_max = int(input("Ingrese precio máximo: \n"))
                if validar_min_max(p_min, p_max):
                    busqueda_precio(p_min, p_max)
                    break
                else:
                    print("Precio mínimo no puede ser mayor al precio máximo")
            except:
                print("Valor debe ser numérico")
    elif opcion == 3:
        while True:
            try:
                codigo = input("Ingrese código del recorrido: \n").strip().upper()
                nuevo_precio = int(input("Ingrese nuevo precio: \n"))
                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio Actualizado")
                else:
                    print("Código no existe")
                seguir = input("¿Desea actualizar otro precio (s/n)?: \n").strip().lower()
                if seguir == 'n':
                    break
            except:
                print("Valor debe ser numérico")
    elif opcion == 4:
        try:
            registro_valido = True
            if registro_valido == True:
                codigo = input("Ingrese código del recorrido: \n").strip().upper()
                if validar_codigo(codigo) == False:
                    print("El código no puede estar vacío.")
                    registro_valido = False
            if registro_valido == True:
                origen = input("Ingrese origen del recorrido: \n").strip().title()
                if validar_origen(origen) == False:
                    print("Origen no puede estar vacio")
                    registro_valido = False
            if registro_valido == True:
                destino = input("Ingrese destino del recorrido: \n").strip().title()
                if validar_destino(destino) == False:
                    print("Destino no puede estar vacio")
                    registro_valido = False
            if registro_valido == True:
                distancia = int(input("Ingrese distancia en km del recorrido: \n"))
                if validar_distancia(distancia) == False:
                    print("Distancia debe ser mayor a 0")
                    registro_valido = False
            if registro_valido == True:
                tipo_bus = input("Ingrese tipo de bus (normal, semi-cama, cama): \n").strip().title()
                if validar_tipo_bus(tipo_bus) == False:
                    print("Tipo de bus debe ser Normal, Semi-cama o Cama")
                    registro_valido = False
            if registro_valido == True:
                servicio = input("Ingrese servicio (dia / noche): \n").title().strip().replace("í", "i")
                if validar_servicio(servicio) == False:
                    print("Servicio debe ser Día o Noche")
                    registro_valido = False
            if registro_valido == True:
                wifi = input("Tiene WiFi (s/n): \n").strip().lower()
                if validar_wifi(wifi) == False:
                    print("Opción debe ser s o n")
                    registro_valido = False
                else:
                    wifi_bool = traducir_booleano(wifi)
            if registro_valido == True:
                precio = int(input("Ingrese precio: \n"))
                if validar_precio(precio) == False:
                    print("Precio debe ser mayor a 0")
                    registro_valido = False
            if registro_valido == True:
                asientos = int(input("Ingrese asientos: \n"))
                if validar_asientos(asientos) == False:
                    print("La cantidad de asientos debe ser mayor a 0")
                    registro_valido = False
            if registro_valido == True:
                if agregar_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio, wifi_bool, precio, asientos):
                    print("Recorrido Agregado")
                else:
                    print("Código del recorrido ya existe")
        except:
            print("Valor debe ser numérico")
    elif opcion == 5:
        codigo = input("Ingrese código del recorrido: \n").strip().upper()
        if eliminar_recorrido(codigo):
            print(f"Recorrido {codigo} eliminado")
        else:
            print("Recorrido no existe")
    else:
        print("Programa finalizado")
        break