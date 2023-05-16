#Escreva um programa que use uma pilha para converter um número decimal para binário.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho
    
    def is_empty(self):
        return self.tamanho == 0
    
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1
    
    def remover(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor
    
    def topo(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._topo.valor


def converter_dec_bin(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 2
        n = n // 2
        p.inserir(r)

    return p

n = int(input('NÚMERO: '))
r = converter_dec_bin(n)

while not r.is_empty():
    print(r.remover())


