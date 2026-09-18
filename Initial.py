from dataclasses import dataclass
from typing import List


@dataclass
class Game:
    title: str
    genre: str
    hours: int
    rating: float


class GameLibrary:
    def __init__(self):
        self.games: List[Game] = []

    def add_game(self, title: str, genre: str, hours: int, rating: float):
        self.games.append(Game(title, genre, hours, rating))

    def sort_by_rating(self):
        self.games.sort(key=lambda game: game.rating, reverse=True)

    def total_hours(self):
        return sum(game.hours for game in self.games)

    def average_rating(self):
        if not self.games:
            return 0.0

        return sum(game.rating for game in self.games) / len(self.games)

    def print_report(self):
        print("Game Library")
        print("============")

        for game in self.games:
            print(
                f"{game.title} | {game.genre} | "
                f"{game.hours} hours | Rating: {game.rating:.1f}"
            )

        print("============")
        print(f"Games: {len(self.games)}")
        print(f"Total Hours: {self.total_hours()}")
        print(f"Average Rating: {self.average_rating():.2f}")


library = GameLibrary()

library.add_game("Cyber World", "Action", 42, 9.1)
library.add_game("Lost Kingdom", "RPG", 68, 8.7)
library.add_game("Speed Legends", "Racing", 25, 8.4)
library.add_game("Space Mission", "Adventure", 35, 9.3)

library.sort_by_rating()
library.print_report()