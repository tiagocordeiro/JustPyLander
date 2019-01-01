import os
import sys
import time


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
        Imprime uma moldura.

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

    go_last_row()


def go_last_row():
    term_rows, term_columns = os.popen('stty size', 'r').read().split()
    print("\033[" + str(int(term_rows) - 1) + ";0H ")


class Marquee:
    def __init__(self):
        self.data = ""
        self.width = 0
        self.linha = ""
        self.coluna = ""

    def animate(self):
        try:
            while True:
                sys.stdout.write("\033[?25l")
                for x in range(0, self.width):
                    time.sleep(0.1)
                    msg = "{}{}".format(" " * x, self.data)
                    sys.stdout.write(f"\033[{self.linha};{self.coluna}H{msg}")
                    sys.stdout.flush()

                for x in range(self.width, 0, -1):
                    time.sleep(0.1)
                    msg = "{}{}".format(" " * x, self.data)
                    sys.stdout.write(f"\033[{self.linha};{self.coluna}H{msg}")
                    sys.stdout.flush()
        except KeyboardInterrupt:
            sys.stdout.write("\033[?25h")
            print("Exiting")


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    moldura(1, 1, 10, 80, "Título da Janela")

    moldura(11, 5, 15, 20, 'Widgets', shadow=True)

    time.sleep(.5)

    # Marquee
    animacao = Marquee()
    animacao.data = "Widgets "
    animacao.width = 5
    animacao.linha = 12
    animacao.coluna = 6

    sys.stdout.flush()
    animacao.animate()
