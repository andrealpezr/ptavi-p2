#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():
    def plus(self, op1, op2):  # es una funcion dentro de la clase, un metodo
        return op1 + op2

    def minus(self, op1, op2):  # es una funcion dentro de la clase, un metodo
        return op1 - op2


micalcu = Calculadora()     # he creado un objeto Calculadora
if __name__ == "__main__":
    try:
        oper1 = int(sys.argv[1])
        oper2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    if sys.argv[2] == "suma":
        result = micalcu.plus(oper1, oper2)
    elif sys.argv[2] == "resta":
        result = micalcu.minus(oper1, oper2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print("El resultado es", result)
