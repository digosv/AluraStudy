
resposta = int(input('Digite um número inteiro: '))

if resposta % 2 == 0:
    print('par')
else: 
    print('impar')

resposta_2 = int(input('Qual é a sua idade?\n Resposta:  '))

if  0 < resposta_2 <= 12:
    print('Criança: 0 a 12 anos')
elif 13 <= resposta_2 <= 18:
    print('Adolescente: 13 a 18 anos')
elif resposta_2 >= 18:
    print('Acima de 18 anos')
else:
    print('Resposta invalida')

usuario = 'derikin'
senha = 'larissa'

resp_usuario = str(input('Digite Usuario: '))
resp_senha = str(input('Digite a senha: '))

if resp_usuario == usuario and resp_senha == senha:
    print('Logado')
else:
    print('Alguma informação está incorreta, por favor, tente novamente')


x = int(input('Digite a coordenada do X: '))
y = int(input('Digite a coordenada do Y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante')
elif x < 0 and y > 0:
    print('Segundo Quadrante')
elif x < 0 and y < 0:
    print('Terceiro Quadrante')
elif x > 0 and y < 0:
    print('Quarto Quadrante')
else:
    print('Eixo')