''' Ex12- Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json'''

import json

with open("person.json") as meu_json:
    person = json.load(meu_json)

print(person)
