def func_valid_ip(entrada):
    pontos = []
    numerosTemp = []
    numeros = []

    for x in entrada:
        if x == "-":
            return False

    if entrada == "" or entrada[-1] == "." or entrada[0] == ".":
        return False
    else:
        for x in range(len(entrada)):
            if entrada[x] == '.':
                pontos.append(x)
        if len(pontos) != 3:
            return False
        else:
            if pontos[0] == pontos[1] - 1 or pontos[1] == pontos[2] - 1:
                return False

    pontos.append(len(entrada))
    num = ""
    comeco = 0

    for x in pontos:
        for a in range(comeco, x):
            num += entrada[a]
        numerosTemp.append(num)
        num = ""
        comeco = x + 1

    for x in numerosTemp:
        if len(x) > 3:
            return False
        try:
            numeros.append(int(x))
        except ValueError:
            return False

    for x in numeros:
        if x < 0 or x > 255:
            return False
    return True

def func_Valid_True(res):
    if res == False:
        print("Entrada Invalida \n")
    else:
        print("Entrada Valida \n")
