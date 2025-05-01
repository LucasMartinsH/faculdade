from app import soma, subtrai

def test_soma_positivos():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-1, -2) == -3

def test_subtrai_positivos():
    assert subtrai(5, 3) == 2

def test_subtrai_negativos():
    assert subtrai(-5, -3) == -2

def test_soma_zero():
    assert soma(0, 0) == 0