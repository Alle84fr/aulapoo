1. REVISANDO

modulo - arquivos que possui parte do programa

dividir módulos em pastas/PACOTES - separa os módulos 

2. biblioteca

módulos, geralmente organizada em pacotes que contém funcionalidades  reutilizáveis

2. 1. TIPOS

- integradas

- terceiros

- próprias/nossas

2. 2. PRÓPRIAS:

como saber quais bibliotecas temos?

pasta vazia - new terminal - digite python ou python 3 (caso foi o 1°)

dir() - mostra os modolos integrados no py

import mome do modulo, ex math

depois dá dir()

dir +- naquele diretório está disponível

achar os arquivos, onde o módulo está definido, oferecido nome._ _file__ para achar. O nome do arquivo se torna o módulo que é o mesmo nome do arquivo

math foi definido em linguagem de baixo nível, outra linguagem, que não py.

O cód só tem a interface de py, como reulização de cód, como melhor desempenho da outra linguagem.

linguagem de baixo nível define como fazer

linguagem de alto nível define o que fazer
e a linguagem faz

para fechar exit()

para importar modúlo e suas classes, para usar

lembre-se de instânciar as classe (importar as funções no módulo principal)

para acessar o nome do módulo

2. 3. Funcionalidade dos módulos

fará um print

meu_módulo

2. 4. importar módulo

procura em conjuntos de pastas

import sys

comando sys.path - procura o módulos nas pastas

nome do mod pode usar apelidos

ex numpy que é np

ex pandas que é pd

ex calculadora trigonométrica que precisa de seno coseno e tangente

from  math import sin, cos, tan

aqui ocupa menos memórias que deixa mais rápido  