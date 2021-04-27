# -*- coding: utf-8 -*-
import math
# Ejercicio 1
nom = str(input("Ingrese su nombre: "))
cal = str(input("Ingrese un calificativo: "))
print(nom, cal)
# Ejercicio 2
n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero: "))
print("La suma de los numeros es ", n1 + n2)
# Ejercicio 3
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero: "))
print("La suma de los numeros es ", num1 + num2)
print("La resta de los numeros es ", num1 - num2)
print("La multiplicacion de los numeros es ", num1 * num2)
print("La division de los numeros es ", num1 / num2)
print("El residuo de los numeros es ", num1 % num2)
# Ejercicio 4
numero = float(input("Ingrese un numero decimal: "))
parte_decimal, parte_entera = math.modf(numero)
print("La parte entera del numero es {} y la parte decimal es {}".format(parte_entera, parte_decimal))
# Tomado de: https://gist.github.com/parzibyte/916601de1242d2dec72316a2b505a949#file-separar-py
# Ejercicio 5
n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))
print("La nota final es: ", n1 * 0.15 + n2 * 0.20 + n3 * 0.15 + n4 * 0.30 + n5 * 0.20)
# Ejercicio 6
venta = int(input("Ingrese el valor de la venta: "))
iva = venta * 0.19
print("El valor de la venta es", venta, "El valor del IVA es", iva,
      "El valor de la venta mas IVA es", venta + (venta * 0.19))
# Ejercicio 7
r = float(input("Ingrese el valor del radio del círculo: "))
print("El area del círculo es", math.pi * (r**2), "El perimetro del círculo es", 2 * math.pi * r)
# Ejercicio 8
lado = float(input("Ingrese la longitud de un lado del hexágono"))
print("El valor del área del hexágono es:", (6 * (lado**2)) / (4 * (math.tan(math.pi / 6))))
# Ejercicio 9
num1 = int(input("Ingrese el valor el primer número: "))
num2 = int(input("Ingrese el valor el segundo número: "))
num3 = int(input("Ingrese el valor el tercer número: "))
print("El promedio de los tres números es:", (num1 + num2 + num3) / 3)
# Ejercicio 10
var1 = int(input("Ingrese un número entero: "))
var2 = int(input("Ingrese otro número: "))
print("Los valores iniciales son", var1, "y", var2)
int1 = var2
int2 = var1
print("Los valores intercambiados son", int1, "y", int2)
# Ejercicio 11
h = float(input("Ingrese la altura a la que será lanzado el objeto (en metros): "))
print("El tiempo de caída del objeto es de", math.sqrt((2 * h) / 10), "segundos")
# Ejercicio 14
m = float(input("Ingrese la masa del objeto (en kilogramos): "))
c = 299792458000
print("La energía del objeto es de", m * c**2, "Julios")
# Ejercicio 15
x1 = float(input("Digite la coordenada x1: "))
y1 = float(input("Digite la coordenada x2: "))
x2 = float(input("Digite la coordenada y1: "))
y2 = float(input("Digite la coordenada y2: "))
print("La distancia entre los puntos es de", math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
# Ejercicio 16
segundos = int(input("Ingrese los segundos a transformar: "))
print(segundos, "segundos equivalen a", segundos / 3600, "horas")
# Ejercicio 17
seg = int(input("Ingrese los segundos a transformar: "))
print(seg, "segundos equivalen a", seg / 60, "horas")
# Ejercicio 18
seg = int(input("Ingrese un tiempo en segundos: "))
hora = seg / 3600
segundos = seg % 3600
minutos = segundos / 60
segundos2 = seg % 60
print("la hora es:", int(hora), int(minutos), segundos2)
# Ejercicio 19
cant = int(input("Ingrese una cantidad de dinero: "))
luca = round(cant / 1000)
if luca < 1:
    print("No tiene billetes de mil")
else:
    print("Tiene", luca, "billetes de mil")
dosk = round(cant / 2000)
if dosk < 1:
    print("No tiene billetes de dos mil")
else:
    print("Tiene", dosk, "billetes de dos mil")
cincok = round(cant / 5000)
if cincok < 1:
    print("No tiene billetes de cinco mil")
else:
    print("Tiene", cincok, "billetes de cinco mil")
diezk = round(cant / 10000)
if diezk < 1:
    print("No tiene billetes de diez mil")
else:
    print("Tiene", diezk, "billetes de diez mil")
veintek = round(cant / 20000)
if veintek < 1:
    print("No tiene billetes de veinte mil")
else:
    print("Tiene", veintek, "billetes de veinte mil")
cincuentak = round(cant / 50000)
if cincuentak < 1:
    print("No tiene billetes de cincuenta mil")
else:
    print("Tiene", cincuentak, "billetes de cincuenta mil")
cienk = round(cant / 100000)
if cienk < 1:
    print("No tiene billetes de cien mil")
else:
    print("Tiene", cienk, "billetes de cien mil")
# Ejercicio 20


def invertir(numero):
    invertido = ""
    for n in numero:
        invertido = n + invertido
    return invertido


num = str(input("Ingrese un número entero a invertir: "))
print(invertir(num))
# Tomado de: https://gist.github.com/parzibyte/efc2ff376323451c975f77f7e85b649d#file-invertir_cadenas-py
# Ejercicio 21
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
# Ejercicio 22


def positivo_negativo(numero):
    negativo = "-"
    for n in numero:
        if n == negativo:
            return True


num = str(input("Ingrese un número positivo o negativo: "))
if positivo_negativo(num):
    print("El número es negativo.")
else:
    print("El número es positivo.")
# Ejercicio 23
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    if numero > 0:
        print("El número es par positivo.")
    else:
        print("El número es par negativo.")
else:
    if numero > 0:
        print("El número es impar positivo.")
    else:
        print("El número es impar negativo.")
# Ejercicio 24
venta = int(input("Ingrese el valor de la venta: "))
iva = venta * 0.19
descuento = venta * 0.05
if venta >= 150000:
    print("El valor de la venta mas iva y con descuento es de", (venta + iva) - descuento)
else:
    print("El valor de la venta mas iva es de", venta + iva)
# Ejercicio 25
numero = int(input("Ingrese un número: "))
if numero >= 10:
    print("La tercera parte del número es", numero * 3)
else:
    print("La cuarta parte del número es", numero * 4)
# Ejercicio 26
n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))
n4 = float(input("Ingrese la nota 4: "))
n5 = float(input("Ingrese la nota 5: "))
nfinal = (n1 * 0.15) + (n2 * 0.20) + (n3 * 0.15) + (n4 * 0.30) + (n5 * 0.20)
if nfinal < 2.0:
    print("No puede habilitar.")
