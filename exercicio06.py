#ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20]
#(incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo
intervalo = 0
fora = 0
for x in range (10):
    num = int (input("Digite um numero:"))
    if num <10 or num > 20:
        fora+=1
    else:
        intervalo+=1
    print (num)

