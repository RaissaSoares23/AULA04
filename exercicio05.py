#ler 10 numeros e escrever quantos desses valores lidos são negativos

soma = 0
for x in range (1,11):
    num = int (input("Digite um numero:"))
    if num < 0:
        soma=soma + 1

print(soma)
