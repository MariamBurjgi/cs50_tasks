from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("172.16.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid_ipv4():
    assert validate("256.0.0.1") == False
    assert validate("192.168.1.300") == False
    assert validate("foo.bar.baz.qux") == False
