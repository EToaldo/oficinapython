def media(num):
    den = len(num)
    soma = sum(num)

    return (soma) / den

def notas(qt_provas):
    num =[]
    for i in range(qt_provas):
        b = float(input(f"Digite a nota da prova {i + 1}:\n"))
        num.append(b)
    return num

def exame(media):
    print(f"\nSua média é:{media:.2f}\n")
    if media >= 7:
        print("Passou\n")
    else:
        print("Exame\n")
        nexame = 10-media
        print(f"Precisará tirar: {nexame:.2f}\n") 
    return 0



