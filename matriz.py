# Entre com 1 matriz de 3x3, exiba a soma de todas as linhas da matriz e de todas as colunas da matriz

linhas1 = []
linhas2 = []
linhas3 = []

print("Criando a matriz 3x3")

print("      1 2 3\n"
      "1 - { 0 0 0 }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na primeira linha... ")
for a in range(3):
    a = int(input("Digite o termo da linha: "))
    linhas1.append(a)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(linhas1[0]) + " " + str(linhas1[1]) + " " + str(linhas1[2]) + " }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na segunda linha... ")
for b in range(3):
    b = int(input("Digite o termo da linha: "))
    linhas2.append(b)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(linhas1[0]) + " " + str(linhas1[1]) + " " + str(linhas1[2]) + " }\n"
      "2 - { " + str(linhas2[0]) + " " + str(linhas2[1]) + " " + str(linhas2[2]) + " }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na terceira linha... ")
for c in range(3):
    c = int(input("Digite o termo da linha: "))
    linhas3.append(c)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(linhas1[0]) + " " + str(linhas1[1]) + " " + str(linhas1[2]) + " }\n"
      "2 - { " + str(linhas2[0]) + " " + str(linhas2[1]) + " " + str(linhas2[2]) + " }\n"
      "3 - { " + str(linhas3[0]) + " " + str(linhas3[1]) + " " + str(linhas3[2]) + " }\n"
      "            3x3")

somaLinhas1 = linhas1[0] + linhas1[1] + linhas1[2]
somaLinhas2 = linhas2[0] + linhas2[1] + linhas2[2]
somaLinhas3 = linhas3[0] + linhas3[1] + linhas3[2]

print("A soma dos termos da primeira linha é: " + str(somaLinhas1))
print("A soma dos termos da segunda linha é: " + str(somaLinhas2))
print("A soma dos termos da terceira linha é: " + str(somaLinhas3))

coluna1 = [linhas1[0], linhas2[0], linhas3[0]]
coluna2 = [linhas1[1], linhas2[1], linhas3[1]]
coluna3 = [linhas1[2], linhas2[2], linhas3[2]]

somaColunas1 = coluna1[0] + coluna1[1] + coluna1[2]
somaColunas2 = coluna2[0] + coluna2[1] + coluna2[2]
somaColunas3 = coluna3[0] + coluna3[1] + coluna3[2]

print("A soma dos termos da primeira coluna é: " + str(somaColunas1))
print("A soma dos termos da segunda coluna é: " + str(somaColunas2))
print("A soma dos termos da terceira coluna é: " + str(somaColunas3))