import sys

from utils.termdraw import moldura, get_terminal_size


def setup_function(function):
    print("setting up %s" % function)


def test_change_terminal_size(capsys):
    with capsys.disabled():
        sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=24, cols=80))


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
    assert tamanho_terminal == ('24', '80')
