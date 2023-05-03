# Bibliotecas
from time import sleep
import sys
import os

# Cores
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
azul_amarelo = '\033[7;33:44m'
reset = '\033[0m'


########### LOGO DO JOGO #############
def escrita_top(text):
    for letra in text:
        sys.stdout.write(letra)
        sys.stdout.flush()
        sleep(0.01)


# Looping (do menu de ajuda e objetivo) que "impede" que o usuário digite opções inválidas.
def Looping():
    resposta2 = str(
        input(yellow + "Deseja retornar ao Menu Inicial? [S/N] " + reset))
    if resposta2.lower().strip() == "s":
        os.system('clear')

    else:
        while resposta2.lower().strip() != "s":
            print(Red + "\nDigite uma opção válida.\n" + reset)
            resposta2 = str(
                input(yellow + "Deseja retornar ao Menu Inicial? [S/N] " +
                      reset))
            os.system('clear')
            continue


#-----------______ COMO JOGAR ______----------
def Objetivo():
    print('''\nCOMO JOGAR:\n
• O objetivo do jogo é simples: Acerte as questões propostas para avançar no jogo.\n
• Responda com letras, um claro exemplo é: Se a resposta certa for "a", então digite "a" e não a resposta por extenso (Dinossauro é a exceção!).\n 
• Em certos momentos o grande sábio Albert Sócrates irá te ajudar.\n 
• Em certos momentos um erro pode ser bastante trágico. \n
        
  ''')
    Looping()


# FUNÇÃO QUE LIMPA O TERMINAL
def limp():
    sleep(1)
    os.system('clear')


#FUNÇÃO QUE VOLTA A PRIMEIRA FASE DO JOGO CASO O JOGADOR NÃO RESPONDA CORRETAMENTE
def Elss():
    print(Red + '\nResposta incorreta. Tente novamente!' + reset)
    sleep(1)
    os.system('clear')


text = (Cyan + '''
  __  __              _______   _    _      ____    _    _   _____   ______
 |  \/  |     /\     |__   __| | |  | |    / __ \  | |  | | |_   _| |___  /
 | \  / |    /  \       | |    | |__| |   | |  | | | |  | |   | |      / / 
 | |\/| |   / /\ \      | |    |  __  |   | |  | | | |  | |   | |     / /  
 | |  | |  / ____ \     | |    | |  | |   | |__| | | |__| |  _| |_   / /__ 
 |_|  |_| /_/    \_\    |_|    |_|  |_|    \___\_\  \____/  |_____| /_____|
                                                                           
                                                                  
''' + reset)

escrita_top(text)

sleep(2)

#---------_________ 1ª FASE ------________


