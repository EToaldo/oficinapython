def media(num):
    den = len(num)
    soma = sum(num)
    return (soma) / den

def notas(qt_provas):
    num =[]
    for i in range(qt_provas):
        b = int(input(f"Digite a nota da prova {i + 1}:\n"))
        num.append(b)
    return num

def exame(media):
    print(f"Sua média é:{media}")
    if media >= 7:
        print("Passou")
    else:
        print("Exame")
        nexame = 10-media
        print(f"Precisará tirar {nexame}") 



