'''
Em python string é definida como str, string é todo texto dentro de aspas, seja dupla ou simples, basicamente string é uma cadeia de caracter

python é uma linguagem de tipagem dinamica

Para colocar uma aspas dentro de uma string basta usar aspas diferentes para que o compilador não entenda como finalização. EX:
print('esta é uma "string"(str).') o testo começa com uma aspas simples e o objeto que queremos por entre aspas no texto esta em aspas duplas

Uma outra maneira de realizar isso é usar um caracterer de escape como a \, o problema é que o codigo fica "feio" e confuso. ex:
print("esta é uma \"string\"(str).")

\n quebra a linha, caso não queira executar comandos dentro da string basta por um r antes dela que ele indicada ao compilador que nenhum comando ali dentro deve ser executado

ex: print(r"esta é uma \n (str).") retorna esta � uma \n (str).
mas não é indicado trabalhar desta forma, a melhor forma são as aspas




'''

print(r"esta é uma \n (str)."
