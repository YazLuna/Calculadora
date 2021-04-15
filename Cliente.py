#!/usr/bin/env python

import sys
sys.path.append("gen-py")

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from decimal import Decimal
from simple import Calculadora

transporte = TSocket.TSocket("localhost", 8080)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)
cliente = Calculadora.Client(protocolo)

transporte.open()
while True:
    print("\n[Cliente]")
    opcion = input("a)Sumar dos números \n b)Restar dos números \n c)Multiplicar dos números \n d)Dividir dos números \n e)Salir \nIngrese una letra:")
    try:
        if opcion == 'e':
            break
        else:
            if opcion == 'a':
                numeroA = input("Numero A: ")
                numeroB = input("Numero B: ")
                numeroA= Decimal(numeroA)
                numeroB= Decimal(numeroB)
                resultado = cliente.sumar(numeroA,numeroB)
                print(resultado)
            else:
                if opcion =='b':
                    numeroA = input("Numero A: ")
                    numeroB = input("Numero B: ")
                    numeroA= Decimal(numeroA)
                    numeroB= Decimal(numeroB)
                    resultado = cliente.restar(numeroA,numeroB)
                    print(resultado)
                else:
                    if opcion =='c':
                        numeroA = input("Numero A: ")
                        numeroB = input("Numero B: ")
                        numeroA= Decimal(numeroA)
                        numeroB= Decimal(numeroB)
                        resultado = cliente.multiplicar(numeroA,numeroB)
                        print(resultado)
                    else:
                        if opcion == 'd':
                            numeroA = input("Numero A: ")
                            numeroB = input("Numero B: ")
                            numeroA= Decimal(numeroA)
                            numeroB= Decimal(numeroB)
                            resultado = cliente.dividir(numeroA,numeroB)
                            print(resultado)
                        else:
                            print("Eliga una opcion correcta")
    except:
        print ("Ingrese números")
transporte.close()