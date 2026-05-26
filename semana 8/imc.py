peso=int(input("digite o seu peso: "))
altura=float(input("digiteba sua altura"))
imc= peso/(altura*altura)
print("o seu IMC é: ", imc)

if imc<18.5:
    print("Abaixo do peso")
elif imc>=18.5 and imc<25:
    print("peso normal")
elif imc>=25 and imc<30:
    print("sobrepeso")
elif imc>=30 and imc<35:
    print("obesidade grau 1")
elif imc>=35 and imc<40:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")