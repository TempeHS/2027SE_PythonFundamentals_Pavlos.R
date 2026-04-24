from twttr import shorten


def test_lowercase():
    assert shorten("ddf") == "ddf"
    assert shorten("hello") == "hll"
    assert shorten("dauin") == "dn"


def test_uppercase():
    assert shorten("Ddf") == "Ddf"
    assert shorten("HEllo") == "Hll"
    assert shorten("dauiN") == "dN"


def test_y():
    assert shorten("sky") == "sky"
    assert shorten("Sky") == "Sky"
    assert shorten("y") == "y"
