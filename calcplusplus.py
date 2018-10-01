#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if __name__ == "__main__":
    mical = calcoohija.CalculadoraHija()

    with open('documento.csv', 'r') as File:
        reader = csv.reader(File)
        for line in reader:
            operacion = line[0]  # escogerá las operaciones
            operando_n = line[1:]  # Te da la lista de operando
            final = int(operando_n[0])  # primer operando

            if operacion == "suma":  # si el primer elemento es "suma"
                num = 0
                for elemento in operando_n:  # desde el primero va sumando
                    num = mical.plus(num, int(elemento))
                print("El resultado de la suma es:", num)

            elif operacion == "resta":  # si el segundo elemento es "resta"
                num = final
                for elemento in operando_n[1:]:	  # desde el primero va restando
                    num = mical.minus(num, int(elemento))
                print("El resultado de la resta es:", num)

            elif operacion == "multiplica":
                num = 1
                for elemento in operando_n:  # va multiplicando
                    num = mical.multiplica(num, int(elemento))
                print("El resultado de la multiplicación es:", num)

            elif operacion == "divide":  # si el primer elemento es "divide"
                try:
                    num = final
                    for elemento in operando_n[1:]:  # va dividiendo en orden
                        num = mical.divide(num, int(elemento))
                    print("El resultado de la división es:", num)
                except ZeroDivisionError:
                        sys.exit("Division by zero is not allowed")
            else:
                sys.exit('Se ha confundido, ingrese de nuevo')
