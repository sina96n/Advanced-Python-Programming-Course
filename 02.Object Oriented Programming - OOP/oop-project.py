import random

class Human():
    count = 0
    def __init__(self, name) -> None:
        self.name = name

        Human.count += 1 

    def rename(self, name):
        self.name = name

    # defining a default representation form for the class
    def __str__(self) -> str:
        return self.name

# class Player that inherits from class Human
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

    # Adding a group of palyers at once
    @classmethod
    def add_players_by_info(cls, names, team):
        players = list()
        for i in range(len(names)):
            p = cls(names[i])
            p.team = team

            players.append(p)

        return players

    # defining a default representation form for the class
    def __str__(self) -> str:

        if self.team ==  None:
            return f"{self.name} : not a Team member."
        else:
            return f"{self.name} : {self.team} "


# creating list of names
names = [
    "Hassan", "Maziar" , "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", 
    "Khashayar", "Milad", "Mostafa", "Amin", "Saeed", "pouya", "pouria", 
    "Reza", "Ali", "Behzad", "Soheil", "Behruz", "Shahruz", "Saman", "Mohsen"
]
teams = ["A","B"]       # desired teams

# choosing random names to put in team A
# putting all remainig names in team B
random_names = random.sample(names, 11)
remaining_names = [x for x in names if x not in random_names]

# creating Player objects for each team
team_a = Player.add_players_by_info(random_names, teams[0])
team_b = Player.add_players_by_info(remaining_names, teams[1])

# printing outputs
print(*team_a, sep="\n")
print(*team_b, sep="\n")




# By Sina Kazemi
# https://github.com/sina96n