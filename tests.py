import os


def moldura(li, ci, lf, cf, titulo='', shadow=False):
    """
    Cria moldura.

    Args:
        li: Linha inicial.
        ci: Coluna inicial.
        lf: Linha final.
        cf: Coluna final
        titulo: Texto do cabeçalho
        shadow: Sombra

    Returns:
        Retorna uma moldura.

    """
    colunas = cf - ci
    linhas = lf - li
    term_rows, term_columns = os.popen('stty size', 'r').read().split()
    
    if colunas > int(term_columns):
        raise Exception(f'A coluna final <cf>, não pode ser maior que: {term_columns}')

    print("\033[" + str(li) + ";" + str(ci) + "H╔" + "═" * (colunas - 2) + "╗")

    lateral_borda = li
    for linha in range(linhas):
        lateral_borda += 1
        print("\033[" + str(lateral_borda) + ";" + str(ci) + "H║" + " " * (colunas - 2) + "║")
    
    print("\033[" + str(lateral_borda) + ";" + str(ci) + "H╚" + "═" * (colunas - 2) + "╝")

    if titulo:
        tamanho_titulo = len(titulo)
        espaco_titulo = colunas - tamanho_titulo
        posicao_titulo = (espaco_titulo / 2) + ci

        print("\033[" + str(li + 1) + ";" + str(int(posicao_titulo)) + "H" + titulo)
        print("\033[" + str(li + 2) + ";" + str(ci) + "H╠" + "═" * (colunas - 2) + "╣")

    lateral_sombra = li
    if shadow:
        for linha in range(linhas):
            lateral_sombra += 1
            print("\033[" + str(lateral_sombra) + ";" + str(int(cf)) + "H█")
        
        print("\033[" + str(lateral_sombra + 1) + ";" + str(int(ci + 1)) + "H" + "█" * colunas)
    
    # print("\033[" + str(int(linhas) + 3) + ";0H ")
    go_last_row()


def go_last_row():
    term_rows, term_columns = os.popen('stty size', 'r').read().split()
    print("\033[" + str(int(term_rows) - 1) + ";0H ")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    moldura(1, 1, 10, 142, "Título da Janela")
    
    moldura(11,5,15,20, 'Widgets', shadow=True)


    # TesteString = """
    # ▀	▁	▂	▃	▄	▅	▆	▇	█	▉	▊	▋	▌	▍	▎	▏
    # ▐	░	▒	▓	▔	▕	▖	▗	▘	▙	▚	▛	▜	▝	▞	▟
    # ░▒▓
    # """

    # print(TesteString)
    # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    # print('\x1b[33;32m' + 'Success!' + '\x1b[0m')
    # print('\x1b[33;92m' + 'Success!' + '\x1b[0m')
    # print('\x1b[33;4m' + 'Success!' + '\x1b[0m')

    # print('\x1b[0;32;40m' + 'Success!' + '\x1b[0m')
    # print('\x1b[1;32;40m' + 'Success!' + '\x1b[0m')
    # print('\x1b[2;32;40m' + 'Success!' + '\x1b[0m')
    # print('\x1b[3;32;40m' + 'Success!' + '\x1b[0m')

    # print('\033[32m' + 'Success!!' + '\x1b[0m')
    # print('\033[92m' + 'Success!!' + '\x1b[0m')
    