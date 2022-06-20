# TDE detetive

# Membros:
# Victor Hugo Brunetto
# Francisco Ochoa Bonatto
# Gabriela Apetz
# Pedro Guimarães Lopes Martins

from replit import clear
import time

pista_a = False
pista_b = False
pista_c = False
pista_d = False
pista_e = False
pista_f = False
pista_g = False
pista_h = False

pistas = []
locais = ["Capela", "Achados e perdidos", "Corredores", "Quartos", "Piano"]
opcoes_capela = ["Falar com as funcionárias", "Verificar papel no chão", "Corda pendurada nas vigas"]
opcoes_achados_e_perdidos = ["Inspecionar dicionário"]
opcoes_corredores = ["Sons estranhos"]
opcoes_quartos = ["Desenhos nas paredes"]
opcoes_piano = ["Testar o piano", "Olhar dentro do piano"]

clear()

print("Bem vindos ao jogo de detetive")

time.sleep(2)

print("-"*125)
print('''Você é um membro do clube de jornalismo da sua escola e certo dia você fica sabendo de rumores 
sobre acontecimentos sobrenaturais que ocorrem nela, diante disso você se propõe a investigar sendo instigado 
pela sua curiosidade e instinto jornalístico. Muitos deles envolvem fantasmas e rituais, como por exemplo o caso do piano 
da capela que supostamente toca sozinho no meio da noite.''')
print("-"*125)

time.sleep(12)

print("Vamos começar a investigação...")

time.sleep(4)


run = True

def continuar_jogo():
    continuacao = int(input("Continuar investigando?\n1 - Sim\n2 - Tentar solucionar o mistério\n> "))
    if continuacao == 2:
        global run
        run = False

while run:    
    clear()
    print("-"*125)
    print(f"Pistas: {pistas}")
    i = 0
    print("-"*125)
    print("Onde você deseja investigar?\n")
    for local in locais:
        print(f"{i} - {local}")
        i += 1
    escolha = int(input("> "))

    clear()

    print("-"*125)
    print(f"Localização: {locais[escolha]}")
    print("-"*125)



    if escolha == 0:
        j = 0
        print("Opções:\n")
        for opcao in opcoes_capela:
            print(f"{j} - {opcao}")
            j += 1
        selecao = int(input("> "))
        if selecao == 0:
            print("-"*150)
            print('''Você fala com uma funcionária de limpeza e ela te conta que antigamente a igreja tinha um pianista chamado Hans Gruber, mas que ele tirou a própria vida. ''')
            if "Pianista Hans Gruber" not in pistas:
                pistas.append("Pianista Hans Gruber")
            pista_c = True
            print("-"*150)
            time.sleep(6)
        elif selecao == 1:
            print("-"*150)
            print("Você encontra um papel com o nome do pianista Hans Gruber que deveria ter sido entregue para realização de uma missa(será que alguém tentou se livrar dele?) porém ele estava borrado")
            if "Papel da missa do Hans gruber" not in pistas:
                pistas.append("Papel da missa do Hans gruber")
            pista_d = True
            print("-"*150)
            time.sleep(6)
        elif selecao == 2:
            print("-"*150)
            print("Você acha uma corda arrebentada nas vigas da igreja")
            if "Corda arrebentada" not in pistas:
                pistas.append("Corda arrebentada")
            pista_h = True
            print("-"*150)
            time.sleep(6)
        clear()
        continuar_jogo()

    elif escolha == 1:
        j = 0
        print("Opções:\n")
        for opcao in opcoes_achados_e_perdidos:
            print(f"{j} - {opcao}")
            j += 1
        selecao = int(input("> "))
        if selecao == 0:
            print("-"*150)
            print("Você acha um diário abandonado no achados e perdidos mas está faltando páginas")
            if "Dicionário com páginas faltando" not in pistas:
                pistas.append("Dicionário com páginas faltando")
            pista_a = True
            print("-"*150)
            time.sleep(6)
        clear()
        continuar_jogo()

    elif escolha == 2:
        j = 0
        print("Opções:\n")
        for opcao in opcoes_corredores:
            print(f"{j} - {opcao}")
            j += 1
        selecao = int(input("> "))
        if selecao == 0:
            print("-"*150)
            print("Você escuta sussurros dentro da igreja mesmo sem ter ninguém além de você por perto")
            if "Sussurros suspeitos" not in pistas:
                pistas.append("Sussurros suspeitos")
            pista_g = True
            print("-"*150)
            time.sleep(6)
        clear()
        continuar_jogo()
        
    elif escolha == 3:
        j = 0
        print("Opções:\n")
        for opcao in opcoes_quartos:
            print(f"{j} - {opcao}")
            j += 1
        selecao = int(input("> "))
        if selecao == 0:
            print("-"*150)
            print("Você acha desenhos estranhos em uma parede de um quarto abandonado na igreja")
            if "Desenhos na parede" not in pistas:
                pistas.append("Desenhos na parede")
            pista_b = True
            print("-"*150)
            time.sleep(6)
        clear()
        continuar_jogo()
        
    elif escolha == 4:
        j = 0
        print("Opções:\n")
        for opcao in opcoes_piano:
            print(f"{j} - {opcao}")
            j += 1
        selecao = int(input("> "))
        if selecao == 0:
            print("-"*150)
            print("Você investiga o piano e descobre que ele está com defeito")
            if "Piano quebrado" not in pistas:
                pistas.append("Piano quebrado")
            pista_e = True
            print("-"*150)
            time.sleep(6)
        elif selecao == 1:
            print("-"*150)
            print("Você encontra dentro do piano um pedaço do diário que estava faltando")
            if "Páginas do dicionário" not in pistas:
                pistas.append("Páginas do dicionário")
            pista_f = True
            print("-"*150)
            time.sleep(6)
        clear()
        continuar_jogo()
        

if pista_a and pista_c and pista_d and pista_f and pista_b and pista_e and pista_g and pista_h:
    print("-"*125)
    print("Realmente existe um fantasma chamado Hans Gruber e você chama um exorcista para te auxiliar")
    print("-"*125)
elif pista_g or pista_f or pista_h:
    print("-"*125)
    print("O fantasma te encontra antes de você solucionar o caso e você morre.")
    print("-"*125)
else:
    print("-"*125)
    print("Você se infiltra na igreja de noite mas descobre que na verdade quem estava tocando o piano era um mendigo super dotado pianista")
    print("-"*125)