import random

class Human():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Player(Human):
    def __init__(self, name, team) -> None:
        super().__init__(name)

        self.team = team



names = [
    "Hassan", "Maziar" , "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", 
    "Khashayar", "Milad", "Mostafa", "Amin", "Saeed", "pouya", "pouria", 
    "Reza", "Ali", "Behzad", "Soheil", "Behruz", "Shahruz", "Saman", "Mohsen"
]
teams = ["A","B"]



# a = Player("Sina")
# print(a)