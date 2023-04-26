"""Lizpy"""
import math


def analisaIMC(peso, altura):

    imc = peso / math.pow(altura, 2)

    print("IMC: %.2f" % imc)
    if imc < 18.5:
        ps = 18.5*pow(altura, 2) - peso
        print("Abaixo do peso!\nVoce precisa subir pelo menos =%.2fkg" % ps)
    elif imc <= 24.9:
        print("Peso ideal!")
    else:
        pb = peso - 24.9*pow(altura, 2)
        print("Acima do peso!\nVoce precisa baixar pelo menos =%.2fkg" % pb)


nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
analisaIMC(peso, altura)
