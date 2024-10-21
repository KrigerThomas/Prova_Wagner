#Na prova, apesar de eu ter colocado os intervalos corretos, era possível reescrever o codigo como segue abaixo.

peso = float(input("Informe o peso em KG: "))
Altura = float(input("Informe a altura em metros: "))
imc = peso / (Altura * Altura)

print(imc)
if imc < 17:
    print("Muito abaixo do peso.")
elif imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau 1")
elif imc < 40:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")