def Fase1():
    os.system('clear')
    print(yellow + "\nComeçando jornada 1... Boa Sorte, você vai precisar!\n" +
          reset)
    sleep(1)
    print(
        blue +
        '''Jurandir Albuquerque: Em um colégio, de 100 alunos, 80 gostam de sorvete de chocolate, 70 gostam de sorvete de creme e  60 gostam dos dois sabores.\n'''
    )
    print(Blue + '''
[A] - 0
  
[B] - 10
  
[C] - 20
  ''' + reset)
    opção1 = input(
        '\nJurandir Albuquerque: Quantos alunos não gostam de nenhum dos dois sabores? '
    )

    if opção1.lower().strip() == "b" or opção1.lower().strip() == '10':
        print(Green + "\nResposta correta!\n" + reset)
        limp()
    elif opção1 == "lafond":
        Fase4()
    else:
        while opção1.lower().strip() != 'b':
            print(Red + 'Resposta incorreta, digite novamente!' + reset)

            opção1 = input(
                '\nJurandir Albuquerque: Quantos alunos não gostam de nenhum dos dois sabores? '
            )
        # FIM DO 1º ELSE
    print(Green + "\nResposta correta!\n" + reset)
    sleep(1)
    os.system('clear')
    print(
        blue +
        '''Jurandir Albuquerque: Numa pesquisa de mercado, verificou-se que 15 pessoas utilizam pelo menos um dos produtos A ou B. Sabendo que 10 dessas pessoas não usam o produto B e que 2 dessas pessoas não usam o produto A. '''
        + reset)
    sleep(1)
    print(Blue + '''
[A] - 0
  
[B] - 2
  
[C] - 3''' + reset)

    sleep(0.05)
    opção2 = input(
        '\nJurandir Albuquerque: Qual é o número de pessoas que utilizam os produtos A e B? '
    )
    if opção2.lower().strip() == "c" or opção2.lower().strip() == '3':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 2º ELSE

    print(
        Blue +
        "\nAlbert Sócrates, o ancião zoroastra: Para passar leia os objetivos do jogo.\n "
        + reset)

    dino = input("\nJurandir Albuquerque: Digite algo no teclado: ")

    if dino.lower() == "dinossauro":
        print(Green + "\nResposta correta!" + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 3º ELSE

    print(blue + 'Jurandir Albuquerque: Assinale a alternativa INCORRETA: \n' +
          reset)
    print(Red + "NÃO SÃO NÚMEROS RACIONAIS:\n " + reset)
    print(Blue + '''[A] - AS DÍZIMAS NÃO PERIÓDICAS
[B] - AS RAÍZES NÃO EXATAS.              
[C] - A RAÍZ QUADRADA DE NÚMEROS NEGATIVOS.
[D] - NENHUMA DAS ANTERIORES.\n''' + reset)
    opção3 = input("Jurandir Albuquerque: Digite sua resposta: ")
    if opção3.lower().strip() == "d" or opção3.lower().strip(
    ) == 'nenhuma das anteriores':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 4º ELSE

    print(blue + 'Jurandir Albuquerque: Considere os conjuntos' + reset)
    print(Blue + '''
A = {1, 4, 7}
B = {1, 3, 4, 5, 7, 8}
          
\033[0;93mÉ correto afirmar que:\033[m
\033[0;34m         
[A] - A superconjunto B
[B] - A subconjunto B
[C] - B ⊅ A
[D] - B intersecção A''' + reset)
    opção4 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção4.lower().strip() == 'b' or opção4.lower().strip(
    ) == 'a subconjunto b':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 5º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Observe os conjuntos a seguir e marque a alternativa correta.'
        + reset)
    print(Blue + '''

A = {x|x é um múltiplo positivo de 4}
B = {x|x é um número par e 4 menor que ou igual a inclinado x menor que 16}

[A] - 145 pertence A
[B] - 26 pertence A e B
[C] - 11 pertence B
[D] - 12 pertence A e B ''' + reset)
    opção5 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção5.lower().strip() == 'd' or opção5.lower().strip(
    ) == '12 pertence a e b':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
    Fase2()


