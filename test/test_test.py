import test


def test_add():
    assert test.add(3, 4) == 7
    assert test.add(3.5, 4) == 7
    assert test.add(3.9, 4) == 7
    assert test.add(3.9, 4.1) == 8


def test_to_sentence():
    assert test.to_sentence('apple') == 'Apple.'
    assert test.to_sentence('Apple trees') == 'Apple trees.'
    assert test.to_sentence('Apple trees.') == 'Apple trees.'