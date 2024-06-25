from twittr import shorten

def test_empty_str():
    assert shorten("") == ""

def test_argument():
    assert shorten("Twitter") == "twttr"
