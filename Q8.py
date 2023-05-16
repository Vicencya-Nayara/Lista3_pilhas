#Escreva um programa que use uma pilha para converter um número decimal para hexadecimal.

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
    
    def topo(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._topo.valor

def converter_dec_hex(n):
    p = Pilha()
    while n > 0:
        r = n % 16
        if r < 10:
            p.inserir(str(r))
        else:
            p.inserir(chr(ord('A') + r - 10))
        n = n // 16

    return p

n = int(input('Digite um número decimal: '))
r = converter_dec_hex(n)
print('Número em hexadecimal: ', end='')

while not r.is_empty():
    print(r.remover(), end='')

