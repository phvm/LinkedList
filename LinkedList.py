class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class Lista:

    def __init__(self):
        self.sentinela = Node(None)
        self.sentinela.proximo = self.sentinela
        self.sentinela.anterior = self.sentinela

    def removerDoFim(self):
        nodo = self.sentinela.anterior
        if nodo is self.sentinela:
            return "-1"
        temporario = nodo.valor
        nodo.anterior.proximo = nodo.proximo
        nodo.proximo.anterior = nodo.anterior
        nodo.proximo = None
        nodo.anterior = None
        return temporario

    def removerDoInicio(self):
        nodo = self.sentinela.proximo
        if nodo is self.sentinela:
            return "-1"
        temporario = nodo.valor
        nodo.anterior.proximo = nodo.proximo
        nodo.proximo.anterior = nodo.anterior
        nodo.proximo = None
        nodo.anterior = None
        return temporario

    def inserirNoComeco(self, valor):
        nodo = Node(valor)
        ponteiro = self.sentinela
        nodo.proximo = ponteiro.proximo
        nodo.anterior = ponteiro
        ponteiro.proximo.anterior = nodo
        ponteiro.proximo = nodo

    def inserirNoFim(self, valor):
        nodo = Node(valor)
        ponteiro = self.sentinela.anterior
        nodo.proximo = ponteiro.proximo
        nodo.anterior = ponteiro
        ponteiro.proximo.anterior = nodo
        ponteiro.proximo = nodo

    def inverter(self):
        atual = self.sentinela.proximo
        while atual.proximo is not self.sentinela:
            aux = atual.proximo
            atual.proximo = atual.anterior
            atual.anterior = aux
            atual = atual.anterior
        if atual.proximo is self.sentinela:
            aux = atual.proximo
            atual.proximo = atual.anterior
            atual.anterior = aux
        self.sentinela.proximo, self.sentinela.anterior = self.sentinela.anterior, self.sentinela.proximo


def main():
    lista = Lista()
    is_reverted = False
    n = int(input())
    for i in range(n):
        entradas = []
        entradas = input().split(" ")
        if entradas[0] == "3" and not is_reverted:
            is_reverted = True
        elif entradas[0] == "3" and is_reverted:
            is_reverted = False
        if not is_reverted:
            if entradas[0] == "1":
                lista.inserirNoComeco(int(entradas[1]))
            elif entradas[0] == "2":
                lista.inserirNoFim(int(entradas[1]))
            elif entradas[0] == "4":
                print(lista.removerDoInicio())
            elif entradas[0] == "5":
                print(lista.removerDoFim())
        else:
            if entradas[0] == "1":
                lista.inserirNoFim(int(entradas[1]))
            elif entradas[0] == "2":
                lista.inserirNoComeco(int(entradas[1]))
            elif entradas[0] == "4":
                print(lista.removerDoFim())
            elif entradas[0] == "5":
                print(lista.removerDoInicio())


if __name__ == '__main__':
    main()
