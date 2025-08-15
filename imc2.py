peso =float(input("Digite seu peso: "))
altura =float(input("Digite sua altura: "))

imc = peso /(altura * altura)
print(f"Seu peso è {peso} e sua {altura} portanto o seu Imc e {imc:.1f}")


if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("peso normal")
elif imc < 29.9:
    print("Sobrepeso" )
elif imc >= 30.0:
    print("cuidado com o peso")
elif imc < 34.9:
    print("obesidade Grau 1 ")
elif imc < 39.9:
    print("Obesidade Grau ll")
else:
    print("Obesidade grau ll (morbita)")