#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def plus(self, op1, op2):  # es una funcion dentro de la clase, un metodo
        return op1 + op2

    def minus(self, op1, op2):  # es una funcion dentro de la clase, un metodo
        return op1 - op2


class CalculadoraHija(Calculadora):
    def multiplica(self, op1, op2):  # es una funcion dentro de la clase
        return op1 * op2

    def divide(self, op1, op2):  # es una funcion dentro de la clase
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")  # cuando op2 es cero


mical = CalculadoraHija()  # he creado un objeto CalculadoraHija


if __name__ == "__main__":
    try:
        digito1 = int(sys.argv[1])
        digito2 = int(sys.argv[3])

    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = mical.plus(digito1, digito2)
    elif sys.argv[2] == "resta":
        result = mical.minus(digito1, digito2)
    elif sys.argv[2] == "multiplica":
        result = mical.multiplica(digito1, digito2)
    elif sys.argv[2] == "divide":
        result = mical.divide(digito1, digito2)
    else:
        sys.exit('La operación hará: sumar, restar, multiplicar o dividir')

    print("El resultado es", result)
