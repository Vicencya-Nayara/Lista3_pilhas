#Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras.

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
        return self.topo.valor
    
def inverter_palavras(frase):
    palavras = frase.split()
    p = Pilha()
    for palavra in palavras:
        p.inserir(palavra)
    nova_frase = ''
    while not p.is_empty():
        nova_frase += p.remover() + ' '
    return nova_frase.strip()

frase = input('Digite uma frase: ')
nova_frase = inverter_palavras(frase)
print(nova_frase)
