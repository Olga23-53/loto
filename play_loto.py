import random

# Карточка игрока
class Card:
    def __init__(self):
        numbers = random.sample(range(1, 91), 15)
        numbers.sort()
        self.rows = [numbers[i * 5:(i + 1) * 5] for i in range(3)]

    def show(self):
        for row in self.rows:
            print(" ".join(f"{num:>2}" if isinstance(num, int) else " -"
                           for num in row))

    def has_number(self, number):
        return any(number in row for row in self.rows)

    def mark(self, number):
        for row in self.rows:
            for i in range(len(row)):
                if row[i] == number:
                    row[i] = 'X'

    def is_complete(self):
        return all(num == 'X' for row in self.rows for num in row)

    def __str__(self):
        lines = []
        for row in self.rows:
            line = " ".join(f"{num:>2}" if isinstance(num, int) else " X" for num in row)
            lines.append(line)
        return "\n".join(lines)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.rows == other.rows

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Card(rows={self.rows})"


# Игрок
class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.card = Card()
        self.is_human = is_human

    def make_move(self, number):
        print(f"\nКарточка игрока: {self.name}")
        self.card.show()

        if self.is_human:
            answer = input(f"Зачеркнуть {number}? (y/n): ").lower()
            if answer == 'y':
                if self.card.has_number(number):
                    self.card.mark(number)
                else:
                    print("Неверно! Числа нет. Вы проиграли.")
                    return False
            else:
                if self.card.has_number(number):
                    print("Неверно! Число есть. Вы проиграли.")
                    return False
        else:
            if self.card.has_number(number):
                self.card.mark(number)
        return True

    def has_won(self):
        return self.card.is_complete()

    def __str__(self):
        player_type = "человек" if self.is_human else "бот"
        return f"Игрок: {self.name} ({player_type})"

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.name == other.name and self.is_human == other.is_human

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Player(name={self.name}, is_human={self.is_human})"


# Игра
class Game:
    def __init__(self):
        self.players = [
            Player("Вы", is_human=True),
            Player("Компьютер", is_human=False)
        ]
        self.bag = list(range(1, 91))
        random.shuffle(self.bag)

    def play(self):
        while self.bag:
            number = self.bag.pop()
            print(f"\nНовый бочонок: {number} (осталось {len(self.bag)})")

            for player in self.players:
                if not player.make_move(number):
                    if player.name.lower() == "вы":
                        print("Вы проиграли!")
                    else:
                        print(f"{player.name} проиграл!")
                    return

                if player.has_won():
                    if player.name.lower() == "вы":
                        print("Вы победили!")
                    else:
                        print(f"{player.name} победил!")
                    return

    def __str__(self):
        players_str = "\n".join(str(player) for player in self.players)
        return f"Игра с игроками:\n{players_str}\nБочонков осталось: {len(self.bag)}"

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return self.players == other.players

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"Game(players={self.players}, bag={self.bag})"

    def __len__(self):
        return len(self.bag)


if __name__ == "__main__":
    game = Game()
    game.play()

    # Проверка карточки
    # card = Card()
    # print(card)

    # Проверка игрока
    # player = Player("Вы", is_human=True)
    # print(player)

    # Проверка сравнения карточек
    # card1 = Card()
    # card2 = Card()
    # print("Карточка 1:")
    # card1.show()
    # print("\nКарточка 2:")
    # card2.show()
    # print("\nКарточки равны?", card1 == card2)

    # Проверка сравнения игроков
    # player1 = Player("Вы", is_human=True)
    # player2 = Player("Вы", is_human=True)
    # print("Игроки равны?", player1 == player2)

    # Проверка repr карточки
    # card = Card()
    # print(repr(card))

    # Проверка __str__ у игры
    # game = Game()
    # print(game)

    # Проверка сравнения игр
    # game1 = Game()
    # game2 = Game()
    # print("Игра 1:", game1.players)
    # print("Игра 2:", game2.players)
    # print("Игры равны?", game1 == game2)
