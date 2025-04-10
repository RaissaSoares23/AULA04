#ler 5 valores, calcular e escrever a média aritmética desses valores lidos
soma = 0
for x in range (6):
    nota = float (input("Digita sua nota:"))
    soma=soma+nota

media = soma/5
print (media)