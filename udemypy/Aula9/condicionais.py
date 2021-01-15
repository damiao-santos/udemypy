'''
Condições IF ELIF e ELSE e Booleanos

Para fazer uma comparação em python utilizamos estas 3 estruturas que seriam equivalente a se(if) senao, se(elif)
e senao(else)

Por convenção em python utilizamos 4 espaços para hierarquia e ele faz isso de forma automatica

ex: if True:
    print('verdadeiro')

O print tem 4 espaços desde a lateral para simbolizar que esta dentro do bloco if, para indicar que a expressão de
baixo so vai executar se a de cima foi verdadeira.

ao tirar os espaços ele perde a hierarquia como no exemplo abaixo

if False:
    print('verdadeiro')

print('a minha expressão nao é verdadeira') que retorna o que esta nesse print na tela.

o else entra quando precisamos executar a expressão e o if não for verdadeiro e assim ele executaria uma segunda ação
e o else nao pode ser usada sozinha, ela depende de um if para existir

ex: if False:
    print('verdadeiro')
else:
    print('não é verdadeiro') ele executa esse bloco de baixo

elif é a abreviação de else if e é usada se queremos manter uma cadeia de if antes de um else para avaliar outras
condicionais

if False:
    print('verdadeiro')
elif True:
    print('buga buga')
else:
    print('não é verdadeiro')


'''

if False:
    print('verdadeiro')
elif True:
    print('buga buga')
else:
    print('não é verdadeiro')

