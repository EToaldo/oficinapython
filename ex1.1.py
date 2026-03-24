n1 = int(input("Digite a Primeira nota:\n"))
n2 = int(input("Digite a Segunda Nota:\n"))

media = (n1+n2)/2

print(f"A média é:{media}")

if media < 7:
    print("Exame")
else:
    print("Passou")