'''
Tipos de dados primitivos

str - string - são textos "assim" ou 'assim'

int - inteiro - são numeros inteiros negativos ou positivos que não tenham ponto flutuante (0, -10, 20 e etc)

float - real\ponto flutuante - são numeros que possuem ponto flutuante, em python não é usada virgula e sim ponto para se parar casas decimais (0.7, 10.3 e etc)

bool - booleano\lógico - e um boolean só tem 2 valores ou true ou false( verdadeiro e falso)

a função type() retorna o tipo do valor indicado em seu parenteses
ex: print(type('damiao')) #retorna <class 'str'>

podemos fazer um type casting em python que é mudar o tipo de valor exibido
ex: print('damiao', type('damiao'), bool('damiao')) retorna damiao <class 'str'> True

pois ao jogar  uma string dentro de um booleano ela sempre retorna o resultado verdadeiro

print('10', type('damiao'), type(int('10'))) - retorna 10 <class 'str'> <class 'int'> e converte a string 10 para inteiro

não podemos converter nome ou ponto flutuante em inteiro, porém podemos converter um numero inteiro em ponto flutuante


'''

#print('10', type('damiao'), type(int('10')))

#exercicio

#nome
print('Damião Tenorio', type('Damião Tenorio'))

#idade
print(30, type(30))

#altura
print(1.75, type(1.75))

#maior de idade
print(30 >= 18, type(30 >= 18))



