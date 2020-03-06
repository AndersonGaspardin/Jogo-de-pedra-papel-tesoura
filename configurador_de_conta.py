print("-----------------------------------")
print("Pedra, Papel ou Tesoura\n Setup de conta")
print("Versão 1.0 ")
print("-----------------------------------")
while True:
    usuario = input("Escolha o usuario:  ")
    senha = input("Cadastre uma senha :  ")
    confirma_senha = input("Por favor confirme a senha:  ")

    if senha != confirma_senha:
        print("As senha não estão iguais. Por favor tente novamente.")

    if senha == confirma_senha:
        print("Sua conta foi criada.")
        text_file = open("contas.txt","a")
        text_file.write("\n")
        text_file.write(usuario)
        text_file.write("\n")
        text_file.write(senha)
        text_file.close()
        break
