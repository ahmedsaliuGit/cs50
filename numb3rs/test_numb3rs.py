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

if __name__ == "__main__":
    main()
