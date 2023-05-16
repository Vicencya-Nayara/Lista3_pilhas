#palíndromo (ou seja, se é igual quando lida de trás para frente).

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
    
def eh_palindromo(palavra):
    p = Pilha()
    tamanho = len(palavra)

    for i in range(0, tamanho // 2):
        p.inserir(palavra[i])

    for i in range((tamanho + 1) // 2, tamanho):
        if p.remover() != palavra[i]:
            return False

    return True

palavra = input('Digite uma palavra: ')

if eh_palindromo(palavra):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
