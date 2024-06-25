from plates import is_valid

def test_all_lette():
    assert is_valid("AA") == True
    assert is_valid("a") == False
    assert is_valid("A") == False

def test_all_number():
    assert is_valid("11") == False

def test_letter_number_2_len():
    assert is_valid("A1") == False
    assert is_valid("1A") == False

def test_letter_number():
    assert is_valid("cs50") == True
    assert is_valid("CS50") == True
    assert is_valid("AAA222") == True
