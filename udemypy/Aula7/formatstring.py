'''
Formatação de strings

Para formatar melhor as strings podemos utilizar um recurso chamado F strings e basta por um f antes da linha inicial e as variaveis entre chaves {}
ex print(f'{nome} tem {idade} anos e seu IMC é: {imc}') retorna damiao tenorio tem 30 anos e seu IMC é: 26.122448979591837

Mas e supondo que queiramos arredondar esse valor do imc para ficar mais polido? podemos após a variavel imc inserir :.2f que mostrará duas casas decimais
ex: print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}') retorna damiao tenorio tem 30 anos e seu IMC é: 26.12

Uma outra função é a format, para isso montamos o seguinte exemplo e adicionamos .format() ao final e dentro do format colacamos as variaveis na ordem que
queiramos que elas apareçam na frase

ex: print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc)) retorna damiao tenorio tem 30 anos de idade e seu IMC é: 26.12

dentro de .format(nome, idade, imc) cada valor tem um indice iniciando em 0 então se quisessemos fazer o seguinte exemplo:

print('{0} tem {1} anos de idade e seu imc é: {2:.2f}'.format(nome, idade, imc)), também retornaria o mesmo que o exemplo anterior, pois nome esta no indice 0, idade no 1 e imc o 2

podemos também enviar parametros nomeados dentro do format(), como no exemplo abaixo

print('{n} tem {i} anos de idade e seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc)) e o resultado continua sendo o mesmo


'''

nome = "damiao tenorio"
idade = 30
altura = 1.75
e_maior = idade >= 18
peso = 80
imc = peso / altura ** 2


print(nome, 'tem', idade, 'anos e seu IMC é:', imc)
print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc))

