from turtle import *
from time import *
from random import *
def circulo():
    size = int(input("Que size: "))
    radio = int(input("Que radio: "))
    pensize(size)
    circle(radio)
    exitonclick()



def cuadrado():

    grande = int(input("Como de grande: "))
    size = int(input("Que size: "))
    pensize(size)
    for i in range(4):
        forward(grande)
        left(90)
    exitonclick()


def triangulo():
    size = int(input("Que size: "))
    color1 = input("color: ")
    pensize(size)
    color(color1)
    for i in range(3):
        left(120)
        forward(100)
    exitonclick()    

def barquito():
    size = int(input("Que size: "))
    a = input('color (en ingles): ')
    pensize(size)
    color(a)
    forward(50)
    left(180-45)
    forward(70)
    left(180-45)
    forward(50)
    b = input("Segundo color?: ")
    color(b)
    forward(30)
    left(90)
    forward(105)
    right(180-45)
    forward(45)
    right(45)
    forward(80)
    right(45)
    forward(45)
    right(180-45)   
    forward(45)
    exitonclick()

#-----------------------------------------------------------

def chatbot():
    print("Buenas!! Estas hablando con Rodri un ChatBot o un bot para conversar y dejar de aburrirse.\nTienes muchas opciones conmigo, te mostrare unas cuantas!!!")
    print("1- Una serie de preguntas para saber como estas! (El bot te pregunta a ti!)")
    print("2- Juego!")
    print("3- Tipo test para algun examen de matematicas")
    print("4- Calculadora!")
    print("5- Algo para cenar?")
    print("6- Cerrar")
    print("Dime que quieres!")

    choice = int(input("Ingresa el numero para hacer la accion: "))

    while choice != 6:
        if choice == 1:
            pregunta1 = input("Como estas: ")
            pregunta1.lower()
            if pregunta1 == 'bien':
                print("Me alegro!")
            elif pregunta1 == 'mal':
                print("Pues alegra esa cara jolin!")
            pregunta2 = input("Que has comido hoy: ")
            if pregunta2 != 'nada':
                print("Que bien!")
            else:
                print("Pues come algo no?")
            pregunta3 = input("Te gustan las patatas: ")
            pregunta3.lower()
            if pregunta3 == 'si':
                print("A mi tambien!")
            elif pregunta3 == 'no':
                print("Pues a mi me encantan!")
            choice = int(input("Ingresa el numero para hacer la accion: "))
        elif choice == 2:
            elegir = input("En que numero del 1 al 10 estoy pensando?\npuedes elegir que te de una pista con decirme (Dame la pista)\nSolo la puedes reclamar 1 vez y la tienes que pedir al principio: ")
            elegir.lower()
            if elegir == '5':
                print("Felicidades lo conseguiste acertar!")
                choice = int(input("Ingresa el numero para hacer la accion: "))
            elif elegir == 'dame la pista' or elegir == 'Dame la pista' or elegir == 'pista':
                print("Las pistas son:\n- Un numero impar\n- tiene un criterio de divisibilidad")
                while input("Dime el numero: ") != '5':
                    print("NONONO ESE NO ES")
                print("Muy bien lo acertaste")
                choice = int(input("Ingresa el numero para hacer la accion: "))
        elif choice == 3:
            dificultad = input("Que dificultad quieres?\n- Alta\n- Media\n- Baja\n- Salir\n")
            while dificultad != 'salir' and dificultad != 'Salir':
                if dificultad == 'Alta' or dificultad == 'alta':
                    preg1 = input("Dime el resultado X: 2x=6\nPosibles respuestas\n- A: 52\n- B: 3\n- C: 3/6\n")
                    while preg1 != 'B' and preg1 != 'C' and preg1 != 'b' and preg1 != 'c':
                        print('Incorrecto!')
                        preg1 = input("Dime el resultado X: 2x=6\nPosibles respuestas\n- A: 52\n- B: 3\n- C: 3\n")
                    print("Muy bien, siguiente pregunta!")
                    preg2 = input("Resultado de X: 2x-3=6+x\nPosibles respuestas:\n- A: 9\n- B: 7\n- C: 4\n")
                    while preg2 != 'a' and preg2 != 'A':
                        print("Incorrecto!")
                        preg2 = input("Resultado de X: 2x-3=6+x\nPosibles respuestas:\n- A: 9\n- B: 7\n- C: 4\n")
                    print("Pregunta superada!! Queda la ultima!")
                    preg3 = input("Resultado de X: 2(2x-3)=6+x\nPosibles respuestas\n- A: 12/3\n- B: 4\n- C: 7\n")
                    while preg3 != 'b' and preg3 != 'c' and preg3 != 'B' and preg3 != 'C':
                        print("Incorrecto!")
                        preg3 = input("Resultado de X: 2(2x-3)=6+x\nPosibles respuestas\n- A: 12/3\n- B: 4\n- C: 7\n")
                    print("Lo conseguiste MUY BIEN!")
                    dificultad = input("Que dificultad quieres?\n- Alta\n- Media\n- Baja\n- Salir\n")
                elif dificultad == 'Media' or dificultad == 'media':
                    preg1m = input("Dime el resultado de la siguiente operacion combinada: 3-6+7*8/9^2 = X\nPosibles respuestas:\n- A: 3\n- B: 9\n- C: 15/3\n")
                    while preg1m != 'c' and preg1m != 'C':
                        print("Incorrecto!!!")
                        preg1m = input("Dime el resultado de la siguiente operacion combinada: 3-6+7*8/9^2 = X\nPosibles respuestas:\n- A: 3\n- B: 9\n- C: 15/3\n")
                    print("Correcto! Siguiente pregunta")
                    preg2m = input("Si Juan tiene 9 cuartos de tierra y el agricultor le retira 2 tercios de tierra y luego una empresa le da\n 7 quintos de tierra, cuanta tierra tiene juan?\n Posibles respuestas:\n- A: 23/5\n- B: 33/21\n- C: 22/5\n")
                    while preg2m != 'c' and preg2m != 'C':
                        print("Incorrecto!!")
                        preg2m = input("Si Juan tiene 9 cuartos de tierra y el agricultor le retira 2 tercios de tierra y luego una empresa le da\n 7 quintos de tierra, cuanta tierra tiene juan?\n Posibles respuestas:\n- A: 23/5\n- B: 33/21\n- C: 22/5\n")
                    print("Felicidades lo adivinaste! ultima pregunta")
                    preg3m = input("Si tienes 3 tipos de lenguajes y estudias la mitad de cada 1, que te queda en total:\nPosibles respuestas:\n- A: Un derrame cerebral\n- B: Nada es correcto\n- C: 9 tercios\n")
                    while preg3m != 'C' and preg3m != 'c':
                        print("Incorrecto!!")
                        preg3m = input("Si tienes 3 tipos de lenguajes y estudias la mitad de cada 1, que te queda en total:\nPosibles respuestas:\n- A: Un derrame cerebral\n- B: Nada es correcto\n- C: 9 tercios\n")
                    print("Lo lograste!!")
                    dificultad = input("Que dificultad quieres?\n- Alta\n- Media\n- Baja\n- Salir\n")
                elif dificultad == 'Baja' or dificultad == 'baja':
                    preg1b = input("Cuanto es: 2*2+3-1*3\n- A: 4\n- B: 3\n- C: 9\n")
                    while preg1b != 'a' and preg1b != 'A':
                        print("Incorrecto!")
                        preg1b = input("Cuanto es: 2*2+3-1*3\n- A: 4\n- B: 3\n- C: 3\n")
                    print("Lo lograste!! Siguiente pregunta")
                    preg2b = input("Si tienes 4 manzanas y martin te da el triple y te comes una cuantas tienes?\n- A: 12\n- B: 11\n- C: 13\n")
                    while preg2b != 'B' and preg2b != 'b':
                        print("Incorrecto!!")
                        preg2b = input("Si tienes 4 manzanas y martin te da el triple y te comes una cuantas tienes?\n- A: 12\n- B: 11\n- C: 13\n")
                    print("Correcto!! Ultima pregunta!")
                    preg3b = input("Si la hija de juan, cumple 5 años, y su hermano tiene la mitad, en 3 años cuantos años tendra el hermano?\n- A: 5.5\n- B: 12\n- C: 9\n")
                    while preg3b != 'A' and preg3b != 'a':
                        print("Incorrecto!!")
                        preg3b = input("Si la hija de juan, cumple 5 años, y su hermano tiene la mitad, en 3 años cuantos años tendra el hermano?\n- A: 5.5\n- B: 12\n- C: 9\n")
                    dificultad = input("Que dificultad quieres?\n- Alta\n- Media\n- Baja\n- Salir\n")
            choice = int(input("Ingresa el numero para hacer la accion: "))
        elif choice == 4:
                preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                while preguntacalc != 'salir' and preguntacalc != 'Salir' and preguntacalc != '6':
                    numero1 = int(input("Indique el primer numero: "))
                    numero2 = int(input('Indique el segundo numero: '))
                    if preguntacalc == '1':
                        print("resultado:", numero1+numero2)
                        preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                    elif preguntacalc == '2':
                        print("resultado:", numero1-numero2)
                        preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                    elif preguntacalc == '3':
                        print("resultado:", numero1*numero2)
                        preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                    elif preguntacalc == '4':
                        print("resultado:", numero1/numero2)
                        preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                    elif preguntacalc == '5':
                        print("resultado:", numero1**numero2)
                        preguntacalc = input('que quieres hacer?\n1: Sumar\n2: Restar\n3: Multiplicar\n4: Dividir\n5: Pontencias\n6: Salir\n')
                    else:
                        print("Numero no reconocido")
                        numero1 = int(input("Indique el primer numero: "))
                        numero2 = int(input('Indique el segundo numero: '))
                choice = int(input("Ingresa el numero para hacer la accion: "))
        elif choice == 5:
                sd = input("Que te apetece cenar hoy, Dulce o salado? (nada para salir): ")
                while sd != 'nada' and sd != 'Nada':
                    if sd == 'salado' or sd == 'Salado':
                        print("Huevos con patatas fritas!!")
                        sd = input("Que te apetece cenar hoy, Dulce o salado? (nada para salir): ")
                    elif sd == 'Dulce' or sd == 'dulce':
                        print("Pues comete un donut!")
                        sd = input("Que te apetece cenar hoy, Dulce o salado? (nada para salir): ")
                    else:
                        sd = input("Que te apetece cenar hoy, Dulce o salado? (nada para salir): ")
                choice = int(input("Ingresa el numero para hacer la accion: "))
        elif choice == 6:
                break
        elif choice == 7:
            print("Has encontrado el sitio prohibido!! Aqui no puedes estar!")
            input("Enter para salir...")
            break
        else:
            print("No entiendo tu respueta")
            exit()

