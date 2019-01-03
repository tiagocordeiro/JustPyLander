from unittest import TestCase
from unittest.mock import patch
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from app import intro
from utils.termdraw import moldura, get_terminal_size, go_last_row, Marquee


class TestGame(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_moldura_simples(self, mock_stdout):
        moldura(2, 1, 8, 15, 'Widgets', shadow=True)
        out = mock_stdout.getvalue()
        f = open("tests/mocks/mock_moldura_simples.txt", "w+")
        f.write(out)
        f.close()

        fread = open("tests/mocks/mock_moldura_simples.txt", "r")
        mock_moldura_simples = fread.read()

        self.assertEqual(out, mock_moldura_simples)

    def test_get_terminal_size(self):
        tamanho_terminal = get_terminal_size()
        self.assertIsNotNone(tamanho_terminal)

    def test_terminal_col_size(self):
        tamanho_terminal = get_terminal_size()
        self.assertGreaterEqual(int(tamanho_terminal[1]), 80)

    def test_terminal_lin_size(self):
        tamanho_terminal = get_terminal_size()
        self.assertGreaterEqual(int(tamanho_terminal[0]), 24)

    def test_moldura_simples_muito_grande(self):
        colunas_terminal = int(get_terminal_size()[1])
        colunas_moldura = colunas_terminal + 10
        with self.assertRaises(Exception) as excinfo:
            moldura(2, 1, 8, colunas_moldura, 'Widgets', shadow=True)

        self.assertEqual(
            str(excinfo.exception),
            f'A coluna final <cf>, não pode ser maior que: {colunas_terminal}'
        )

    @patch('sys.stdout', new_callable=StringIO)
    def test_go_last_row(self, mock_stdout):
        go_last_row()
        out = mock_stdout.getvalue()

        # Mock stdout builder ;)
        f = open("tests/mocks/mock_last_row.txt", "w+")
        f.write(out)
        f.close()

        fread = open("tests/mocks/mock_last_row.txt", "r")
        mock_last_row = fread.read()

        self.assertEqual(out, mock_last_row)

    def test_marquee(self):
        animacao = Marquee()
        animacao.data = "Widgets "
        animacao.width = 5
        animacao.linha = 12
        animacao.coluna = 6
        self.assertEqual(animacao.data, "Widgets ")

    @patch('sys.stdout', new_callable=StringIO)
    def test_game_intro(self, mock_stdout):
        intro()
        out = mock_stdout.getvalue()

        # Mock stdout builder ;)
        f = open("tests/mocks/mock_game_intro.txt", "w+")
        f.write(out)
        f.close()

        fread = open("tests/mocks/mock_game_intro.txt", "r")
        mock_game_intro = fread.read()

        self.assertEqual(out, mock_game_intro)
