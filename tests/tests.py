import sys

import pytest

from app import intro
from utils.termdraw import moldura, get_terminal_size, go_last_row, Marquee


def setup_function(function):
    print("setting up %s" % function)


def test_saida_terminal(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print("next")
    out, err = capsys.readouterr()
    assert out == "next\n"


def test_moldura_simples(capsys):
    moldura(2, 1, 8, 15, 'Widgets', shadow=True)
    out, err = capsys.readouterr()

    # Mock stdout builder ;)
    f = open("tests/mocks/mock_moldura_simples.txt", "w+")
    f.write(out)
    f.close()

    fread = open("tests/mocks/mock_moldura_simples.txt", "r")
    mock_moldura_simples = fread.read()

    assert out == mock_moldura_simples
    assert err == ''


def test_get_terminal_size():
    tamanho_terminal = get_terminal_size()
    print("Tamanho do terminal: ", tamanho_terminal)
    assert tamanho_terminal is not None


def test_terminal_col_size():
    tamanho_terminal = get_terminal_size()
    assert int(tamanho_terminal[1]) >= 80


def test_terminal_lin_size():
    tamanho_terminal = get_terminal_size()
    assert int(tamanho_terminal[0]) >= 24


def test_moldura_simples_muito_grande():
    colunas_terminal = int(get_terminal_size()[1])
    colunas_moldura = colunas_terminal + 10
    with pytest.raises(Exception) as excinfo:
        moldura(2, 1, 8, colunas_moldura, 'Widgets', shadow=True)
    assert str(excinfo.value) == f'A coluna final <cf>, não pode ser maior que: {colunas_terminal}'


def test_go_last_row(capsys):
    go_last_row()
    out, err = capsys.readouterr()

    # Mock stdout builder ;)
    f = open("tests/mocks/mock_last_row.txt", "w+")
    f.write(out)
    f.close()

    fread = open("tests/mocks/mock_last_row.txt", "r")
    mock_last_row = fread.read()

    assert out == mock_last_row
    assert err == ""


def test_marquee():
    animacao = Marquee()
    animacao.data = "Widgets "
    animacao.width = 5
    animacao.linha = 12
    animacao.coluna = 6
    assert animacao.data == "Widgets "


def test_game_intro(capsys):
    intro()
    out, err = capsys.readouterr()

    # Mock stdout builder ;)
    f = open("tests/mocks/mock_game_intro.txt", "w+")
    f.write(out)
    f.close()

    fread = open("tests/mocks/mock_game_intro.txt", "r")
    mock_game_intro = fread.read()

    assert err == ''
    assert out == mock_game_intro
