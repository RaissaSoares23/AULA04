num = int (input("Digite um numero:"))
if num > 0:
    for x in range(1, num + 1,1):
        print (x, end = " ")
else:
    print("Número inválido")
    