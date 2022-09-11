import pytest, math


# float

@pytest.mark.parametrize('input,expected', [(1.4, 1), (1.5, 2), (1, 1)])
def test_float_round(input, expected):
    actual = round(input)
    assert actual == expected

def test_float_sqrt():
    f: float = -3
    try:
        assert math.sqrt(f)
    except ValueError:
        pass


# str

@pytest.mark.parametrize('number, expected', [(1.2, '1'), (1, '1'), (1.8, '1')])
def test_str_format_digit__should_round_before_format(number, expected):
    s: str = 'I am %d' % (number)
    assert s == 'I am ' + expected

def test_str_get_char_by_index():
    s: str = 'Kate'
    try:
        assert s[6]
    except IndexError:
        pass


# dict

def test_dict_get_value_by_key__when_no_key():
    d = {'Оно': 'Стивен Кинг'}
    try:
        assert d['Преступление и наказание']
    except KeyError:
        pass

@pytest.mark.parametrize('key,expected', [('Оно', 'Стивен Кинг'), ('Преступление и наказание', 'Федор Михайлович Достоевский')])
def test_dict_get_value_by_key__when_has_key(key, expected):
    d = {'Оно': 'Стивен Кинг', 'Преступление и наказание': 'Федор Михайлович Достоевский'}

    actual = d[key]
    assert actual == expected
