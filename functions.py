recorridos = {
    'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
    'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
    'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
    'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
    'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True],
}

venta = {
    'R001': [7990, 20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    'R006': [4990, 12],
}

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción : \n"))
            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Opción no válida")
        except:
            print("Valor debe ser numérico")

def _validar_string(palabra):
    if len(palabra) > 0:
        return True
    else:
        return False

def _validar_numero(numero):
    if numero > 0:
        return True
    else:
        return False

def validar_min_max(p_min, p_max):
    if _validar_numero(p_min) and _validar_numero(p_max):
        if p_min <= p_max:
            return True
        else:
            return False
    else:
        print("Valor debe ser numérico")

def asientos_origen(origen):
    if _validar_string(origen):
        asientos_disponibles = 0
        encontrado = False
        for a in recorridos:
            ciudad_origen = recorridos[a][0]
            if ciudad_origen.title() == origen.title():
                asientos = venta[a][1]
                asientos_disponibles = asientos_disponibles + asientos
                encontrado = True
        
        if encontrado:
            print(f"Los asientos disponibles son {asientos_disponibles}")
        else:
            print("No se ha encontrado la ciudad de origen")
    else:
        print("La ciudad de origen no debe venir vacia")

def busqueda_precio(p_min, p_max):
    lista_busqueda = []
    for p in venta:
        precio_actual = venta[p][0]
        cupos_actuales = venta[p][1]
        if precio_actual >= p_min and precio_actual <= p_max and cupos_actuales > 0:
            origen = recorridos[p][0]
            destino = recorridos[p][1]
            texto_guardar = f"{origen}--{destino}--{p}"
            lista_busqueda.append(texto_guardar)

    if len(lista_busqueda) > 0:
        lista_busqueda.sort()
        print(f"Los recorridos encontrados son: {lista_busqueda}")
    else:
        print("No hay recorridos en ese rango de precios.")

def buscar_codigo(codigo):
    if _validar_string(codigo):
        if codigo in venta:
            return True
        else:
            return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        if _validar_numero(nuevo_precio):
            venta[codigo][0] = nuevo_precio
            return True
        else:
            print("Nuevo precio debe ser mayor a 0")
            return False
    else:
        return False

def eliminar_recorrido(codigo):
    if buscar_codigo(codigo):
        if codigo in recorridos:
            del recorridos[codigo]
            del venta[codigo]
            return True
        else:
            return False

def validar_codigo(codigo):
    if _validar_string(codigo):
        if codigo not in venta:
            return True
        else:
            return False
    else:
        return False

def validar_origen(origen):
    if _validar_string(origen):
        return True
    else:
        return False

def validar_destino(destino):
    if _validar_string(destino):
        return True
    else:
        return False

def validar_distancia(distancia):
    if _validar_numero(distancia):
        return True
    else:
        return False

def validar_tipo_bus(tipo_bus):
    if tipo_bus == "Normal" or tipo_bus == "Semi-cama" or tipo_bus == "Cama":
        return True
    else:
        return False

def validar_servicio(servicio):
    if servicio == "Dia" or servicio == "Noche":
        return True
    else:
        return False

def validar_wifi(wifi):
    if wifi == "s" or wifi == "n":
        return True
    else:
        return False

def traducir_booleano(respuesta):
    if respuesta == "s":
        return True
    else:
        return False

def validar_precio(precio):
    if _validar_numero(precio):
        return True
    else:
        return False

def validar_asientos(asientos):
    if asientos >= 0:
        return True
    else:
        return False

def agregar_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio, wifi, precio, asientos):
    if codigo in recorridos:
        return False
    else:
        recorridos[codigo] = [origen, destino, distancia, tipo_bus, servicio, wifi]
        venta[codigo] = [precio, asientos]
        return True