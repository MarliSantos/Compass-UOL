''' EX 1 - Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
Como saída, imprima o ano em que a pessoa completará 100 anos de idade.'''

nome = str(input('qual o seu nome?'))
idade = int(input('qual sua idade?'))
anoNasc = int(2023 - idade)
novoAno = int(anoNasc + 100)
print(novoAno)