#--------------------------------------------------------------------------------------------------------------------------------------
pregunta = int(input("Que quieres hacer?: \n1: dibujar\n2: ChatBot\n3: >>>>>\n"))

if pregunta == 2:
    chatbot()

elif pregunta == 1:
    s = int(input("Que quieres hacer?\n1: Circulo\n2: Cuadrado\n3: Triangulo\n4: Barquito de papel\n"))
    if s == 1:
        circulo()
    elif s == 2:
        cuadrado()
    elif s == 3:
        triangulo()
    elif s == 4:
        barquito()


elif pregunta == 3:
    preg = int(input("Buenas, te voy a dar 2 opciones por selecionar la opcion 3\n1: Cronometro\n2: Generar equipos aleatorios\n"))
    if preg == 1:
        start = time()
        input("presiona enter para finalizar el contador...")
        end = time()
        print(round(end-start), "segs")
        input()
    elif preg == 1:
        eq1 = int(input("El número de miembros en el equipo 1:"))
        eq2 = int(input("El número de miembros en el equipo 2:"))
        print("Nadador", randint(1, eq1), "- Nadador", randint(1, eq2))


elif pregunta == 4:
    import webbrowser
    
    print("Cargando")
    for i in range(4):
        sleep(1)
        print('...')
    input("presiona enter...")
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(url)


