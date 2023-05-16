#Escreva um programa que use uma pilha para converter um número hexadecimal para decimal.

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

def converter_hex_dec(hexadecimal):
    p = Pilha()
    for caractere in hexadecimal:
        if caractere.isdigit():
            p.inserir(int(caractere))
        elif caractere.isalpha():
            valor = ord(caractere.upper()) - ord('A') + 10
            p.inserir(valor)

    resultado = 0
    multiplicador = 1
    while not p.is_empty():
        digito = p.remover()
        resultado += digito * multiplicador
        multiplicador *= 16

    return resultado

hexadecimal = input('Digite um número hexadecimal: ')
decimal = converter_hex_dec(hexadecimal)
print('Número em decimal:', decimal)
