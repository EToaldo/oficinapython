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



