from twttr import shorten

def test_empty_str():
    assert shorten("") == ""

def test_argument():
    assert shorten("Twitter") == "Twttr"

def test_lowercase():
    assert shorten("baller") == "bllr"

def test_uppercase():
    assert shorten("BALLER") == "BLLR"
