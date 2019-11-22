"""
docstring
"""
import solver


def test_plus():
    """

    :return:
    """
    assert solver.solve("2+2") == 4


def test_minus():
    """

    :return:
    """
    assert solver.solve("2-2") == 0


def test_mult():
    """

    :return:
    """
    assert solver.solve("2*2") == 4


def test_div():
    """

    :return:
    """
    assert solver.solve("2/2") == 1


def test_mult_plus():
    """

    :return:
    """
    assert solver.solve("2*2+2") == 6


def test_plus_mult():
    """

    :return:
    """
    assert solver.solve("2+2*2") == 6


def test_complex_expr():
    """

    :return:
    """
    assert solver.solve("3*2+4/2-7") == 1
