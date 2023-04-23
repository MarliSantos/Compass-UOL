import hashlib
while True:
    string = input("Digite a string para mascarar: ")
    string_cod = hashlib.sha1(string.encode('utf-8'))
    print("O hash da string é: ", string_cod.hexdigest())