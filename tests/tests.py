import sys

from utils.termdraw import moldura


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
