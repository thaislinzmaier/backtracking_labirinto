def valida(matriz, x, y):
    if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]) and matriz[x][y] == 'o':
        return True
    else:
        return False

def acha_caminho(matriz, comeco, final):
    def backtrack(x, y):
        if [x, y] == final:
            return True
        if valida(matriz, x, y):
            matriz[x][y] = '.'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                novo_x, novo_y = x + dx, y + dy
                if backtrack(novo_x, novo_y):
                    return True
            matriz[x][y] = 'o'
        return False
    if backtrack(comeco[0], comeco[1]):
        for linha in matriz:
            print(" ".join(linha))
    else:
        print("Caminho não encontrado.")

if __name__ == "__main__":
    with open(r"entrada.txt", "r") as file:
        n, m = map(int, file.readline().split())
        comeco_x, comeco_y, final_x, final_y = map(int, file.readline().split())
        labirinto = []
        for i in range(n):
            linha = list(file.readline().split(' '))
            labirinto.append(linha)
    acha_caminho(labirinto, [comeco_x, comeco_y], [final_x, final_y])
