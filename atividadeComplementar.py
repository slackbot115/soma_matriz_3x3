m1linhas1 = []
m1linhas2 = []
m1linhas3 = []

m2linhas1 = []
m2linhas2 = []
m2linhas3 = []

print("Criando a Matriz 1")

print("      1 2 3\n"
      "1 - { 0 0 0 }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na primeira linha... ")
for a in range(3):
    a = int(input("Digite o termo da linha 1: "))
    m1linhas1.append(a)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m1linhas1[0]) + " " + str(m1linhas1[1]) + " " + str(m1linhas1[2]) + " }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na segunda linha... ")
for b in range(3):
    b = int(input("Digite o termo da linha 2: "))
    m1linhas2.append(b)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m1linhas1[0]) + " " + str(m1linhas1[1]) + " " + str(m1linhas1[2]) + " }\n"
      "2 - { " + str(m1linhas2[0]) + " " + str(m1linhas2[1]) + " " + str(m1linhas2[2]) + " }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na terceira linha... ")
for c in range(3):
    c = int(input("Digite o termo da linha 3: "))
    m1linhas3.append(c)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m1linhas1[0]) + " " + str(m1linhas1[1]) + " " + str(m1linhas1[2]) + " }\n"
      "2 - { " + str(m1linhas2[0]) + " " + str(m1linhas2[1]) + " " + str(m1linhas2[2]) + " }\n"
      "3 - { " + str(m1linhas3[0]) + " " + str(m1linhas3[1]) + " " + str(m1linhas3[2]) + " }\n"
      "            3x3")

print("Criando a Matriz 2")

print("      1 2 3\n"
      "1 - { 0 0 0 }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na primeira linha... ")
for a in range(3):
    a = int(input("Digite o termo da linha 1: "))
    m2linhas1.append(a)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m2linhas1[0]) + " " + str(m2linhas1[1]) + " " + str(m2linhas1[2]) + " }\n"
      "2 - { 0 0 0 }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na segunda linha... ")
for b in range(3):
    b = int(input("Digite o termo da linha 2: "))
    m2linhas2.append(b)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m2linhas1[0]) + " " + str(m2linhas1[1]) + " " + str(m2linhas1[2]) + " }\n"
      "2 - { " + str(m2linhas2[0]) + " " + str(m2linhas2[1]) + " " + str(m2linhas2[2]) + " }\n"
      "3 - { 0 0 0 }\n"
      "            3x3")

print("Inserindo valores na terceira linha... ")
for c in range(3):
    c = int(input("Digite o termo da linha 3: "))
    m2linhas3.append(c)

print("A matriz agora esta assim: ")
print("      1 2 3\n"
      "1 - { " + str(m2linhas1[0]) + " " + str(m2linhas1[1]) + " " + str(m2linhas1[2]) + " }\n"
      "2 - { " + str(m2linhas2[0]) + " " + str(m2linhas2[1]) + " " + str(m2linhas2[2]) + " }\n"
      "3 - { " + str(m2linhas3[0]) + " " + str(m2linhas3[1]) + " " + str(m2linhas3[2]) + " }\n"
      "            3x3")

op = int(input("Deseja realizar a Soma ou a Multiplicação das matrizes? \n"
           "Soma - 1\n"
           "Multiplicação - 2\n"
           "Fechar o programa - 0\n"))

if op == 1:
    print("Soma das matrizes realizadas: ")
    print("      1 2 3\n"
          "1 - { " + str(m1linhas1[0] + m2linhas1[0]) + " " + str(m1linhas1[1] + m2linhas1[1]) + " " + str(m1linhas1[2] + m2linhas1[2]) + " }\n"
          "2 - { " + str(m1linhas2[0] + m2linhas2[0]) + " " + str(m1linhas2[1] + m2linhas2[1]) + " " + str(m1linhas2[2] + m2linhas2[2]) + " }\n"
          "3 - { " + str(m1linhas3[0] + m2linhas3[0]) + " " + str(m1linhas3[1] + m2linhas3[1]) + " " + str(m1linhas3[2] + m2linhas3[2]) + " }\n"
          "            3x3")

elif op == 2:
    print("Multiplicação das matrizes realizadas: ")
    print("      1 2 3\n"
          "1 - { " + str((m1linhas1[0] * m2linhas1[0]) + (m1linhas1[1] * m2linhas2[0]) + (m1linhas1[2] * m2linhas3[0])) + " " +
          str((m1linhas1[0] * m2linhas1[1]) + (m1linhas1[1] * m2linhas2[1]) + (m1linhas1[2] * m2linhas3[1])) + " " +
          str((m1linhas1[0] * m2linhas1[2]) + (m1linhas1[1] * m2linhas2[2]) + (m1linhas1[2] * m2linhas3[2])) + " }\n"
          "2 - { " + str((m1linhas2[0] * m2linhas1[0]) + (m1linhas2[1] * m2linhas2[0]) + (m1linhas2[2] * m2linhas3[0])) + " " +
          str((m1linhas2[0] * m2linhas1[1]) + (m1linhas2[1] * m2linhas2[1]) + (m1linhas2[2] * m2linhas3[1])) + " " +
          str((m1linhas2[0] * m2linhas1[2]) + (m1linhas2[1] * m2linhas2[2]) + (m1linhas2[2] * m2linhas3[2])) + " }\n"
          "3 - { " + str((m1linhas3[0] * m2linhas1[0]) + (m1linhas3[1] * m2linhas2[0]) + (m1linhas3[2] * m2linhas3[0])) + " " +
          str((m1linhas3[0] * m2linhas1[1]) + (m1linhas3[1] * m2linhas2[1]) + (m1linhas3[2] * m2linhas3[1])) + " " +
          str((m1linhas3[0] * m2linhas1[2]) + (m1linhas3[1] * m2linhas2[2]) + (m1linhas3[2] * m2linhas3[2])) + " }\n"
          "            3x3")
else:
    print("Fechando o programa...")
    exit()
