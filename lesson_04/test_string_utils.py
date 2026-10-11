import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Два теста - подсказки от техлида
@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Добавить шесть тестов для оставшихся трех функций
# Trim
@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  hello", "hello"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" hello world", "hello world"),
    ("hello  ", "hello  "),
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Contains
@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
  ("SkyPro", "S", True),
  ("SkyPro", "k", True),
  ("hello world", "o", True),
  ("12345", "3", True),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
  ("SkyPro", "u", False),
  ("hello world", "v", False),
  ("12345", "9", False),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


# delete_symbol
@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
  ("SkyPro", "k", "SyPro"),
  ("SkyPro", "Sky", "Pro"),
  ("hello world", "l", "heo word"),
  ("12345", "3", "1245"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, input_symbol, expected", [
  ("SkyPro", "u", "SkyPro"),
  ("hello world", "v", "hello world"),
  ("12345", "9", "12345"),
 ])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
