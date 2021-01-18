'''
Operadores Relacionais

== - igual a
> - maior que
>= - maior ou igual
<  - menor que
<= - menor ou igual
!= - diferente de

Eles são feitos para realizar comparações ou relações entre dados, sempre que forem executados eles retornam um
valor booleano ( true ou false)

caso queiramos fazer uma checagem se uma idade é maior que 18 para pegar emprestimo

ex: name = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))
idade_limite = 18

if idade >= idade_limite:
    print(f'{name} pode pegar emprestimo')
else:
    print(f'{name} não pode emprestimo')


e se quisermos limitar entre 20 e 30 anos?

name = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

#limite para emprestimo
idade_menor = 20 #muito jovem
idade_maior = 30 #muito velho

if idade >= idade_menor and idade <= idade_maior:
    print(f'{name} pode pegar emprestimo')
else:
    print(f'{name} não pode emprestimo')

'''

name = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

#limite para emprestimo
idade_menor = 20 #muito jovem
idade_maior = 30 #muito velho

if idade >= idade_menor and idade <= idade_maior:
    print(f'{name} pode pegar emprestimo')
else:
    print(f'{name} não pode emprestimo')



