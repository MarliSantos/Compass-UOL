# O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',', 5)
        resultado.append(palavras[:])

frequencia = []
nfrequencia = 0
nomefrequente = 0
for coluna in resultado[1::]:
    frequencia.append(coluna[4])
    nomefrequente = max(frequencia, key=frequencia.count)
    if coluna[4] == nomefrequente:
        nfrequencia += 1

with open ('etapa 4.txt', 'w', encoding='utf-8') as text:
    text.write('O nome dos filmes mais frequentes e sua respectiva frequencia:')
    text.write('\nO nome do filme mais frequente é {} e sua frequência é {}.'.format(nomefrequente, nfrequencia))
    