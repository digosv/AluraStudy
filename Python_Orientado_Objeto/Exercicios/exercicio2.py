class Musica:
    def __init__(this, nome, artista, duracao):
        this.nome = nome
        this.artista = artista
        this.duracao = duracao 

class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        return f'Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}'

civic = Carro('Civic G7', 'Preto', 2006)
print(civic)

class Restaurante:
    def __init__(self, nome, categoria, horario, tema):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.horario = horario
        self.tema = tema
        

boteco_do_bene = Restaurante('Boteco Do Bene', 'Boteco', '16 as 23', 'Comida de Boteco')

class Restaurante_japones:
    def __init__(self, nome, categoria, horario='16 as 23', tema='japao'):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.horario = horario
        self.tema = tema

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.horario} | {self.tema}'


japa = Restaurante_japones('naruto','comida japonesa')

print(japa)

class CLiente:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

rodrigo = CLiente('Rodrigo', 20, 123123131, 'rodrigo@gmail.com')

print(vars(rodrigo))


        