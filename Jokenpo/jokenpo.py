import random
from random import choice, randint

# Escolha do computador
ai_computer = ['Pedra', 'Papel', 'Tesoura']
ai_computer_choice = choice(ai_computer)

loop = True

while loop:
    ai_computer = ['Pedra', 'Papel', 'Tesoura']
    ai_computer_choice = choice(ai_computer)
    print("Escolhi minha jogada, sua vez:")
    print(ai_computer_choice)

    print("""
    MENU:
    [1] Pedra
    [2] Papel
    [3] Tesoura
    [4] Sair    
    """)

    player_choice = str(input("Escolha sua jogada: "))
    if int(player_choice) > 4 or int(player_choice) < 1:
        print("Opcao invalida")

    match player_choice:
        case '1':
            player_choice = 'Pedra'
            match ai_computer_choice:
                case 'Pedra':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nEMPATE\n', '-=' * 10)
                case 'Papel':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nPERDEU\nHumano fraco\n', '-=' * 10)
                case 'Tesoura':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nGANHOU\nBoa escolha\n', '-=' * 10)

        case '2':
            player_choice = 'Papel'
            match ai_computer_choice:
                case 'Pedra':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nGANHOU\nBoa escolha\n', '-=' * 10)
                case 'Papel':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nEMPATE\n', '-=' * 10)
                case 'Tesoura':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nPERDEU\nHumano fraco\n', '-=' * 10)

        case '3':
            player_choice = 'Tesoura'
            match ai_computer_choice:
                case 'Pedra':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nPERDEU\nInseto\n', '-=' * 10)
                case 'Papel':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nGANHOU\nBoa escolha\n', '-=' * 10)
                case 'Tesoura':
                    print(f'\nIA     |    Sua escolha')
                    print(f'\n{ai_computer_choice} X {player_choice}')
                    print('-=' * 10, '\nEMPATE\n', '-=' * 10)
        case '4':
            player_choice = 'Sair'
            loop = False



