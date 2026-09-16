Esse arquivo serve para anotações.

Essa função dentro de uma classe, define como ela é mostrada com um print(class)
def **str**(self):
return f'Nome: {self.nome}, Categoria: {self.categoria}, Status: {self.ativo}'

nessas classes posso usar this ao inves de self, ou qualquer outro nome. exemplo:

class Restaurante:
def **init**(this, nome, categoria):
this.nome = nome
this.categoria = categoria
this.ativo = False
