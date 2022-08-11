# Pedro Gonçalves Classen.

# Trabalho 1 - Conjuntos.
# Programa que lê um arquivo de texto contendo a quantidade operações, quais operações, os conjuntos de cada operação e depois imprime os resultados no terminal.

# Split para ler os numeros como por inteiro inves de caractere por caractere.
# Adiciono numeros concatenando inves de lista porque achei mais facil de fazer o resultado aparecer conforme a especificação.
def uniao(c1, c2):
    c1 = c1.split(", ")
    c2 = c2.split(", ")
    resultado = ""
    for i in range(len(c1)):
        resultado += c1[i]+", "
    for i in range(len(c2)):
        if c1.count(c2[i]) == 0:
            resultado += c2[i]+", "
    resultado = resultado.strip(", ")
    return resultado

def intersecao(c1, c2):
    c1 = c1.split(", ")
    c2 = c2.split(", ")
    resultado = ""
    for i in range(len(c1)):
        if c2.count(c1[i]) == 1:
            resultado += c1[i]+", "
    resultado = resultado.strip(", ")
    return resultado

def diferenca(c1, c2):
    c1 = c1.split(", ")
    c2 = c2.split(", ")
    resultado = ""
    for i in range(len(c1)):
        if c2.count(c1[i]) == 0:
            resultado += c1[i]+", "
    resultado = resultado.strip(", ")
    return resultado

def prodCartesiano(c1, c2):
    c1 = c1.split(", ")
    c2 = c2.split(", ")
    resultado = ""
    for i in range(len(c1)):
        for j in range(len(c2)):
            resultado += "(" + c1[i] + "," + c2[j] + "); "
    resultado = resultado.strip("; ")
    return resultado

# Lê o arquivo e o organiza como uma matriz.
with open("teste3.txt") as file:
    linhas = file.readlines()
    matriz = []
    # Variável x serve como um ponto de partida para o segundo loop for.
    x = 1
    for i in range(int(linhas[0])):
        vetor = []
        for j in range(3):
            vetor.append(linhas[j+x].strip())
        x += 3
        matriz.append(vetor)

# Verifica qual operação deve ser realizada e imprime o resultado.
for i in range(len(matriz)):
    if matriz[i][0] == "U":
        matriz[i].append(uniao(matriz[i][1], matriz[i][2]))
        print("União: conjunto 1 {" + matriz[i][1] + "}, conjunto 2 {" + matriz[i][2] + "}. Resultado: {" + matriz[i][3] + "}")
    elif matriz[i][0] == "I":
        matriz[i].append(intersecao(matriz[i][1], matriz[i][2]))
        print("Interseção: conjunto 1 {" + matriz[i][1] + "}, conjunto 2 {" + matriz[i][2] + "}. Resultado: {" + matriz[i][3] + "}")
    elif matriz[i][0] == "D":
        matriz[i].append(diferenca(matriz[i][1], matriz[i][2]))
        print("Diferença: conjunto 1 {" + matriz[i][1] + "}, conjunto 2 {" + matriz[i][2] + "}. Resultado: {" + matriz[i][3] + "}")
    elif matriz[i][0] == "C":
        matriz[i].append(prodCartesiano(matriz[i][1], matriz[i][2]))
        print("Produto cartesiano: conjunto 1 {" + matriz[i][1] + "}, conjunto 2 {" + matriz[i][2] + "}. Resultado: {" + matriz[i][3] + "}")