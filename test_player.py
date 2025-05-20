from play_loto import Card, Player
import pytest

# создаём тестовую карточку с числами от 1 до 15
@pytest.fixture
def test_card_with_number():
    card = Card()
    card.rows = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    print("\nТестовая карточка:")
    for row in card.rows:
        print(" ".join(f"{num:>2}" for num in row))
    return card

# Тестовая карточка без наследования от Card — только нужные методы
class CardForTest:
    def __init__(self, rows):
        self.rows = rows

    def is_complete(self):
        return all(num == 'X' for row in self.rows for num in row)

# Проверка: игрок выиграл (вся карточка из 'X')
def test_player_has_won_true():
    player = Player("Тестовый игрок")
    player.card = CardForTest([['X'] * 5, ['X'] * 5, ['X'] * 5])
    assert player.has_won() is True

# Проверка: игрок НЕ выиграл (есть число среди 'X')
def test_player_has_won_false():
    player = Player("Тестовый игрок")
    player.card = CardForTest([['X'] * 5, ['X', 7, 'X', 'X', 'X'], ['X'] * 5])
    assert player.has_won() is False

# Игрок говорит "y", но числа нет — проигрыш
def test_human_wrong_input_yes(monkeypatch, test_card_with_number):
    player = Player("Человек", is_human=True)
    player.card = test_card_with_number
    monkeypatch.setattr('builtins.input', lambda _: 'y')  # Симулируем ввод "y"
    result = player.make_move(99)  # Числа 99 нет в карточке
    assert result is False

# Игрок говорит "n", но число есть — проигрыш
def test_human_wrong_input_no(monkeypatch, test_card_with_number):
    player = Player("Человек", is_human=True)
    player.card = test_card_with_number
    monkeypatch.setattr('builtins.input', lambda _: 'n')  # Симулируем ввод "n"
    result = player.make_move(5)  # Число 5 есть
    assert result is False

# Игрок говорит "y", и число действительно есть — успех
def test_human_correct_input(monkeypatch, test_card_with_number):
    player = Player("Человек", is_human=True)
    player.card = test_card_with_number
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    result = player.make_move(5)
    assert result is True
    assert player.card.rows[0][4] == 'X'  # Проверим, что 5 заменилось на 'X'
