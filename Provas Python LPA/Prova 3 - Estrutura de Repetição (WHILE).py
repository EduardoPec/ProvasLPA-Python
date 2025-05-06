numero_surpresa = 7
tentativas = 3
print(">JOGO ADIVINHAÇÃO<")
print("-> Você tera 3 chances para adivinhar o número correto, boa sorte!")

while tentativas > 0 and tentativas < 4:
    numero = int(input("Informe um número --> "))
    if numero == numero_surpresa:
        print("----------------------------------------------------------------")
        print(f"Parabéns! O número {numero} digitado está correto")
        print("----------------------------------------------------------------")
        break
    else:
        print("----------------------------------------------------------------")
        print(f"Tente novamente! O número {numero} digitado não está correto")    
        print("----------------------------------------------------------------") 
        tentativas -= 1        
else:
   print("Que pena! Não foi dessa vez, quem sabe na próxima...")
