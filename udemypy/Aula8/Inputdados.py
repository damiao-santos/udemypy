'''
Entrada de Dados em Python

Para solicitar o input de dados em python temos uma função chamada input(), e ela recebe uma string e essa string
aparece para o usuario na tela

ex: input("Qual seu nome? ")

Podemos atribui-lo a uma variavel para quando o usuario inserir um dado ele seja guardado

ex: nome = input("Qual seu nome? ")

o input sempre vai retornar uma string mesmo que você insira um numero

e se quisessemos que o programa nos retornasse o ano de nascimento

nome = input("Qual seu nome? ")
idade = input('Qual a sua idade? ')
nascimento = 2021-idade

print()
print(f'{nome} tem {idade} anos')

retornaria erro, pois o input retorna string e não deixa fazer uma conta entre string e inteiro
a forma de contorna isso é realizar um casting de variavel

nome = input("Qual seu nome? ")
idade = input('Qual a sua idade? ')
nascimento = 2021 - int(idade) #cast transformando idade que era string em int

print()
print(f'{nome} tem {idade} anos'
        f' {nome} nasceu em {nascimento}')

Como novo exemplo vamos fazer uma calculadora que soma apenas

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

soma = int(numero_1) + int(numero_2)

print(f'a soma dos dois números é: {soma}')

é possivel fazer o cast tbm no input

numero_1 = int(input('Digite um numero: '))

'''

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite outro numero: ')

soma = int(numero_1) + int(numero_2)

print(f'a soma dos dois números é: {soma}')