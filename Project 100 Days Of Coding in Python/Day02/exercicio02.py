peso = input("Peso: ")
altura = input("Altura: ")

imc = float(peso)/float(altura) ** 2
imc = int(imc)

print("IMC: " + str(imc))
