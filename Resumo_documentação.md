# IF/Else

if — testa uma condição; se for verdadeira, executa o bloco.
elif — testa uma condição alternativa (pode haver zero ou mais).
else — executado quando nenhuma condição anterior foi verdadeira (é opcional).

A palavra-chave elif é uma abreviação de "else if" e serve para evitar indentação excessiva. 
Uma cadeia if … elif … elif … substitui os comandos switch ou case de outras linguagens. 

## Exemplo:
x = int(input("Insira um número inteiro: "))

if x < 0:
    print("Negativo")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Um")
else:
    print("Maior que um")
