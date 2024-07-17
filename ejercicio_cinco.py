"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def datos_personales_alumno(datos):
    keys = ["nombre", "apellido", "edad", "programa_estudio", "semestre"]
    return {keys[i]: datos[i] for i in range(len(keys))}

# Ejemplo de uso
datos_alumno = ("alex", "flores", "28", "APSTI", "III")
salida = datos_personales_alumno(datos_alumno)
print(salida) 