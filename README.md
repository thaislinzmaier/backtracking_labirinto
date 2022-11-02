# backtracking_labirinto
Projeto de Complexidade de Algoritmos para a resolução de um labirinto utilizando backtracking

Utilizando um backtracking faça um programa que leia um arquivo "entrada.txt", descrevendo um labirinto na forma de uma matriz e encontre um caminho entre dois pontos do labirinto. A primeira linha do arquivo contem dois inteiros N,M descrevendo o número de linhas e o número de colunas do labirinto. A segunda linha contem 4 valores: a posição inicial (linha e coluna) e a posição final (linha e coluna) do caminho procurado. As linhas seguintes descrevem o labirinto onde o caracter 'x' representa uma parede, e o caracter 'o' representa uma casa vazia (por onde é possível passar). O exemplo abaixo mostra um possível arquivo de entrada:

4 4   // labirinto de 4 linhas e 4 colunas

0 1 2 3 // busca caminho da posição (0,1) até a posição (2,3)

o o o x  // primeira linha do labirinto 

x o o x

o o x o

x o o o

O programa deve mostrar na tela o labirinto, com o primeiro caminho encontrado, marcando o caminho com o caracter ".". Se não encontrar caminho, deve escrever uma mensagem apropriada.

o . o x    // caminho da casa (0,1) até a casa (2,3).

x . o x

o . x  .

x .  .  .
