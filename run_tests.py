from students import Student
from team import Team

"""-------------Part A------------"""

student = Student("Ying", "E65")

print(f"{student.name} is in {student.cohort}")
print(student.talk())

# student.say_favourite_language(input("what's your fav language? "))

print(student.say_favourite_language("Python"))

"""-------------Part B------------"""

players = ["Craig", "Jason", "Tom", "Patrick"]
team = Team("Cool Runnings", players, "Irv Blitzer")

# add new player called Pete
team.add_player("Pete")
print(players)

# check if the player in the list
print(team.has_player("Jerry"))
print(team.has_player("Tom"))

# extension
team.play_game(True)
print(team.point)