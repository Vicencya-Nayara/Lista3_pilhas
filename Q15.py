#Escreva um programa que leia uma string contendo números e use uma pilha para converter a string em um número binário.

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

def converter_str_bin(string):
    p = Pilha()
    for caractere in string:
        if caractere.isdigit():
            p.inserir(int(caractere))

    resultado = 0
    multiplicador = 1
    while not p.is_empty():
        digito = p.remover()
        resultado += digito * multiplicador
        multiplicador *= 10

    return bin(resultado)[2:]

string = input('Digite uma string contendo números: ')
binario = converter_str_bin(string)
print('Número em binário:', binario)
