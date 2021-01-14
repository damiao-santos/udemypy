'''
Operadores aritmeticos

+ -> soma
- -> subtração
* -> multiplicação
/ -> divisão
// -> divisão inteira
** -> exponenciação
% -> resto de divisão
() -> parenteses - usado para alterar a precedencia nas contas

ex:
print(10 * 10)
print(10 + 10)
print(10 - 5)
print(10 / 2)
print(10 // 2)
print(10 % 2)

O operador de * tbm serve como operador de repetição quando usado com uma string

ex: print(10 * "10") retorna 10101010101010101010

Quando usado por duas string o simbolo de + vira um simbolo de concatenação juntando as strings

ex: print("5" + "5") ao inves de retornar 10 retorna 55 pois junta os 2 5 que são strings

outro exemplo de concatenção

print("damiao" + " " + "tenorio") retorna damiao tenorio

o operador // por ser uma divisão de numero inteiro ela arredonda o valor da divisão

ex: print(9 // 2) ao inves de retornar 4.5 retorna 4

O operador de exponenciação é o equivalente da matemática a potenciação

ex: print(2 ** 10) lê-se 2 elevado a 10 e retorna 1024

com o % obtemos o resto da divisão, ela acontece normalmente porém o resultado que será mostrado é do resto

ex: print(10 % 3) retorna 1

Os parenteses () alteram a precedencia dos operadores

ex: print(5+2*10) retorna 25 ao inves de 70 pois a multiplicação é resolvida primeiro
print((5+2)*10) retorna 70 pois primeiro será executada a adição depois a multiplicação alterando a precedencia

Precedência dos Operadores Aritméticos

Assim como aprendemos na matemática, operadores têm uma certa precedência que pode ser alterada usando os parênteses
(como descrito na aula anterior).

Abaixo, segue uma lista mais precisa de quais operadores tem maior prioridade na hora de realizar contas mais complexas
(de maior para menor precedência).

    ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

    ** - Depois vem a exponenciação

    * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

    +  - - Por fim, soma e subtração

Contas com operadores de mesma precedência são realizadas da esquerda para a direita.

Observação: existem muito mais operadores do que estes em Python e todos eles também têm precedência,
você pode ver a lista completa em https://docs.python.org/3/reference/expressions.html#operator-precedence
(sempre utilize a documentação oficial como reforço caso necessário).

Caso tenha dúvidas, faça testes com números. Por exemplo, olhe para essa conta e tente decifrar como chegar
no resultado: 2 + 5 * 3 ** 2 - (23.5 + 23.5) (o resultado é 0.0).
Para isso você precisa realizar as contas com maior precedência primeiro.

'''

print((5+2)*10)

