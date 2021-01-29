'''
Len - Quantidade de Caracteres

vamos ver como contar quantos caracteres dentro de uma string, para isso utilizaremos a função len() do python
Funciona com string e outros tipos de dados, porém nao funciona com tipos numericos

Ex: user = input('Digite seu usuario: ')

qtd_caracteres =  len(user)

print(user, qtd_caracteres, type(qtd_caracteres)) retorna damiao 6 <class 'int'>

e se quisessemos verificar se o colaborador digitou uma quantidade minima adequada

user = input('Digite seu usuario: ')

qtd_caracteres =  len(user)

if qtd_caracteres < 6:
    print('Precisa digitar pelo menos 6 caracteres')
else:
    print('cadastrado com sucesso')

Podemos pegar tbm duas string e somar as strings delas e ver a quantidade

string1 = input('digite algo: ')
string2 = input('digite outra coisa: ')

print(f'a quantidade de caracteres foi {len(string1) + len(string2)}')


Em python tudo é um objeto e podemos ver metodos atrelados a ele, então com isso a função len() apenas chama o
metodo __len()__ que sria o mesmo que string1.__len__(), então basicamente ao realizar print('string1') é o mesmo
que executar print(string1.__len__())


'''

string1 = input('digite algo: ')
string2 = input('digite outra coisa: ')

print(f'a quantidade de caracteres foi {len(string1) + len(string2)}')

string1.__len__()


