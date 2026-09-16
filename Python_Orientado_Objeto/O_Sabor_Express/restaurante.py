
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}' 
    
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Mario', 'Pizzaria')

# Função vars mostra a chave e o valor: 'nome': 'Praça'

Restaurante.listar_restaurante()