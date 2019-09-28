from main import plus, minus, mul, div


def test_plus():
    assert plus(1, 1) == 2


def test_minus():
    assert minus(1, 3) == -2


def test_mul():
    assert mul(1, 3) == 3


def test_div():
    assert div(3, 3) == 1
