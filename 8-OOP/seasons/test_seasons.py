from seasons import main


# Returned Dates For Correct Tests Will Need To Be Updated Before Testing
def test_data_type():
    assert main("2009-08-17") == 8779680.0
    assert main(2009 - 8 - 17) == "Wrong Input Format"
    assert main(2009.0 - 8.0 - 17.0) == "Wrong Input Format"


def test_amounts():
    assert main("2009-08-17") == 8779680.0
    assert main("2009-18-17") == "Wrong Values Inputted"
    assert main("2009-08-32") == "Wrong Values Inputted"
    assert main("2009-04-31") == "Wrong Values Inputted"
    assert main("2009-02-29") == "Wrong Values Inputted"
    assert main("2008-02-29") == 9550080.0


def test_future():
    assert main("2009-08-17") == 8779680.0
    assert main("2026-04-28") == "Can't be born in the future"
    assert main("2026-05-27") == "Can't be born in the future"
    assert main("2027-04-27") == "Can't be born in the future"
    assert main("2026-04-27") == 0.0
