class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0

    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1

    def remover(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor

    def obter_topo(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._topo.valor

def ordenar_lista(lista):
    p = Pilha()
    for i in lista:
        p.inserir(i)
    lista_ordenada = []
    while not p.is_empty():
        lista_ordenada.insert(0, p.remover())
    return lista_ordenada

lista = [5, 3, 2, 4, 1]
lista.sort()
lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)
