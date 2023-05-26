#1. Indicar cuál es el menor de tres enteros solicitados al usuario

""" print("Vamos a averiguar el numero menor de los 3 que vas a insertar")

n1 = input('Inserta un numero: ')
n2 = input('Inserta el segundo numero: ')
n3 = input('Inserta el tercer numero: ')
if (n1 < n2 and n1<n3):
    print ("El menor de los tres números es el: " + n1)
if (n2 < n1 and n2<n3):
    print ("El menor de los tres números es el: " + n2)
if (n3 < n1 and n3 < n2):
    print("El menor de los tres números es el: " + n3) """

#2. Dispones de frase y una letra, solicitados al usuario y debes mostrar la cantidad de veces que aparece la letra en la frase.

""" frase = input("Escribe una frase: ")
letra = input("Ahora introduce una letra: ")
cont = 0
# frase = "Hola que tal"
# letra = "a"
# l está solo en el for, es local
for l in frase:
    if l == letra:
        cont +=1
print("La letra " + letra + " se encuentra repetida "+ str(cont) + " veces") """

#3. Suma o resta dos números reales solicita la información al usuario

"""a = int(input("Introduce un numero: "))
b = int(input("Introduce otro numero: "))

suma = str(a+b)

print("La suma de los dos numeros es: " + suma)"""

#4. Permite validar a un usuario con 3 intentos y los datos de validación correctos almacenados en dos constantes predefinidas.

usuario = "Sara"
contraseña = "mayo"

a = input("Introduce usuario: ")
b = input("introduce contraseña: ")

if a == usuario and b == contraseña:
    print("Es correcto")

elif a != usuario or b != contraseña

#5. Crea una variable que sea una letra, si es una a muestra el número 7, si es una b, el 9, si es una c el 101 y si no es ninguno de los tres, indica que se han equivocado de letra

"""var = input("Adivina la letra: ")
if var == "a":
    num = 7
    print("Es el numero: " + str(num))
elif var == "b":
    num = 9
    print("Es el numero: " + str(num))
elif var == "c":
    num = 101
    print("Es el numero: " + str(num))
else:
    print("Te has equivocado de letra")"""


#6. Dispones de tres números enteros H, M, S correspondientes a hora, minutos y segundos respectivamente, debes comprobar si se trata de una hora válida.

"""H = int(input("Añade una hora: "))
M = int(input("Añade los minutos: "))
S = int(input("Añade los segundos: "))

if 00 <= H <= 24 and 00 <= M <= 60 and 00 <= S <= 60:
    print("Es una hora válida: "+ str(H) + " horas, " + str(M) + " minutos y "+ str(S) + " segundos")
else:
    print("No es un formato de horas posible")"""


#7. Solicita al usuario dos fechas del mismo año e indica la cantidad de días que hay entre ellas



#Opcionales:

#8. Añade el año al ejercicio 7, siempre por encima del 2000 e indica la diferencia en semanas y días que hay entre las dos fechas y cuál es anterior y posterior.


