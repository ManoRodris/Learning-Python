peso = input("Peso: ")
altura = input("Altura: ")

imc = float(peso)/float(altura) ** 2

if imc < 16.9:
    print(f"Muito abaixo do peso - Seu IMC é {imc:.2f}")
elif imc >= 17 and imc <= 18.4:
    print(f"Abaixo do peso - Seu IMC é {imc:.2f}")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Peso normal - Seu IMC é {imc:.2f}")
elif imc >= 25 and imc <= 29.9:
    print(f"Acima do peso - Seu IMC é {imc:.2f}")
elif imc >= 30 and imc <= 34.9:
    print(f"Obesidade grau I - Seu IMC é {imc:.2f}")
elif imc >= 35 and imc <= 40:
    print(f"Obesidade grau II - Seu IMC é {imc:.2f}")
elif imc > 40:
    print(f"Obesidade grau III - Seu IMC é {imc:.2f}")

