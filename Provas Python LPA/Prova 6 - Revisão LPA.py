nome_usuario = "eduardo"
senha_usuario = "1234"
tentativas = 3

while tentativas > 0:
    nome = input("Informe o nome de usuário: ")
    senha = input("Informe a senha do usuário: ")
    if nome == nome_usuario and senha == senha_usuario:
        print("=================================")
        print("Login bem sucedido, Bem vindo!")
        print("=================================")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print("====================================================")
            print(f"Login invalido, restam {tentativas} tentativas!")
            print("====================================================")
        else:
          print("==================================================================")
          print(f"Limite máximo de {tentativas} tentativas atingidas! Acesso bloqueado.")
          print("==================================================================")
          for i in range(3):
              print("Acesso bloqueado")