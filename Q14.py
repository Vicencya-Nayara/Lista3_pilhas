#Escreva um programa que leia uma expressão matemática na forma de string e utilize uma pilha 
#para converter a expressão para a notação polonesa reversa.

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
    
def conversao_rpn(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    rpn= []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            rpn.append(caracter)
        elif caracter == '(':
            operadores.inserir(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                rpn.append(operadores.remover())
            operadores.remover()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                rpn.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        rpn.append(operadores.remover())
    return ''.join(rpn)



exp = input('Digite uma expressão matemática: ')
rpn = conversao_rpn(exp)
print('Expressão em RPN: ', rpn)