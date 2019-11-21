import solver


def test_plus():
    assert solver.solve("2+2") == 4


def test_minus():
    assert solver.solve("2-2") == 0


def test_mult():
    assert solver.solve("2*2") == 4


def test_div():
    assert solver.solve("2/2") == 1


def test_mult_plus():
    assert solver.solve("2*2+2") == 6


def test_plus_mult():
    assert solver.solve("2+2*2") == 6


def test_complex_expr():
    assert solver.solve("3*2+4/2-7") == 1