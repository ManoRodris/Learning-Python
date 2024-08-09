#mkmsjag tsjusk jagfalwjga kwflavg hjsuspn - 18


print("======== Cifra de césar ========")
cripto = input("Informe se vai encriptar ou decriptar uma mensagem: (e/d)\n").lower().strip()
while cripto != "d" and cripto != "e":
    print("Resposta invalida, tente novamente")
    cripto = input("Informe se vai encriptar ou decriptar uma mensagem: (e/d)\n").lower().strip()

mensagem = input("Informe a mensagem a ser trabalhada:\n").lower().strip()

cripto_cifra = int(input("Informe o numero da cifra: (ate 26)\n"))
while (cripto_cifra <= 0) or (cripto_cifra > 26):
    print("Numero invalido, tente novamente")
    cripto_cifra = int(input("Informe o numero da cifra: (ate 26)\n"))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

nova_mensagem = ""

if cripto == "d":
    for char in mensagem:
        if char in alfabeto:
            index = alfabeto.index(char)
            nova_index = (index - cripto_cifra) % 26
            nova_mensagem += alfabeto[nova_index]
        else:
            nova_mensagem += char

if cripto == "e":
    for char in mensagem:
        if char in alfabeto:
            index = alfabeto.index(char)
            nova_index = (index + cripto_cifra) % 26
            nova_mensagem += alfabeto[nova_index]
        else:
            nova_mensagem += char

print("Mensagem final: " + nova_mensagem)
        







