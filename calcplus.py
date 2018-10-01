#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija


if __name__ == "__main__":

    lectura = open('documento.txt', 'r')  # ponemos modo lectura el fichero
    fichero = lectura.readlines()  # devuelve una lista a cada linea

    mical = calcoohija.CalculadoraHija()

    for elemento in fichero:
        separo_comas = elemento.split(',')  # separa la lista por comas
        operacion = separo_comas[0]  # accedemos al primer elemento de cada una
        operando1 = int(separo_comas[1])  # escoge el operando1 de cada linea
        operando_n = separo_comas[2:]  # desde el operando2 hasta el operandon

        if operacion == "suma":  # si el primer elemento es "suma"
            num = operando1
            for elemento in operando_n:  # desde el primero va sumando
                num = mical.plus(num, int(elemento))
            print("El resultado de la suma es:", num)

        elif operacion == "resta":  # si el segundo elemento es "resta"
            num = operando1
            for elemento in operando_n:	  # desde el primero va restando
                num = mical.minus(num, int(elemento))
            print("El resultado de la resta es:", num)

        elif operacion == "multiplica":  # si el tercer elemento "multiplica"
            num = operando1
            for elemento in operando_n:  # desde el primero va multiplicando
                num = mical.multiplica(num, int(elemento))
            print("El resultado de la multiplicación es:", num)

        elif operacion == "divide":  # si el primer elemento es "divide"
            try:
                num = operando1
                for elemento in operando_n:  # va dividiendo en orden
                    num = mical.divide(num, int(elemento))
                print("El resultado de la división es:", num)
            except ZeroDivisionError:
                    sys.exit("Division by zero is not allowed")
        else:
            sys.exit('Se ha confundido, ingrese de nuevo')

lectura.close  # al terminar la lectura cerramos el fichero