if nfinal < 3.0:
    print("Reprobó.")
if nfinal >= 3.0:
    print("Aprobó.")
if nfinal > 4.5:
    print("Felicitaciones.")
# Ejercicio 27
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
print("El número mayor es", max(n1, n2))
# Ejercicio 28
numero = int(input("Ingrese un número entero: "))
print("El número ingresado equivale a", float(numero), "en decimal.")
# Ejercicio 29
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
print("El número mayor es", max(n1, n2, n3), "y el menor es", min(n1, n2, n3))
# Ejercicio 30
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
suma = n1 + n2
if suma > n3:
    print("La suma de los dos primeros números es mayor que el tercer número ingresado.")
else:
    print("La suma de los dos primeros números es menor que el tercer número ingresado.")
# Ejercicio 31
distancia = int(input("Ingrese la distancia a recorrer (en kilómetros): "))
dias = int(input("Ingrese los días de estancia: "))
pasaje = 5000 * distancia
if distancia > 1000 and dias > 7:
    print(pasaje - (pasaje * 0.15))
else:
    print("El precio del pasaje es", pasaje)
# Ejercicio 32
year = int(input("Ingrese un año: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
# tomado de: https://www.codigopiton.com/como-saber-si-un-ano-es-bisiesto-en-python/
# Ejercicio 34
user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
if user.startswith("admin") and password.startswith("12345678"):
    print("Inicio de sesión completado")
else:
    print("Inicio de sesión fallido (usuario o contraseña incorrectos).")
# Ejercicio 35
numero = int(input("Ingrese un número del 0 al 10: "))
if numero == 0:
    print("CERO")
elif numero == 1:
    print("UNO")
elif numero == 2:
    print("DOS")
elif numero == 3:
    print("TRES")
elif numero == 4:
    print("CUATRO")
elif numero == 5:
    print("CINCO")
elif numero == 6:
    print("SEIS")
elif numero == 7:
    print("SIETE")
elif numero == 8:
    print("OCHO")
elif numero == 9:
    print("NUEVE")
elif numero == 10:
    print("DIEZ")
else:
    print("ERROR (El número no está entre 0 y 10.")
# Ejercicio 36
num = int(input("Ingrese un número menor a 100000: "))
if num < 100000:
    print("El número", "(", num, ")", "tiene", len(str(num)), "dígitos")
else:
    print("ERROR (el número es mayor a 100000)")
# Ejercicio 37
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
if num2 > num1 and num3 > num2:
    print("Los números se incrementan.")
elif num2 < num1 and num3 < num2:
    print("Los números disminuyen.")
else:
    print("Los números no se incrementan ni se disminuyen")
# Ejercicio 38


def num_rango(num1, num2):
    return num1 and num2 in range(0, 6)


numero1 = int(input("Ingrese un número entre 0 y 5: "))
numero2 = int(input("Ingrese otro número entre 0 y 5: "))
print(num_rango(numero1, numero2))
# Ejercicio 39
dia = int(input("Ingrese el número de algún día de la semana (1 a 7): "))
if dia == 1:
    print("El 1 equivale al lunes.")
elif dia == 2:
    print("El 2 equivale al martes.")
elif dia == 3:
    print("El 3 equivale al miércoles.")
elif dia == 4:
    print("El 4 equivale al jueves.")
elif dia == 5:
    print("El 5 equivale al viernes.")
elif dia == 6:
    print("El 6 equivale al sábado.")
elif dia == 7:
    print("El 7 equivale al domingo.")
else:
    print("ERROR (ingresó un número que no está entre 1 y 7).")
# Ejercicio 40
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número: "))
num3 = int(input("Ingrese otro número: "))
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Al menos dos de los números son iguales.")
else:
    print("No hay números iguales.")
# Ejercicio 41
print("Los diez primeros números naturales son:")
for x in range(0, 11):
    print(x, "", end="")
# Ejercicio 42
print("Los diez primeros números naturales impares son:")
for x in range(0, 11):
    if x % 3 == 0:
        print(x, "", end="")
# Ejercicio 43
print("Los diez primeros números naturales pares son:")
for x in range(0, 11):
    if x % 2 == 0:
        print(x, "", end="")
# Ejercicio 45
n = int(input("Ingrese un número entero: "))
for x in range(1, n + 1):
    print(x, -x + 1 - 2)
# Ejercicio 46
n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número mayor: "))
for x in range(n, m + 1):
    if m > n:
        print(x, "", end="")
    else:
        print("El segundo número es menor que el primero, inténtelo de nuevo.")
# Ejercicio 47
n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número mayor: "))
print(sum(range(n, m + 1)))
# Ejercicio 48
n1 = int(input("Ingrese un número entero: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese otro número: "))
n4 = int(input("Ingrese otro número: "))
n5 = int(input("Ingrese otro número: "))
n6 = int(input("Ingrese otro número: "))
n7 = int(input("Ingrese otro número: "))
n8 = int(input("Ingrese otro número: "))
n9 = int(input("Ingrese otro número: "))
n10 = int(input("Ingrese otro número: "))
print("La suma de los números ingresados es:", n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)
print("El promedio de los números ingresados es:", (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10)
# Ejercicio 49
cont = 0
suma = 0
numero = 1
while numero != 0:
    numero = int(input("Ingrese un número entero (0 para calcular la suma y promedio: "))
    if numero != 0:
        suma += numero
        cont += 1
print("La suma de los números ingresados es:", suma)
print("El promedio de los números ingresados es: ", suma / cont)
# Ejercicio 51
numero = ()
while True:
    numero = int(input("Digite el valor permitido (0): "))
    if numero != 0:
        continue
    else:
        print(numero)
        break
