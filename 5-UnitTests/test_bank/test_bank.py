from bank import value


def test_0():
    assert value("hello") == "$0"
    assert value("Hello") == "$0"
    assert value("Hello!") == "$0"
    assert value("Hello there!") == "$0"


def test_20():
    assert value("hey") == "$20"
    assert value("Hey") == "$20"
    assert value("Hey!") == "$20"
    assert value("Hey there!") == "$20"


def test_100():
    assert value("wassup") == "$100"
    assert value("Wassup") == "$100"
    assert value("Wassup!") == "$100"
    assert value("Wassup there!") == "$100"
