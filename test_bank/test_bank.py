from bank import value

def test_values():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("What's Up") == 100