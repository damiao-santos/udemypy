'''
*Criar Variaveis para nome(str), idade(int),
*altura(float), e peso(float) de uma pessoa
*criar uma variavel com o ano atual(int)
*obter o ano de nascimento da pessoa(baseado na idade e ano atual)
*obter o IMC da pessoa com 2 casas decimais(peso e na altura da pessoa)
*exibir um texto com todos os valores na tela usando F-Strings

'''

nome = 'Eulina Gomes'
idade = 58
altura = 1.60
peso = 90
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2


print(f'{nome} tem {idade} anos e {altura} de altura e pesa {peso}.\nO IMC de {nome} é: {imc:.2f}\n{nome} nasceu em {ano_nascimento}')

#ou

print(f'{nome} tem {idade} anos e {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é: {imc:.2f}')
print(f'{nome} nasceu em {ano_nascimento}')
