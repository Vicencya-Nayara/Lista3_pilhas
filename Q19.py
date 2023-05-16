#Escreva um programa que use uma pilha para converter um número binário para octal.

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
    
def bin_para_octal(binario):
    p = Pilha()
    while binario != 0:
        resto = binario % 8
        p.inserir(resto)
        binario //= 8
    
    numero_octal = ''
    while not p.is_empty():
        numero_octal += str(p.remover())
    
    return numero_octal

num_bin_str = input('Digite um número binário: ')
num_bin = int(num_bin_str, 2)  # Converte a string para um número binário
print(f"O número binário {num_bin_str} em octal é {bin_para_octal(num_bin)}")
