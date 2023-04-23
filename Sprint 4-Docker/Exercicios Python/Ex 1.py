'''Ex 1 - Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.'''

with open('numeros.txt', 'r') as f:
    numeros = [int(x.strip()) for x in f.readlines()]
pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)
cinco_maiores_pares = pares[:5]
soma = sum(cinco_maiores_pares)

print("Cinco maiores pares: ", cinco_maiores_pares)
print("Soma dos cinco maiores pares: ", soma)