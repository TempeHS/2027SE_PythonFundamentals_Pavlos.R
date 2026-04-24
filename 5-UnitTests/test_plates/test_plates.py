from plates import check_is_valid


def test_length():
    assert check_is_valid("AB1234") == True
    assert check_is_valid("AB12") == True
    assert check_is_valid("AB") == True
    assert check_is_valid("AB1") == True
    assert check_is_valid("A") == False
    assert check_is_valid("AB12345") == False


def test_letter():
    assert check_is_valid("AB1234") == True
    assert check_is_valid("AB123") == True
    assert check_is_valid("A1B23") == False
    assert check_is_valid("12AB3") == False


def test_value():
    assert check_is_valid("AB1234") == True
    assert check_is_valid("2AB12") == False
    assert check_is_valid("1B123") == False
    assert check_is_valid("A3B23") == False


def test_num():
    assert check_is_valid("AB1234") == True
    assert check_is_valid("AB12") == True
    assert check_is_valid("A1B23") == False
    assert check_is_valid("12AB3") == False
    assert check_is_valid("AB120") == True
    assert check_is_valid("AB103") == True
    assert check_is_valid("A0B13") == False
