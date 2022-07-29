from bank import value

def test_starts_w_h():
    assert value("hi") == 20

def test_starts_w_hello():
    assert value("Hello") == 0

def test_starts_w_other():
    assert value("deneme") == 100