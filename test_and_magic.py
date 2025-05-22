from play_loto import Card, Player, Game

def test_card_creation():
    card = Card()
    assert len(card.rows) == 3
    assert all(len(row) == 5 for row in card.rows)

def test_card_mark_and_complete():
    card = Card()
    numbers = [num for row in card.rows for num in row]
    for num in numbers:
        card.mark(num)
    assert card.is_complete() is True

def test_card_has_number():
    card = Card()
    num = card.rows[0][0]
    assert card.has_number(num)
    assert card.has_number(999) is False

def test_player_make_move_correct(monkeypatch):
    player = Player("Тестовый", is_human=True)
    num = player.card.rows[0][0]
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert player.make_move(num) is True

def test_player_make_move_incorrect(monkeypatch):
    player = Player("Тестовый", is_human=True)
    num = 999  # точно нет в карточке
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert player.make_move(num) is False

def test_player_skip_incorrect(monkeypatch):
    player = Player("Тестовый", is_human=True)
    num = player.card.rows[0][0]  # есть в карточке
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert player.make_move(num) is False

def test_player_skip_correct(monkeypatch):
    player = Player("Тестовый", is_human=True)
    num = 999  # точно нет в карточке
    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert player.make_move(num) is True

def test_bot_move():
    player = Player("Бот", is_human=False)
    num = player.card.rows[0][0]
    assert player.make_move(num) is True

def test_game_length():
    game = Game()
    assert len(game) == 90

def test_player_equality():
    p1 = Player("Игрок", True)
    p2 = Player("Игрок", True)
    p3 = Player("Другой", False)
    assert p1 == p2
    assert p1 != p3

def test_card_equality():
    c1 = Card()
    c2 = Card()
    assert c1 != c2
    assert c1 == c1
