import random

class Military:
    def __init__(self, uniq_id, team_id):
        self.uniq_id = uniq_id
        self.team_id = team_id


class Team:
    def __init__(self, teamId):
        self.TeamId = teamId
        self.team = []

    def add_military(self, military):
        self.team.append(military)


class Soldier(Military):
    def become_hero(self, hero):
        pass


class Hero(Military):
    def __init__(self, uniq_id, team_id, level=1):
        Military.__init__(self, uniq_id, team_id)
        self.level = level

    def level_up(self):
        self.level += 1


team1 = Team(1)
team2 = Team(2)
hero1 = Hero(1, 1)
hero2 = Hero(2, 2)
team1.add_military(hero1)
team2.add_military(hero2)
for i in range(3, 100):
    uniq_id = i
    choice = random.randint(1, 2)
    if choice == 1:
        team1.add_military(Soldier(uniq_id, 1))
    else:
        team2.add_military(Soldier(uniq_id, 2))


print("Team1 lenght :", len(team1.team))
print("Team2 lenght :", len(team2.team))

if len(team1.team) >= len(team2.team):
    hero1.level_up()
    print("The hero of team1 raises the level", hero1.level)
else:
    hero2.level_up()
    print("The hero of team2 raises the level", hero2.level)

if len(team1.team) >= len(team2.team):
    team1.team[1].become_hero(Soldier)
    print('Team1 get new hero', team1.team[1].uniq_id)
else:
    team2.team[1].become_hero(Soldier)
    print('Team2 get new hero', team2.team[1].uniq_id)