#--------------------------------------|
#_____________ 2ª FASE ________________|
#--------------------------------------|
def Fase2():
    os.system('clear')
    print(
        Green +
        "\nParabéns, você conseguiu, por um milagre divino, chegar até aqui! Boa sorte, de novo.\n"
        + reset)
    sleep(1)
    print(
        blue +
        '''Jurandir Albuquerque: Sobre o plano cartesiano, julgue as afirmativas a seguir:.\n'''
    )
    print(Blue + '''
I - O eixo horizontal é conhecido também como eixo das abscissas.

II - O ponto A (-5, 3) é um ponto do terceiro quadrante.

III - O eixo vertical é conhecido também como eixo das coordenadas.

\033[0;93mPodemos afirmar que:\033[m

\033[0;34mA) Somente a afirmativa I é verdadeira.

B) Somente a afirmativa II é verdadeira.

C) Somente a afirmativa III é verdadeira.

D) Somente as afirmativas II e III são verdadeiras.

E) Somente as afirmativas I e III são verdadeiras.\033[m
  ''' + reset)
    opção6 = input('\nJurandir Albuquerque: Digite sua resposta: ')

    if opção6.lower().strip() == "a":

        print(Green + "\nResposta correta!\n" + reset)
        limp()
    else:
        while opção6.lower().strip() != 'a':
            print(Red + 'Resposta incorreta! Tente novamente' + reset)
            opção6 = input('\nJurandir Albuquerque: Digite sua resposta: ')
        # FIM DO 7º ELSE

    print(Green + "\nResposta correta!\n" + reset)
    sleep(1)
    limp()
    print(
        blue +
        '''Jurandir Albuquerque: Em um plano cartesiano, foram marcados os pontos A (2, 3), B(-1, 2), C (2, -3) e D (1, 0). O único quadrante em que não há nenhum ponto marcado é:. '''
        + reset)
    sleep(1)
    print(Blue + '''
[A] I

[B] II

[C] III

[D] IV
''' + reset)

    sleep(0.05)
    opção7 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção7.lower().strip() == "c" or opção7.lower().strip() == 'III':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 8º ELSE

    print(
        blue +
        "Jurandir Albuquerque: O plano cartesiano é um sistema de coordenadas desenvolvido por René Descartes. Esse sistema de coordenadas é formado por duas retas perpendiculares, chamadas de eixos cartesianos. O plano cartesiano é dividido em quadrantes. Sobre os quadrantes do plano cartesiano, considerando um ponto A (x, y), em que x > 0 e y < 0, temos um ponto que pertence ao:\n"
        + reset)
    print(Blue + '''[A] primeiro quadrante

[B] segundo quadrante

[C] terceiro quadrante

[D] quarto quadrante

[E] eixo das abscissas          
''' + reset)

    opção8 = input("\nJurandir Albuquerque: Digite sua resposta: ")

    if opção8.lower().strip() == "d" or opção8.lower().strip(
    ) == 'quarto quadrante':
        print(Green + "\nResposta correta!" + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 9º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Sobre o plano cartesiano, julgue as afirmativas a seguir:\n'
        + reset)
    print(
        Blue +
        '''I - Os pontos no plano cartesiano são conhecidos como par ordenado.

II - No primeiro quadrante, o par ordenado (x, y) é composto por dois números positivos.

III - No quarto quadrante, o par ordenado (x, y) é composto por dois números negativos.
          
''' + reset)
    print(yellow + 'As afirmativas I, II e III são, respectivamente:\n' +
          reset)
    print(Blue + '''A) Verdadeira, falsa e verdadeira.

B) Falsa, verdadeira e verdadeira.

C) Verdadeira, verdadeira e falsa.

D) Falsa, verdadeira e falsa.

E) Verdadeira, verdadeira e verdadeira.\n''' + reset)

    opção9 = input("Jurandir Albuquerque: Digite sua resposta: ")
    if opção9.lower().strip() == "c" or opção9.lower().strip(
    ) == 'Verdadeira, verdadeira e falsa':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase1()
        # FIM DO 10º ELSE

    print(
        blue +
        'Jurandir Albuquerque: De acordo com conteúdo estudado sobre matrix, marque a opção verdadeira: \n'
        + reset)
    print(Blue + '''[A] Matriz transposta é quando a linha vira coluna

[B] - O primeiro número da matriz sempre será a quantidade de colunas

[C] - Matriz nula é quando contém apenas números negativos

[D] - Matriz oposta é a matriz que contém os mesmos números, porém em posição opostas

''' + reset)
    opção10 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção10.lower().strip() == 'a':
        print(Green + "\nResposta correta! " + reset)
        limp()
        Fase3()
    else:
        Elss()
        Fase1()
        # FIM DO 11º ELSE


