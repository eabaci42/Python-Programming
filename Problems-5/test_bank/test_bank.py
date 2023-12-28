from bank import value


def main():
    test_upper()
    test_lower()
    test_mix()


def test_upper():
    assert value("Hello".upper()) == 0
    assert value("Hello, Newman".upper()) == 0
    assert value("How you doing?".upper()) == 20
    assert value("What's happening?".upper()) == 100


def test_lower():
    assert value("Hello".lower()) == 0
    assert value("Hello, Newman".lower()) == 0
    assert value("How you doing?".lower()) == 20
    assert value("What's happening?".lower()) == 100


def test_mix():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100
