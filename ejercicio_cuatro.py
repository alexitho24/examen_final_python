"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""


registros_alumnos = {
    1: {'nombre': 'Juan', 'edad': 18, 'curso': 'Matemáticas'},
    2: {'nombre': 'María', 'edad': 20, 'curso': 'Historia'}
}
def imprimir_registros():
    for key, value in registros_alumnos.items():
        print(f"Registro {key}: {value}")
def editar_registro(registro, campo, nuevo_valor):
    if registro in registros_alumnos:
        registros_alumnos[registro][campo] = nuevo_valor
        print(f"El campo '{campo}' del registro {registro} ha sido actualizado.")
    else:
        print(f"El registro {registro} no existe.")
imprimir_registros()
editar_registro(1, 'edad', 19)
imprimir_registros()