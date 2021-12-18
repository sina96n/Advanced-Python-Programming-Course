import random

class Human():
    count = 0
    def __init__(self, name) -> None:
        self.name = name

        Human.count += 1 

    def rename(self, name):
        self.name = name


    def __str__(self) -> str:
        return self.name


class Player(Human):
    def __init__(self, name) -> None:
        super().__init__(name)

        self._team = None

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, t):
        self._team = t

    @classmethod
    def add_players_by_info(cls, name_lst, team):
        players = list()
        for i in range(len(name_lst)):
            p = cls(name_lst[i])
            p.team = team

            players.append(p)

        return players


    def __str__(self) -> str:

        if self.team ==  None:
            return f"{self.name} : not a Team member."
        else:
            return f"{self.name} : {self.team} "



names = [
    "Hassan", "Maziar" , "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", 
    "Khashayar", "Milad", "Mostafa", "Amin", "Saeed", "pouya", "pouria", 
    "Reza", "Ali", "Behzad", "Soheil", "Behruz", "Shahruz", "Saman", "Mohsen"
]
teams = ["A","B"]

random_names = random.sample(names, 11)
remaining_names = [x for x in names if x not in random_names]

team_a = Player.add_players_by_info(random_names, teams[0])
team_b = Player.add_players_by_info(remaining_names, teams[1])

print(*team_a, sep="\n")
print(*team_b, sep="\n")