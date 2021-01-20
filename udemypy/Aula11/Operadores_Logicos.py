'''
Operadores Logicos

and - significa 'e' e é usada para comparar duas coisas para ser true ambas devem ser True, se qualquer uma das
comparações forem falsas, ele retorna False

ex: comparacao1 and comparacao2

or - significa ou e é necessario apenas um dos lados ser verdadeiro para retornar verdadeiro

ex: comp1 or comp2

not - ele nao precisa de duas expressões, apenas de uma e ele é chamado de operador de inversão ou inversor. Pois
ele inverte o valor

Ex: a = 2
b = 3

if b > a:
    print('B é maior que A')
else:
    print('A maior que B')

retorna B maior que A, porém caso insira o not:

a = 2
b = 3

if not b > a:
    print('B é maior que A')
else:
    print('A maior que B')

Retorna A maior que B

podemos utiliza-lo também com variaveis vazias

a = ''
b = 0

if not a:
    print('Preencha valor de A')

in - verifica se algo esta presente na variavel ou na expressão

nome = 'damiao'

if 'da' in nome:
    print('lindao') retorna essa resposta
else:
    print('nao da nao')


not in - ele é o inversor do in

nome = 'damiao'

if 'da' not in nome:
    print('lindao')
else:
    print('nao da nao') retorna essa resposta

exemplificação -  verificação de usuario

usuario = input('nome de usuario: ')
senha = input('senha do usuario: ')

usuario_bd = 'damiao'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('logou')
else:
    print('usuario ou senha invalido')


'''



