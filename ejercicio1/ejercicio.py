'''                                                                                                             
Defina una variable de cada tipo de primitivo
1 Concatena a la cadena las otras variables aplicando la conversion correcta para funcionar, guarda el resultado en una variable.  
'''
#Entero
numero = 2
#Flotante
flotante = 7.2
#Booleano
estudiante = True 
#Cadena
cadena = "str"

# Concatena 
Concatena = cadena + " " + str(numero) + " " + str(flotante)+ " " + str(estudiante)
print (Concatena)


'''
2 resultado Investiga sobre el limite de los enteros y los flotantes en python
'''
#los limites de un entero puede alamacenar todos los valores enteros. Este tipo de entero puede ser de cualquier tamaño. no hay limite.
#los limites de un flotantes se pueden representar como un punto y la parte decimal para decir 0.decimal 

'''
3 Aplica la formula de la suma  de los primeros n numeros pares (investigar) toman numero entero y almacenar el resultado en una variable
'''
n = 10
resultado = 0

for i in range  (2,n+1,2):
    resultado += i
print (resultado)

'''
 4 Imprimir los resultados de las tareas anteriores
'''
print(Concatena)
print("resultado")
print(resultado)
print("numero")
print(numero)
print("flotante")
print(flotante)
print("estudiante")
print(estudiante)
print("cadena")
print(cadena)
