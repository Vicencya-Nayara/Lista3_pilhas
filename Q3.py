#Escreva um programa que leia uma string contendo números e operações matemáticas (+, -, *, /) e 
#use uma pilha para calcular o resultado da expressão.

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
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(exp):
    p = Pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.inserir(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
            if caractere == '+':
                resultado = int(num1) + int(num2)
                p.inserir(str(resultado))
            elif caractere == '-':
                resultado = int(num1) - int(num2)
                p.inserir(str(resultado))
            elif caractere == '*':
                resultado = int(num1) * int(num2)
                p.inserir(str(resultado))
            elif caractere == '/':
                resultado = int(num1) / int(num2)
                p.inserir(str(resultado))
    return p.remover()

exp = input('Digite uma expressão matemática: ')
pos = infixa_para_posfixa(exp)
print(pos)

