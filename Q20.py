#Escreva um programa que use uma pilha para converter um número binário para hexadecimal.

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

def bin_para_hexa(num_binario):
    p = Pilha()
    while num_binario != 0:
        resto = num_binario % 16
        p.inserir(resto)
        num_binario //= 16
    
    num_hexadecimal = ''
    while not p.is_empty():
        digito = p.remover()
        if digito < 10:
            num_hexadecimal += str(digito)
        else:
            num_hexadecimal += chr(ord('A') + digito - 10)
    
    return num_hexadecimal

num_binario = int(input('Digite um número binário: '), 2)
print(f'O número binário {num_binario} em hexadecimal é {bin_para_hexa(num_binario)}')