from numb3rs import validate

def main():
    test_valid_ip()
    test_invalid_ip()

def test_valid_ip():
    assert validate("192.0.1.2") == "Valid"
    assert validate("192.255.1.2") == "Valid"
    assert validate("192.245.106.2") == "Valid"
    assert validate("192.235.109.200") == "Valid"

def test_invalid_ip():
    assert validate("-192.0.1.2") == "Invalid"
    assert validate("cat") == "Invalid"
    assert validate("192.678.1.2") == "Invalid"
    assert validate("1234567890") == "Invalid"
    assert validate("-192.0.1") == "Invalid"

if __name__ == "__main__":
    main()
