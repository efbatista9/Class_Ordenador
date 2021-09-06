import random
import time


class Ordenador:

    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i + 1, fim):
                # encontrou um elemento menor...
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j               # ...substitui.

            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def bolha(self, lista):

        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]


class ContaTempos:

    def lista_aleatoria(self, n):  # n = número de elementos da lista
        from random import randrange
        # lista com n elementos, todos sendo zero
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)  # inteiros entre 0 e 999
        return lista

    def compara(self, n):

        lista1 = self.lista_aleatoria(n)
        lista2 = lista1

        o = Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou", depois - antes, "segundos")

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou", depois - antes, "segundos")
