print("-----Exercício 1-----")
Niv_Reservatório = float(input("Digite o nível atual do reservatório de água(em %) = "))
if Niv_Reservatório <= 100:
   if Niv_Reservatório < 20:
      print("Nível Crítico - Ligar Bomba de Emergência")
   elif Niv_Reservatório >= 20 and Niv_Reservatório <= 80:
      print("Nível Operacional - Monitorar")
   elif Niv_Reservatório > 80:
      print("Nível Alto - Desligar Entrada")
print("\n-----Exercício 2-----")
tensoes = [12.5 , 11.9 , 13.1 , 10.5 , 12.0 , 11.8 , 13.5 , 12.2 , 11.5 , 12.8]
soma = 0
fora_da_faixa = 0
for i in tensoes:
    soma += i 
    if i <= 12.5 and i >= 11.5:
       fora_da_faixa += 1
media = soma / len(tensoes)
print(f"Média = {media}\nMax:{ max(tensoes)}V,\nMin: {min(tensoes)}V")
print("\n-----Exercício 3-----")
N = int(input("Digite um número inteiro = "))
a = 0
b = 1
contador = 0
while contador < N:
    print(a)
    c = a + b
    a = b
    b = c
    contador += 1
print("\n-----Exercício 4------")
matriz = [
  ["", "", ""] ,
  ["", "", ""] ,
  ["", "", ""]
]
soma_diagonal = 0
for i in range(len(matriz)):
      for j in range(len(matriz[i])):
           matriz[i][j] = int(input(" Elemento = "))
print("Matriz: ")
for i in range(len(matriz[i])):
    print(matriz[i])
for i in range(3):
    soma_diagonal += matriz[i][i]
print(f"A soma das diagonais: {soma_diagonal}")
