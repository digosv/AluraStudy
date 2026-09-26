
class Pessoa:

    def __init__(self, nome='', idade='', profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Ola, me chamo {self.nome} e tenho {self.idade} anos.'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return f'Ola, sou {self.nome} e meu cargo é {self.profissao}'
        else:
            return f'Ola, sou {self.nome}'

rodrigo = Pessoa('rodrigo', 20, 'Analista de Dados')
print(rodrigo)
rodrigo.aniversario()
print(rodrigo)
print(rodrigo.saudacao)


        