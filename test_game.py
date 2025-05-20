import pytest
from play_loto import Card, Player, Game


class CardForTest(Card):
    def __init__(self, rows):
        super().__init__()
        self.rows = rows

# ---------- FIXTURES ----------

@pytest.fixture
def winning_card():
    return CardForTest([['X'] * 5, ['X'] * 5, ['X'] * 5])


@pytest.fixture
def losing_card():
    return CardForTest([
        ['X'] * 5,
        ['X', 7, 'X', 'X', 'X'],  # 7 не зачеркнута
        ['X'] * 5
    ])


@pytest.fixture
def test_card_without_99():
    return CardForTest([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ])


# ---------- ТЕСТЫ ДЛЯ GAME ----------

def test_game_player_wins(monkeypatch, capsys, winning_card, losing_card):
    game = Game()

    # Подменяем игроков: оба — не человек (чтобы не было input)
    game.players = [
        Player("Вы", is_human=False),
        Player("Компьютер", is_human=False)
    ]

    game.players[0].card = winning_card
    game.players[1].card = losing_card

    game.bag = [42]  # любое число

    game.play()

    output = capsys.readouterr().out
    assert "Вы победили" in output



def test_game_player_loses(monkeypatch, capsys, test_card_without_99):
    game = Game()

    game.players = [
        Player("Вы", is_human=True),
        Player("Компьютер", is_human=False)
    ]

    game.players[0].card = test_card_without_99
    game.players[1].card = CardForTest([['X'] * 5, ['X'] * 5, ['X'] * 5])  # Компьютер выигрывает

    monkeypatch.setattr('builtins.input', lambda _: 'y')  # Игрок говорит "зачеркну", но 99 нет

    game.bag = [99]  # числа нет в карточке игрока

    game.play()

    output = capsys.readouterr().out
    assert "Вы проиграли" in output
