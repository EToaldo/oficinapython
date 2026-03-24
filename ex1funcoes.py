import funcoes as c

qt_provas = int(input("Quantidade de Provas:"))

num = c.notas(qt_provas)

m = c.media(num)

print(f"Sua média é: {m}")
if m >= 7:
    v = print("Passou")
else:
    print("Exame")