#--------------------------------------|
#_____________ 4ª FASE ________________|
#--------------------------------------|
def Fase4():
    os.system('clear')
    print(Green +
          "\nParabéns, você conseguiu avançar para a 4ª e última fase!\n" +
          reset)
    sleep(1)
    print(
        yellow +
        'É melhor você tentar algo, vê-lo não funcionar e aprender com isso, do que não fazer nada. - Jorge Lafond. 250.A.C \n\n'
        + reset)
    sleep(1)
    print(
        blue +
        '''Jurandir Albuquerque: Temos o conjunto A = {2, 6, 10. 4. 8} E o conjunto B = {10, 7, 4, 8, 2}  .\n'''
    )
    print(yellow + "\nOnde estão localizados os elementos 2, 4, 8?\n")
    print(Blue + '''[A]  Conjunto A .
[B] Na interseção de A e B.
[C] O conjunto B.         
[D] No conjunto A e B menos a INTERSEÇÃO.         
                 
''' + reset)
    opção11 = input('\nJurandir Albuquerque: Digite sua resposta: ')

    if opção11.lower().strip() == "b":

        print(Green + "\nResposta correta!\n" + reset)
        limp()
    else:
        limp()
        Fase3()
        # FIM DO 12º ELSE

    print(Green + "\nResposta correta!\n" + reset)
    sleep(1)
    limp()
    print(blue + '''Jurandir Albuquerque: Marque a alternativa correta:\n''' +
          reset)
    print(yellow + '''A = {X | X é um múltiplo positivo de 4}\n
B = {X | X É UM NÚMERO par 4<=X<16}\n          
''' + reset)
    sleep(1)
    print(Blue + '''
[A] 145 PERTENCE a A
[B] 26 PERTENCE a A e B primeira coluna e assim por diante. O que é linha vira coluna.
[C] 11 PERTENCE a B
[D] 12 Pertence a A e B
''' + reset)

    sleep(0.05)
    opção12 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção12.lower().strip() == "d":
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 13º ELSE

    print(
        blue +
        "Jurandir Albuquerque: Represente os conjuntos:\nA = {-3, -1. 0, 1. 6, 7}\nB = {-4, 1, 3, 5, 6, 7}\n"
        + reset)
    sleep(1)
    print(yellow + 'Conjunto A = -3, -1, 0, 1, 6, 7' + reset)
    print(yellow + 'Conjunto B = -4, 1, 3, 5, 6, 7 ' + reset)
    print(yellow + 'Conjunto c = -5, -3, 1, 2, 3, 5 ' + reset)
    sleep(1)
    print(yellow +
          '\nDetermine a INTERSEÇÃO de B com União dos conjuntos A e B:  \n' +
          reset)
    print(Blue + '''[A] - {1, 3, 6, 7, 8, }
[B] - {3, 5, 6,8, 9,20}          
[C] - {1,5, 7, 3, 2, 6, 7}
[D] - {1, 3, 5, 6, 7}
[E] - {1, 6, 4, 5, 6, 7,}
          
''' + reset)

    opção13 = input("\nJurandir Albuquerque: Digite sua resposta: ")

    if opção13.lower().strip() == "d":
        print(Green + "\nResposta correta!" + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 14º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Nos conjuntos A e B, qual alternativa representa uma relação de inclusão? \n'
        + reset)
    print(Blue + '''[A] Conjunto A e B seperados
[B] Conjunto B dentro do conjunto A
[C] INTERSEÇÃO do conjunto A e B
[D] Conjunto A MAIOR que conjunto B    
''' + reset)

    opção14 = input("Jurandir Albuquerque: Digite sua resposta: ")
    if opção14.lower().strip() == "b":
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 15º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Sendo A = {1, 3, 6, 12, 15, 19} e B = {1, 2, 3, 8, 9} \n'
        + reset)
    print(yellow + "Determine: A - B" + reset)
    sleep(1)
    print(yellow + '\nMarque a alternativa correta:\n' + reset)
    print(Blue + '''[A] - {1, 2, 3, 6, 8, 12, 15, 19}
[B] - {1, 3, }        
[C] - {6, 12, 15, 19}           
          ''' + reset)
    opção15 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção15.lower().strip() == 'c':
        print(Green + "\nResposta correta! " + reset)
        limp()
        print(
            yellow +
            "Parabéns, você concluiu o desafio! Não tem nenhuma recompensa.\n\n"
            + reset)
        sleep(1)
        print(
            Purple +
            '''  ____                 _                        _            __                _ 
 |  _ \       _       | |                      | |          / _|              | |
 | |_) |_   _(_)      | | ___  _ __ __ _  ___  | |     __ _| |_ ___  _ __   __| |
 |  _ <| | | |    _   | |/ _ \| '__/ _` |/ _ \ | |    / _` |  _/ _ \| '_ \ / _` |
 | |_) | |_| |_  | |__| | (_) | | | (_| |  __/ | |___| (_| | || (_) | | | | (_| |
 |____/ \__, (_)  \____/ \___/|_|  \__, |\___| |______\__,_|_| \___/|_| |_|\__,_|
         __/ |                      __/ |                                        
        |___/                      |___/                                  ''' +
            reset)
        sleep(10)
        quit()
    else:
        Elss()
        Fase3()
        # FIM DO 16º ELSE


