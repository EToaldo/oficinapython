def soma(list):
    soma = 0
    for i in range(len(list)):
        soma = soma + list[i]
    print(f"A soma das compras é:{soma}\n")

lista = []

while True:
    Valor = int(input("Escreva o valor da compra:\n"))
    if Valor >= 0:
        lista.append(Valor)
    else:
        break

print(f"Os valores da lista são :{lista}\n")

soma(lista)
