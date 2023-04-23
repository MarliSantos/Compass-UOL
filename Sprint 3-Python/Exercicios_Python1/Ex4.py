'''Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().'''

inicio = 1
fim = 100
  
for i in range(inicio, fim+1): 
  if i>1: 
    for n in range(2,i): 
        if(i % n==0): 
            break
    else: 
        print(i) 
