numero_inicial = int(input("Informe o inicio do intervalo: "))
numero_final = int(input("Informe o final do intervalo: "))
numeros_pares = 0

for numero in range(numero_inicial, numero_final + 1):
    if numero%2==0:
        numeros_pares+=numero


if numeros_pares > 0:  
    print("----------------------------------------------------")
    print(f"A soma dos números pares no intervalo é igual a: {numeros_pares}")
    print("----------------------------------------------------")
else:
    print("--------------------------------------------")
    print("Não existem números pares nesse intervalo")
    print("--------------------------------------------")
    


