
class Restaurante:
    nome = ''
    categoria = ''
    ativo = True

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

print(restaurante_praca.nome)

print(f'Restaurante {restaurante_praca.nome} está ativo') if restaurante_praca.ativo == True else print(f'Restaurante {restaurante_praca.nome} está desativado.')

categoria = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print('Okay')
else:
    print('Não é Fast food a categoria')

restaurante_pizza.ativo = True
print(f'Nome Restaurante:{restaurante_praca.nome} \nCategoria Restaurante: {restaurante_praca.categoria}')