def Fase3():
    os.system('clear')
    print(Green + "\nParabéns, você conseguiu avançar para a 3ª fase!\n" +
          reset)
    sleep(1)
    print(Red + 'Aqui o caldo começa a esquentar...\n\n' + reset)
    sleep(1)
    print(
        blue +
        '''Jurandir Albuquerque: Dados os pares ordenados A (-3,-3) , B (3,-3), C(3,3) e D (-3,3),desenvolva o plano cartesiano e represente a figura geométrica encontrada, tamanho do eixo AB e tamanho do eixo AD.'''
    )
    print(
        Blue +
        '''[A] Figura representada: Quadrado | Tamanho do eixo AB = 6 | Tamanho do eixo AD = 6.
[B] Figura representada: Quadrado | Tamanho do eixo AB = 6 | Tamanho do eixo AD = 7.
[C] Figura representada: Bob Esponja | Tamanho do eixo AB = 6| Tamanho do eixo AD = 5.         
[D] Figura representada: Triângulo | Tamanho do eixo AB = 12 | Tamanho do eixo AD = 9.         
[E] Figura representada: Quadrado | Tamanho do eixo AB = 13 | Tamanho do eixo AD = 8.\n      
                 
''' + reset)
    opção11 = input('\nJurandir Albuquerque: Digite sua resposta: ')

    if opção11.lower().strip() == "a":

        print(Green + "\nResposta correta!\n" + reset)
        limp()
    else:
        limp()
        Fase3()
        # FIM DO 12º ELSE

    print(Green + "\nResposta correta!\n" + reset)
    sleep(1)
    limp()
    print(
        blue +
        '''Jurandir Albuquerque: De acordo com o que você estudou sobre os tipos de matrizes, marque a opção correta: '''
        + reset)
    sleep(1)
    print(Blue + '''
[A] Matriz  Nula é caracterizada por não conter elementos dentro da matriz.\n
[B] Matriz Transposta é quando linhas e colunas são trocadas: a primeira linha vira 
primeira coluna e assim por diante.O que é linda vira coluna.\n
[C] Matriz Oposta é a obtida pela inversão dos elementos da primeira matriz com os elementos da segunda matriz, nos seus respectivos lugares. O seja; O elemento da 1ª linha e 1ª coluna da Matriz A, vira o elemento da 1ª linha e 1ª coluna da matriz B.\n
[D] Matriz Diagonal é uma matriz quadrada com vários números 1 na sua diagonal principal, e zero em todas as demais posições.\n
''' + reset)

    sleep(0.05)
    opção12 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção12.lower().strip() == "d":
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 13º ELSE

    print(
        blue +
        "Jurandir Albuquerque: De acordo com os conjuntos apresentados, é verdade que , das afirmações:\n"
        + reset)
    sleep(1)
    print(yellow + 'Conjunto A = 2, 3, 6, 9, 15, 17' + reset)
    print(yellow + 'Conjunto B = 2, 6, 15' + reset)
    sleep(1)
    print(Blue + '''\nI - Nenhum elemento de A pertence ao conjunto B

II - Alguns elementos de A pertencem ao conjunto B.

III -  O conjunto B é um conjunto unitário.

IV - Todos os elementos de B pertencem ao conjunto A.

V - O conjunto B é um subconjunto de A. 

''' + reset)
    print(yellow + 'São verdadeiras somente:\n' + reset)
    sleep(0.9)
    print(Blue + '''[A] - I e II
[B] - II e IV          
[C] - II e V
[D] - I e IV
[E] - II, IV e V
          
''' + reset)

    opção13 = input("\nJurandir Albuquerque: Digite sua resposta: ")

    if opção13.lower().strip() == "e":
        print(Green + "\nResposta correta!" + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 14º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Dada a função: Y = 2x + 3 , e sabendo que  x = {2,4,5}, Determine os pares ordenados e desenvolva o plano cartesiano:\n'
        + reset)
    print(Blue + '''[A] (2,5) (4,30) (5,2)
[B] (2,12) (4,11) (5,13)
[C] (2,9) (43,-122) (5,12)
[D] (2,5) (4,3) (5,6)
[E] (2,4) (4,15) (5,9)
[F] (2,7) (4,11) (5,13)          
[G] (2,7) (4,11) (5,13)        
[H] (2,2) (4,1) (5,-2)       
''' + reset)

    opção14 = input("Jurandir Albuquerque: Digite sua resposta: ")
    if opção14.lower().strip() == "g" or opção14.lower().strip() == 'f':
        print(Green + "\nResposta correta! " + reset)
        limp()
    else:
        Elss()
        Fase3()
        # FIM DO 15º ELSE

    print(
        blue +
        'Jurandir Albuquerque: Descreva os seguintes conjuntos, listando seus elementos.\n'
        + reset)
    print(Blue + '''I - {x / x é um número inteiro e 5<x<12}

II - { x / x é uma cor que está presente na bandeira do Brasil}

III - { x / x é o resultado da soma ( 25 +23) }
\n''' + reset)
    sleep(1)
    print(yellow + '\nMarque a alternativa correta:\n' + reset)
    print(
        Blue +
        '''[A] - I = {  6,7,8,9,10,11}  | II = { Verde, amarelo, azul e branco}   | III = {40}
[B] - I = {  6,7,6,8,10,11}  | II = { Verde, amarelo, azul e branco}   | III = {45}        
[C] - I = {  6,7,8,9,10,11}  | II = { Verde, amarelo, azul e branco}   | III = {48}          
[D] - I = {  5,8,8,8,10,11}  | II = { Verde, amarelo, azul e branco}   | III = {47}          
[E] - I = {  5,15,9,8,10,11} | II = { Verde, amarelo, azul e branco}   | III = {45}         
[F] - I = {  6,2,3,3,10,11}  | II = { Verde, amarelo, azul e branco}   | III = {45}    
          ''' + reset)
    opção15 = input('\nJurandir Albuquerque: Digite sua resposta: ')
    if opção15.lower().strip() == 'c':
        print(Green + "\nResposta correta! " + reset)
        limp()
        Fase4()
    else:
        Elss()
        Fase3()
        # FIM DO 16º ELSE


################## REGRAS DO JOGO ###############
def Regras():

    print('''\n•  Este é um jogo de Multipla escolha.\n       
• Jurandir Albuquerque irá te conduzir ao longo da jornada.\n        
• A cada nível avançado as perguntas ficam mais difíceis.\n                          
• Ao todo são 4 níveis, cada nível contendo 5 perguntas.\n
• Em certos momentos o jogador poderá consultar o grande sábio Albert Sócrates, o ancião zoroastra.\n
• Não é proibido pesquisar no Google.\n
• Cada erro te leva ao ínicio da fase(ou não).
''')

    Looping()


while True:
    print(blue + '\n\nDigite uma opção para prosseguir.\n' + reset)
    print(Blue + '''[1] - REGRAS                             
[2] - COMEÇAR O JOGO
[3] - OBJETIVO
[4] - SAIR 
  ''' + reset)
    resposta_user = (input(green + "Selecione uma opção: " + reset))

    if resposta_user.strip() == "1":
        Regras()
    elif resposta_user.strip() == "2":
        Fase1()
    elif resposta_user.strip() == "3":
        Objetivo()
    elif resposta_user.strip() == "4":
        sleep(0.03)
        print(green + "\nSAINDO...\n")

        exit()

    else:
        os.system('clear')
