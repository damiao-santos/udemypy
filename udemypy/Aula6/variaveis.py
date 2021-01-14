'''
Variaveis em Python

São locais designados na memoria do computador em que salvamos informações, para criar uma variavel damos um nome a ela
e utilizamos o = que quando utilizado sozinho é um operador de atribuição, ou seja, ele atribui(insere) o valor na
variavel

ex: nome = "damiao tenorio"
print(nome) retorna damiao tenorio

Por ser uma linguagem de tipagem dinamica, podemos inserir qualquer valor em uma variavel que ela assume o tipo
do valor inserido

ex:
nome = "damiao tenorio"
print(nome, type(nome)) retorna damiao tenorio <class 'str'>

nome = 123456
print(nome, type(nome)) retorna 123456 <class 'int'>

exemplos:

nome = "damiao tenorio"
idade = 30
altura = 1.75
e_maior = idade >= 18

print('Nome:', nome)  Nome: damiao tenorio
print('Idade:', idade)  Idade: 30
print('Altura:', altura)  Altura: 1.75
print('Maior de idade?', e_maior)  Maior de idade? True

Variaveis devem iniciar com letras, podem conter numeros mas não podem inicar com eles, em caso de nome composto
utilizar o _ para separar os nomes e as letras devem ser minusculas

Podemos usar as variaveis em operações aritimeticas se elas tiverem valores inteiros ou float armazenado nela

ex: nome = "damiao tenorio"
idade = 30
altura = 1.75
e_maior = idade >= 18

print( altura * idade) retorna 52.5

Para declarar um valor booleano explicito como True ou False dentro da variavel a primeira letra deve ser maiuscula

ex: maior = True
    menor = False

#exercicio calcula o IMC
nome = "damiao tenorio"
idade = 30
altura = 1.75
e_maior = idade >= 18
peso = 80
imc = peso / altura ** 2


print(nome, 'tem', idade, 'anos e seu IMC é:', imc) retorna damiao tenorio tem 30 anos e seu IMC é: 26.122448979591837


'''

#exercicio calcula o IMC
nome = "damiao tenorio"
idade = 30
altura = 1.75
e_maior = idade >= 18
peso = 80
imc = peso / altura ** 2


print(nome, 'tem', idade, 'anos e seu IMC é:', imc)
