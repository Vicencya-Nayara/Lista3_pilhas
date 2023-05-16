#Escreva um programa que leia uma string contendo caracteres (, ), {, }, [ e ], 
#e use uma pilha para verificar se os caracteres estão balanceados.

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
    
    def obter_topo(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self.topo.valor

def balancear_caracteres(sequencia):
    p = Pilha()
    abertos = "({["
    fechados = ")}]"

    for char in sequencia:
        if char in abertos:
            p.inserir(char)
        elif char in fechados:
            if p.is_empty():
                return False
            topo = p.remover()
            if abertos.index(topo) != fechados.index(char):
                return False
    
    return p.is_empty()

sequencia = input('Digite a sequencia de caracteres: ')

if balancear_caracteres(sequencia):
    print('Os caracteres estão balanceados')
else:
    print('Os caracteres não estão balanceados')