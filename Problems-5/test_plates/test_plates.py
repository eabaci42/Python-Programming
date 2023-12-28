from plates import is_valid


def main():
    test_is_valid_upper()
    test_is_valid_lower()
    test_is_valid_mix()


def test_is_valid_upper():
    for key in valid_keys:
        assert is_valid(key.upper()) == True
    for key in invalid_keys:
        assert is_valid(key.upper()) == False


def test_is_valid_lower():
    for key in valid_keys:
        assert is_valid(key.lower()) == True
    for key in invalid_keys:
        assert is_valid(key.lower()) == False


def test_is_valid_mix():
    for key in valid_keys:
        assert is_valid(key) == True
    for key in invalid_keys:
        assert is_valid(key) == False


invalid_keys = [
    "CS05",
    "CS50P",
    "PI3.14",
    "H",
    "QUTATIME",
    ". 5",
    "CS.50",
    "CS.50CS",
    "@CS50",
    "2023CS",
    "",
    "A1",
    "ABCDEF1",
    "AB@12"
]

valid_keys = [
    "CS50",
    "AB1234",
    "GH12",
    "XY"
]
