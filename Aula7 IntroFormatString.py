nome = 'David'
idade = 25
altura = 1.78
peso = 89
imc = peso / (altura ** 2)
ano_atual = 2021
nasc = ano_atual - idade

print(f'{nome} tem {idade} anos e {altura} de altura')
print(f'{nome} pesa {peso}kg e seu IMC é {imc:.2f}')
print(f'{nome} nasceu em {nasc}')

#
print('{} tem {} anos, {} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('O ano de nascimento de {} é {}'.format(nome, nasc))
