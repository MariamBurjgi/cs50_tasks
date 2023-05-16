from jar import Jar

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    try:
        jar = Jar("not an integer")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid capacity"

    try:
        jar = Jar(-5)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative capacity"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12
    try:
        jar.deposit(1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for deposit that exceeds capacity"
    try:
        jar.deposit("not an integer")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid deposit argument"


def test_withdraw():
    jar = Jar(8)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    try:
        jar.withdraw(1)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for withdraw that exceeds size"
    try:
        jar.withdraw("not an integer")
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for invalid withdraw argument"
