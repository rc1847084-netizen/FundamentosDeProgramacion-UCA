# Fundamentos de Programacion
# Modulo 3
# Ruben Cuellar Lopez
'''Ejercicio 1: 
a) Si la calificacion es 9 o mas, diga "Excelente".
b) Si es menor que 0 o mayor que 10, diga "Calificacion invalida"
c) Si la calificacion es mayor que 8 pero menor que 9 que diga "buen trabajo" '''


calificacion = float(input("Escribe tu calificación: "))

if calificacion >10:
    print("Calificación Invalida")
elif calificacion <0:
        print("Calificación Invalida")
elif calificacion >=9:
     print("Excelente")
elif calificacion >8:
     print("Buen trabajo!!")
elif calificacion >=6:
     print("Aprobado")
elif calificacion <=5:
     print("Reprobado")

