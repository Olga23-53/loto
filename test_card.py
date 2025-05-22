from play_loto import Card

def test_has_number_true():
    card = Card()
    # Вставляем известное число вручную
    card.rows = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    assert card.has_number(7) is True

def test_has_number_false():
    card = Card()
    card.rows = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    assert card.has_number(99) is False

def test_mark_number():
    card = Card()
    card.rows = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    card.mark(8)
    assert card.rows[1][2] == 'X'

def test_is_complete_false():
    card = Card()
    card.rows = [['X', 'X', 'X', 'X', 'X'], ['X', 7, 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X']]
    assert card.is_complete() is False

def test_is_complete_true():
    card = Card()
    card.rows = [['X'] * 5, ['X'] * 5, ['X'] * 5]
    assert card.is_complete() is True







