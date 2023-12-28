import pytest
from fuel import convert, gauge


# Main function to run all the tests
def main():
    test_value_error()
    test_zero_division()
    test_convert()
    test_gauge()


# Test for the convert function with valid inputs
def test_convert():
    for key in [0, 1, 2, 3, 4]:
        assert convert(f"{key}/4") == key * 25
    for key in valid_convert_keys:
        assert type(convert(key)) == type(1)


# Test to check if ValueError is raised for invalid inputs
def test_value_error():
    with pytest.raises(ValueError):
        for key in value_error_keys:
            convert(key)


# Test to check if ZeroDivisionError is raised for fractions with zero denominator
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        for key in zero_division_error_keys:
            convert(key)


# Test for the gauge function with different inputs
def test_gauge():
    for key in gauge_f_keys:
        assert gauge(key) == "F"
    for key in gauge_e_keys:
        assert gauge(key) == "E"
    for key in gauge_percentage_keys:
        assert gauge(key) == (str(key) + "%")


# Valid keys for the convert function to test
valid_convert_keys = [
    "1/2",
    "2/2",
    "1/3",
    "2/3",
    "3/3",
    "1/4",
    "2/4",
    "3/4",
    "4/4",
    "1/5",
    "2/5",
    "3/5",
    "4/5",
    "5/5",
    "1/10",
    "5/10",
    "10/10",
    "1/20",
    "10/20",
    "15/20",
    "20/20",
]

# Invalid keys for convert function that should raise a ValueError (CS50)
value_error_keys = [
    "1/cat",
    "cat/1",
    "cat/cat",
    "5/3",
    "10/2",
    "dog/mouse",
]

# Invalid keys for convert function that should raise a ValueError (FULL)
"""
full_value_error_keys = [
    "1/cat",
    "cat/1",
    "cat/cat",
    "5/3",
    "10/2",
    "dog/mouse",
    "",
    "123",
    "12/34/56",
    "12-34",
    "ab+cd",
]
"""

# Keys that should raise a ZeroDivisionError in convert function
zero_division_error_keys = ["1/0", "5/0", "100/0", "0/0"]

# Keys for gauge function that should result in 'F' for full
gauge_f_keys = [99, 100, 150, 200]

# Keys for gauge function that should result in 'E' for empty
gauge_e_keys = [0, 1, -10, -50]

# Keys for gauge function that should show a percentage
gauge_percentage_keys = [2, 50, 75, 98]
