"""
crear una funcion que reciba como parametro una lista de numeros y me retorne dos valores el numero menor y el numero mayor en un diccionario
ejem:
entrada: [4,7,10,4,1,0]
salida : {menor:0,mayor:10}
"""
def encontrar_menor_mayor(lista):
    menor = lista[0]
    mayor = lista[0]
    
    for num in lista:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num
    
    diccionario = {'menor': menor, 'mayor': mayor}
    
    return diccionario

# Ejemplo de uso
entrada = [4, 7,8,12,14,20,100]
salida = encontrar_menor_mayor(entrada)
print(salida)