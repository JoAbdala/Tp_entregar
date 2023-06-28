#Ejercio nº 1
num = int(input("Ingresa un número: "))
factorial = 1

if num > 0:
        print(f"El factorial de {num} es:")
        while num > 1:
            print(f"{num} * ", end="")
            factorial *= num
            num -= 1
        print("1 =", factorial)
else:
        print("No puedo sacar el factorial de 0")
# Ejercicio nº 2       
        
cont = 0
suma = 0

while cont < 5:
    valor = int(input("Ingrese un valor entero: "))
    suma += valor
    cont += 1

promedio = suma / 5

print("La suma de los valores es:", suma)
print("El promedio de los valores es:", promedio)


#Ejercicio nº3


num= 1
while num != 0:
    num = int(input("Ingrese un número (0 para salir): "))
    if num % 2 == 0:
        print("El número", num, "es par.")
    else:
        print("El número", num, "es impar.")


# Ejercicio nº4
import random


par = 0
impar = 0
multip_5_y_3 = 0
suma = 0
negat_y_multip_2 = 0


for i in range(10):
    valor = random.randint(-100, 100)  
    print(valor)  
    suma += valor 
    
    if valor % 2 == 0:
        par += 1
        if valor < 0 and valor % 2 == 0:
            negat_y_multip_2 += 1
    else:
        impar += 1

    
    match (valor % 5, valor % 3):
        case (0, 0):
            multip_5_y_3 += 1
    

promedio = suma / 10


print("Cantidad de valores pares:-->  ", par)
print("Cantidad de valores impares:--> ", impar)
print("Cantidad de valores múltiplos de 5 y 3:--> ", multip_5_y_3)
print("Suma total de los valores:--> ", suma)
print("Cantidad de valores negativos y múltiplos de 2:", negat_y_multip_2)
print("Promedio total:-->  ", promedio)
