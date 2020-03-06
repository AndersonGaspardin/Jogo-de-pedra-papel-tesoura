import time
import random

print("Pedra, Papel ou Tesoura\n Versão 1.0 ")
print("Feito por Andereson H. Gaspardine Jr.")

derrota = "A máquina venceu"
vitoria = "Você venceu"

vidas = 7
vidas_da_maquina = 10
placar = 0
empate = 0
lista_senhas = []
while True:
    print("Para começar complete as informções abaixo.")
    usuario = input("Por Favor entre com o seu usuário:\t")
    senha = input("Por favor entre com o sua senha:\t")
    procura_em_arquivo = open("contas.txt", "r")
    for linha in procura_em_arquivo:
        if usuario and senha in linha:
            print("Acesso concedido.")
            time.sleep(0.5)
            print("Carregando.")
            time.sleep(0.5)
            print("Carregando..")
            time.sleep(0.5)
            print("Carregando...")
            time.sleep(0.5)
            menu_inicial = """
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     ___                  ______________     ______________     _______________     ____      ___                                            
    ¦   ¦                ¦              ¦   ¦              ¦   ¦               ¦   ¦    ¦    /   /                                           
 /------------------     ¦     ___      ¦   ¦  __________  ¦   ¦  _____________¦   ¦    ¦   /   /                                            
/            \     ¦     ¦    ¦   ¦     ¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦  /   /                                             
¦       ------------     ¦    ¦___¦   __¦   ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦_/   /                                              
¦       ------------     ¦           \      ¦ ¦          ¦ ¦   ¦ ¦                 ¦         /                                               
¦            \     ¦     ¦    ¦\      \     ¦ ¦          ¦ ¦   ¦ ¦                 ¦    ¦\   \                                               
¦       ------------     ¦    ¦ \      \    ¦ ¦__________¦ ¦   ¦ ¦_____________    ¦    ¦ \   \                                              
¦       ------------     ¦    ¦  \      \   ¦              ¦   ¦               ¦   ¦    ¦  \   \                   ___  ___  ___  ___    
¦            \     ¦     ¦____¦   \______\  ¦______________¦   ¦_______________¦   ¦____¦   \___\                 ¦   ¦¦   ¦¦   ¦¦   ¦       
¦       ------------                                                                                          ___ ¦   ¦¦   ¦¦   ¦¦   ¦       
\       ------------ ___________     _______________     ___________     ___________     _____________       ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
 \           \     /¦   _____   ¦   ¦     _____     ¦   ¦   _____   ¦   ¦           ¦   ¦             ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
  \---------------/ ¦  ¦     ¦  ¦   ¦    ¦_____¦    ¦   ¦  ¦     ¦  ¦   ¦    _______¦   ¦     ___     ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦  ¦_____¦  ¦   ¦     _____     ¦   ¦  ¦_____¦  ¦   ¦   ¦           ¦    ¦   ¦    ¦      ¦   ¦¦   ¦¦   ¦¦   ¦¦   ¦       
                    ¦    _______¦   ¦    ¦     ¦    ¦   ¦    _______¦   ¦   ¦_____      ¦    ¦___¦   _¦      \                       /       
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦    _____¦     ¦           \         \                     /        
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦   ¦_______    ¦    ¦\      \         \                   /         
                    ¦   ¦           ¦    ¦     ¦    ¦   ¦   ¦           ¦           ¦   ¦    ¦ \      \         \                 /                                _____
                    ¦___¦           ¦____¦     ¦____¦   ¦___¦           ¦___________¦   ¦____¦  \______\         \_______________/                                /     /
                                                                                                                                                                 /     /
 ______________     _______________     ____     ______________     ______________     ______________     _____________     ______________                    /     /
¦   ___________¦   ¦               ¦   ¦    ¦   ¦   ___________¦   ¦   ___________¦   ¦              ¦   ¦             ¦   ¦   ___________¦    ________    /     /
¦  ¦               ¦  _____________¦   ¦    ¦   ¦  ¦               ¦  ¦               ¦  __________  ¦   ¦     ___     ¦   ¦  ¦               /          /     /
¦  ¦___________    ¦ ¦                 ¦    ¦   ¦  ¦___________    ¦  ¦___________    ¦ ¦          ¦ ¦   ¦    ¦   ¦    ¦   ¦  ¦___________   ¦         /     /
¦____________  ¦   ¦ ¦                 ¦    ¦   ¦____________  ¦   ¦____________  ¦   ¦ ¦          ¦ ¦   ¦    ¦___¦   _¦   ¦____________  ¦  ¦       /     /
             ¦ ¦   ¦ ¦                 ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦          ¦ ¦   ¦           \                  ¦ ¦  ¦               __________________
             ¦ ¦   ¦ ¦_____________    ¦    ¦                ¦ ¦                ¦ ¦   ¦ ¦__________¦ ¦   ¦    ¦\      \                 ¦ ¦  ¦                                 ¦
 ____________¦ ¦   ¦               ¦   ¦    ¦    ____________¦ ¦    ____________¦ ¦   ¦              ¦   ¦    ¦ \      \    ____________¦ ¦  ¦               __________________¦
¦______________¦   ¦_______________¦   ¦____¦   ¦______________¦   ¦______________¦   ¦______________¦   ¦____¦  \______\  ¦______________¦  ¦______________¦

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Regras:
                Você escolhe o nivel de dificuldade: 1 = Fácil, 2 = Médio e 3 = Dificil
                No fácil você terá 7 vidas e a maquina terá 10;
                No Médio você terá 5 vidas e a maquina terá 15;
                No Dificil você terá somente 3 vidas e a maquina terá 20.
                
                Se você vencer uma rodada, ganhará uma vida extra e o computador perderá uma vida.
                Se você perder uma rodada, perderá uma vida, porém o computador nao ganha uma vida extra
                Se empatar as vidas dos dois jogadores se mantêm.
                -----------------------------------------
                Para abrir as regras digite regras.
                -----------------------------------------
                Você pode sair do jogo a qualquer momento, basta digitar sair.
                -----------------------------------------
                 Para visualizar o número de vitórias digite placar
                 Para visualizar o número de empates digite empate
                 Para visualizar o número de vidas que ainda tem digite vidas
                 
                 Você consegue vencer "A Máquina".
                 Boa sorte!!!
                """
            print(menu_inicial)
            dificuldade = 0
            dificuldade_valida = False
            while not dificuldade_valida:
                if dificuldade == 1:
                    dificuldade_valida = True
                if dificuldade == 2:
                    vidas = 5
                    vidas_da_maquina = 15
                    dificuldade_valida = True
                if dificuldade == 3:
                    vidas = 3
                    vidas_da_maquina = 20
                    dificuldade_valida = True
                else:
                    dificuldade = int(input("Qual o nivel de dificuldade: 1 = Fácil, 2 = Médio e 3 = Dificil:\t"))

            valendo = True
            while valendo:
                ppt = str.capitalize(input("Pedra, Papel ou Tesoura?\t"))
                computador_ppt = ("Pedra", "Papel", "Tesoura")
                computador_ppt = random.choice(computador_ppt)
                # Escolhendo Pedra
                if ppt == "Pedra" and computador_ppt == "Papel":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(derrota)
                    print("")
                    print("")
                    vidas -= 1
                if ppt == "Pedra" and computador_ppt == "Tesoura":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(vitoria)
                    print("")
                    print("")
                    placar += 1
                    vidas += 1
                    vidas_da_maquina -= 1

                # Escolhendo Papel
                if ppt == "Papel" and computador_ppt == "Tesoura":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(derrota)
                    print("")
                    print("")
                    vidas -= 1
                if ppt == "Papel" and computador_ppt == "Pedra":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(vitoria)
                    print("")
                    print("")
                    placar += 1
                    vidas += 1
                    vidas_da_maquina -= 1

                # Escolhendo Tesoura
                if ppt == "Tesoura" and computador_ppt == "Pedra":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(derrota)
                    print("")
                    print("")
                    vidas -= 1
                if ppt == "Tesoura" and computador_ppt == "Papel":
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print(vitoria)
                    print("")
                    print("")
                    placar += 1
                    vidas += 1
                    vidas_da_maquina -= 1

                # Em caso de Empate
                if ppt == computador_ppt:
                    print(f"O computador escolheu: {computador_ppt}.")
                    print("")
                    print("Empataram")
                    print("")
                    print("")
                    empate += 1

                # Menu do sistema
                if ppt == "Regras":
                    print("**********************************************")
                    print("Regras")
                    print("**********************************************")
                    print("-Pedra amassa a Tesoura")
                    print("-Papel embrulha a Pedra")
                    print("-Tesoura corta o Papel")
                    print("**********************************************")
                if ppt == "Vidas":
                    print("**********************************************")
                    print(f"Ainda restam {vidas} vidas.")
                    print("**********************************************")
                if ppt == "Placar":
                    print("**********************************************")
                    print(f"Você já venceu {placar} rodadas da maquina.")
                    print("**********************************************")
                if ppt == "Empate":
                    print("**********************************************")
                    print(f"Você já empatou {empate} rodadas da maquina.")
                    print("**********************************************")

                # Um dos participantes ficando sem vida
                if vidas == 0:
                    print("Obrigado por jogar.")
                    print("Acabaram as suas vidas")
                    print(f"Você venceu {placar} rodadas da 'A Maquina'")
                    print(f"Você e 'A Maquina' empataram {empate} rodadas")
                    stop = input("Pressione ENTER para sair.")
                    valendo = False
                    nivel = ['', 'Fácil', 'Médio', 'Difícil']
                    nivel = nivel[dificuldade]
                    text_file = open("resultados.txt","a")
                    text_file.write("\n")
                    text_file.write(f"\tO usuario {usuario} perdeu da maquina após ganhar {placar} rodadas e empatar {empate} vezes no nível {nivel}")
                    text_file.write("\n")
                if vidas_da_maquina == 0:
                    print("Obrigado por jogar.")
                    print("Acabaram as vidas da máquina.")
                    print("VOCÊ VENCEU")
                    nivel = ['', 'Fácil', 'Médio', 'Difícil']
                    nivel = nivel[dificuldade]
                    print(f"Você venceu 'A Maquina' no nível {nivel[dificuldade]}")
                    print(f"Você e 'A Maquina' empataram {empate} rodadas")
                    stop = input("Pressione ENTER para sair.")
                    valendo = False
                    text_file = open("resultados.txt", "a")
                    text_file.write("\n")
                    text_file.write(
                        f"\tO usuario {usuario} ganhou da maquina após ganhar {placar} rodadas e empatar {empate} vezes no nível {nivel}")
                    text_file.write("\n")
                if ppt == "Sair":
                    valendo = False
                    text_file = open("resultados.txt", "a")
                    text_file.write("\n")
                    text_file.write(
                        f"\tO usuario {usuario} saiu do jogo com {placar} rodadas ganhas e {empate} empates no nível {nivel}")
                    text_file.write("\n")
        if usuario in linha and senha != linha:
            print("Sua senha está incorreta.")
            print("-------------------------")
