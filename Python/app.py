import os

#restaurantes = []

# Estrutura de Dicionario:
restaurantes = [{'nome':'Bigoboo', 'categoria':'Japones', "ativo":True},
                {'nome':'SushiO', 'categoria':'Japones', "ativo":False},
                {'nome':'Subway', 'categoria':'Lanche', "ativo":True}]

def voltar():
    input('Digite uma tecla para voltar para o menu principal...')
    main()

def inicio_programa(text):
    os.system('cls')
    linha = '*' * (len(text))
    print(linha)
    print(text)
    print(linha)


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
    print('3. Alternar Estado Restaurantes')
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
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    inicio_programa('Encerrando Programa')


def cadastrar_restaurante():
    inicio_programa('Cadastro de Novos Restaurantes')
    
    nome_do_restaurante = input('Digite o restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_restaurante = {'nome':nome_do_restaurante,'categoria':categoria_restaurante,'ativo':False}

    restaurantes.append(dados_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n')

    voltar()


def listar_restaurantes():

    inicio_programa('Listando Restaurantes')
    print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado'  if restaurante['ativo'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)}')
    
    voltar()

def ativar_restaurantes():
    inicio_programa('Ativar Restaurante.')

    input('Digite o nome do seu restaurante: ')
    voltar()

def alternar_estado_restaurante():
    inicio_programa('Alternando Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {restaurante["nome"]} foi ativado com sucesso' if restaurante['ativo'] else f'\nO restaurante {restaurante["nome"]} foi desativado com sucesso.'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado...')


    voltar()


def opcao_invalida():
    print('Opção inválida\n')
    voltar()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()

