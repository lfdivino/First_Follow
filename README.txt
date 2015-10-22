TRABALHO DE COMPILADORES - UNIFEI

autor: Luiz Felipe do Divino


Descrição:

	Esta aplicação foi criada com o intuito de aplicar os algoritmos para descobrir o First e o Follow de gramáticas setadas no arquivo gramatica.txt


Exemplo:

gramatica:
S → XYZ
X → aXb | ε
Y → cYZcX | d
Z → eZYe | f

First(X) = {a, ε}	Follow(X) = {c, d, b, e, f}
First(Y) = {c, d}	Follow(Y) = {e, f}
First(Z) = {e, f}	Follow(Z) = {$, c, d}
First(S) = {a, c, d}    Follow(S) = {$}