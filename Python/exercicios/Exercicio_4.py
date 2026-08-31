"""1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade."""
pessoas = [{'nome':'Pedro','idade':16,'cidade':'Poços de Caldas'},
           {'nome':'Franciele','idade':20,'cidade':'Valinhos'},
           {'nome':'Paulo','idade':30,'cidade':'São Paulo'}]

for pessoa in pessoas:
    print(f'Nome: {pessoa["nome"].ljust(10)} Idade:{str(pessoa["idade"]).ljust(10)} Cidade: {pessoa["cidade"]}')

"""2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário."""

pessoa['nome'] = 'Felipe'

for pessoa in pessoas:
    print(f'\nNome: {pessoa["nome"].ljust(10)} Idade:{str(pessoa["idade"]).ljust(10)} Cidade: {pessoa["cidade"]}')


"""3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados."""

numeros_quadrados = [{"numero":1,"quadrado":1},{"numero":2,"quadrado":4},{"numero":3,"quadrado":9},{"numero":4,"quadrado":16},{"numero":5,"quadrado":25}]

numeros_quadrados_2 = {x:x**2 for x in range(1,6)}
print(numeros_quadrados_2)

for numero in numeros_quadrados:
    print(f"{numero['numero']}:{numero['quadrado']}")


"""4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário."""

pessoa = {'nome':'Paulo', 'idade':20}

if "nome" in pessoa:
    print('A chave nome existe no dicionário')
else:
    print('A chave nome não existe no dicionário')


"""5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário."""

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)