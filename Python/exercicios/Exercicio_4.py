"""1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade."""
pessoas = [{'nome':'Pedro','idade':16,'cidade':'Poços de Caldas'},
           {'nome':'Franciele','idade':20,'cidade':'Valinhos'},
           {'nome':'Paulo','idade':30,'cidade':'São Paulo'}]

for pessoa in pessoas:
    print(f'Nome: {pessoa['nome'].ljust(10)} Idade:{str(pessoa['idade']).ljust(10)} Cidade: {pessoa['cidade']}')

"""2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário."""

for pessoa in pessoas:
    if pessoa['nome'] == 'Pedro':
        pessoa['nome'] == 'João'
    else:
        print('Pessoa não encontrada')