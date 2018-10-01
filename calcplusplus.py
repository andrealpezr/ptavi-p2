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
            operacion = line[0] #escogerá las operaciones
            operando_n = line[1:]  # Te da la lista de operando
            
            if operacion == "suma":
                num = 0
                for suma in operando_n:
                    num = mical.plus(num, int(suma))
                print("El resultado de la suma es:", num )
            
            elif operacion == "resta":
                num = int(operando_n[0])
                for resta in operando_n:
                    num = mical.minus(num, int(resta))
                print("El resultado de la resta es:", num)
            
            else:
                print("jo")
            




























File.close()          