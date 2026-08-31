import os

restaurantes = []

def voltar():
    input('Digite uma tecla para voltar para o menu principal...')
    main()
    

def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def escolher_opcao():
    

    try:
        opcao_escolhida = input('Escolha uma opção: ')
        #print(type(opcao_escolhida))
        opcao_escolhida = int(opcao_escolhida) 
        #print(type(opcao_escolhida))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    os.system('cls')
    #os.system('clear') no macbook
    print('Encerrando Programa\n')

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de Novos Restaurantes\n')
    
    nome_do_restaurante = input('Digite o restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n')

    input('Digite uma tecla para voltar para o menu principal...')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando Restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    input('Digite uma tecla para voltar para o menu principal...')
    main()

def ativar_restaurantes():
    print('Ativar restaurente')

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu inicial: ')
    main()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()

