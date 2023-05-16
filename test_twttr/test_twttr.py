from twttr import shorten

def test_shorten():
    assert shorten("") == ""
    assert shorten("Hello") == "Hll"
    assert shorten("wor1ld") == "wr1ld"
    assert shorten("Python.") == "Pythn."
    assert shorten("AEIOU") == ""



