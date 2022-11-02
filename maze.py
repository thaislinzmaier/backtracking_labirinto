def imprime_solucao(solucao):
     
    for i in solucao:
        for j in i:
            print(str(j) + " ", end ="")
        print("")
 
def a_salvo(labirinto, x, y):
     
    if x != 'x' and x < N and y != 'x' and y < N and labirinto[x][y] == 'o':
        return True
     
    return False
 
def resolve_labirinto(labirinto):
     
    solucao = [ [ 'o' for j in range(4) ] for i in range(4) ]
     
    if resolve_labirinto_ate(labirinto, 0, 0, solucao) == False:
        print("Solução não existe");
        return False
     
    imprime_solucao(solucao)
    return True
     
def resolve_labirinto_ate(labirinto, x, y, solucao):
     
    if x == N - 1 and y == N - 1:
        solucao[x][y] = '.'
        return True
         
    if a_salvo(labirinto, x, y) == True:
        solucao[x][y] = '.'
         
        if resolve_labirinto_ate(labirinto, x + 1, y, solucao) == True:
            return True
             
        if resolve_labirinto_ate(labirinto, x, y + 1, solucao) == True:
            return True
   
        solucao[x][y] = 0
        return False
 

if __name__ == "__main__":

    lista_posicoes = []

    with open(r'G:\Meu Drive\Ciência da Computação\2022 4\Complexidade de Algoritmos\TDES\Maze\entrada.txt', 'r') as arquivo:
        arquivo_txt = arquivo.read()
        N = int(arquivo_txt[0])
        lista_posicoes.append(arquivo_txt[12:48])


    lista_posicoes_tratada =  [x.replace('\n', '') for x in lista_posicoes]
    
    lista_posicoes_tratada = lista_posicoes_tratada[0].split(" ")

    lista_labirinto = []

    for i in lista_posicoes_tratada:
        if i == 'xx' or i == 'xo' or i == 'ox':
            a = [*i]
            lista_labirinto.append(a[0])
            lista_labirinto.append(a[1])
        else:
            lista_labirinto.append(i)


    comeco = 0
    fim = 16
    pulos = 4
    labirinto = []
    for i in range(comeco, fim, pulos):
        x = i
        labirinto.append(lista_labirinto[x:x+pulos])

    for i in labirinto:
        print(i)

    resolve_labirinto(labirinto)