"""
Crear un diccionario de 5 registros de tiendas comerciales
y crear las siguientes funciones para el procesamiento de su informacion
1. funcion que me permita editar el nombre de una las tiendas comerciales
2. funcion que me permita actualizar el horario de atencion.
3. funcion que me permita eliminar una tienda comercial.
"""

tiendas_comerciales = {
    1: {'nombre': 'vara', 'horario': '9:00 - 18:00'},
    2: {'nombre': 'bigote', 'horario': '10:00 - 19:00'},
    3: {'nombre': 'que rico pincho', 'horario': '8:30 - 17:30'},
    4: {'nombre': 'donde tu tia', 'horario': '9:30 - 18:30'},
    5: {'nombre': 'hoy no fio mañana si', 'horario': '10:30 - 19:30'}
}
def editar_nombre_tienda(id_tienda, nuevo_nombre):
    if id_tienda in tiendas_comerciales:
        tiendas_comerciales[id_tienda]['nombre'] = nuevo_nombre
        print(f"Nombre de la tienda {id_tienda} actualizado a: {nuevo_nombre}")
    else:
        print(f"La tienda {id_tienda} no existe.")
def actualizar_horario_tienda(id_tienda, nuevo_horario):
    if id_tienda in tiendas_comerciales:
        tiendas_comerciales[id_tienda]['horario'] = nuevo_horario
        print(f"Horario de atención de la tienda {id_tienda} actualizado a: {nuevo_horario}")
    else:
        print(f"La tienda {id_tienda} no existe.")

def eliminar_tienda(id_tienda):
    if id_tienda in tiendas_comerciales:
        del tiendas_comerciales[id_tienda]
        print(f"Tienda {id_tienda} eliminada correctamente.")
    else:
        print(f"La tienda {id_tienda} no existe.")

print("Registros de las tiendas comerciales:")
for key, value in tiendas_comerciales.items():
    print(f"Tienda {key}: {value}")


editar_nombre_tienda(2, 'vigote')
actualizar_horario_tienda(4, '9:00 - 18:00')
eliminar_tienda(3)

print("\nRegistros de las tiendas comerciales después de las modificaciones:")
for key, value in tiendas_comerciales.items():
    print(f"Tienda {key}: {value}")
    