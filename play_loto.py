import random

# Карточка игрока
class Card:
    def __init__(self):
        numbers = random.sample(range(1, 91), 15)
        numbers.sort()
        self.rows = [numbers[i*5:(i+1)*5] for i in range(3)]

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


# Игрок
class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.card = Card()
        self.is_human = is_human

    def make_move(self, number):
        print(f"\n{self.name}'s карточка:")
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
                    print(f"{player.name} проиграл!")
                    return

                if player.has_won():
                    print(f"{player.name} победил!")
                    return


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.play()
