from os import system

def calculadora_opciones()->str:
    """Muestra las opciones de la calculadora y retorna un input para elegir la opción

    Returns:
        str: retorna la opción elegida
    """
    print("   Calculadora -- opciones: ")
    if flag_primer_operando:
        print(f"a. Ingresar primer operando ---> {primer_operando}")
    else: 
        print("a. Ingresar primer operando")

    if flag_segundo_operando:
        print(f"b. Ingresa segundo operando ---> {segundo_operando}")
    else:
        print("b. Ingresar segundo operando")

    if flag_operacion:
        match operacion:
            case "1":
                eleccion = "Suma"
            case "2":
                eleccion = "Resta"
            case "3":
                eleccion = "Multiplicacion"
            case "4":
                eleccion = "Division"
            case "5":
                eleccion = "Factorial"
        print(f"c. Elegir operacion ---> {eleccion}")
    else: 
        print("c. Elegir operacion")

    print("d. Mostrar resultado")
    print("e. Salir")
    return input("Elija una opción: ")

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")

def operacion_opciones()->str:
    """Muestra las opciones de las operaciones y retorna la opción elegida

    Returns:
        str: retorna la opción elegida
    """
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. factorial")
    return input("Elija una opción: ")

def resultado(seleccion:str)->str:
    """En base a la operación elegida, se realizan las operaciones y se retorna el resultado

    Args:
        seleccion (str): La operación seleccionada

    Returns:
        str: El resultado de la operación seleccionada
    """
    match seleccion:
        case "1":
            cuenta = primer_operando + segundo_operando
        case "2": 
            cuenta = primer_operando - segundo_operando
        case "3":
            cuenta = primer_operando * segundo_operando
        case "4":
            if segundo_operando == 0:
                try:
                    primer_operando / segundo_operando
                except:
                    cuenta = print("No es posible dividir por cero :(")
            else:
                cuenta = primer_operando / segundo_operando
        case "5":
                factorial_1 = factorial(primer_operando)
                factorial_2 = factorial(segundo_operando)
                return print(f"el factorial del primer operando es {factorial_1} y el del segundo operando es {factorial_2}")
    return cuenta

def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
    


def signo(seleccion:str)->str:
    match seleccion:
        case "1":
            operacion = "+"
        case "2":
            operacion = "-"
        case "3":
             operacion = "*"
        case "4":
            operacion = "/"
        case "5":
            operacion = "!"
    return operacion

#------------------------------------------------------------

flag_primer_operando = False
flag_segundo_operando = False
flag_operacion = False
flag_resultado = False


while True:
    limpiar_pantalla()
    match calculadora_opciones():
        case "a":
            primer_operando = input("Ingrese el primer operando")
            while not primer_operando.isdigit():
                primer_operando = input("Debe ser un numero")
            primer_operando = int(primer_operando)
            caso_a = print(f"Ingresar primer operando: {primer_operando}")
            flag_primer_operando = True
        case "b":
            if flag_primer_operando:
                segundo_operando = input("Ingrese el segundo operando")
                while not segundo_operando.isdigit():
                    segundo_operando = input("Debe ser un numero")
                segundo_operando = int(segundo_operando)
                flag_segundo_operando = True
            else: 
                print("No puedes ingresar el segundo operando sin haber ingresado el primero")
            pausar()
        case "c":
            if flag_primer_operando and flag_segundo_operando:
                operacion = operacion_opciones()
                flag_operacion = True
            elif flag_primer_operando:
                print("No puedes elegir la operacion sin haber ingresado el segundo operando")
                pausar()
            else:
                print("No puedes elegir la operacion sin haber puesto el primer y segundo operando")
                pausar()
        case "d":
            if flag_primer_operando and flag_segundo_operando and flag_operacion:
                    print(f"El resultado entre {primer_operando} {signo(operacion)} {segundo_operando} es: {resultado(operacion)}")
            elif flag_primer_operando and flag_segundo_operando:
                print("Te falta pedir el operador para conseguir el resultado")
            elif flag_primer_operando:
                print("No puedes pedir el resultado sin haber puesto el segundo operando y el tipo de operacion")
            else: 
                print("Te faltan los pasos a, b y c")
            flag_primer_operando = False
            flag_segundo_operando = False
            flag_operacion = False
            pausar()
        case "e":
            continuar = input("Desea continuar? s/n: ")
            if continuar == "s":
                continue 
            elif continuar == "n":
                break
            while continuar != "s" and continuar != "n":
                continuar = input("Debe ser s/n: ")
            pausar()


print("Fin del programa")


