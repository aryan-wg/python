# import config

# This line loads a set of 6 random numbers from the config file
lottery_numbers = {1,3,4,5,6,7} 

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

matching = {
    player["name"]:player["numbers"].intersection(lottery_numbers)
    for player
    in players 
}
print(matching)
# scores = { (player["name"],100**len(player["matching"])) for player in matching }
scores = { player:100**len(matching) for player,matching in matching.items() }
print(scores)

max_score = {"name":"noOne","score":-1}
for player in scores.items():
    if max_score["score"]<player[1]:
       max_score["name"] = player[0]
       max_score["score"] = player[1]
print(f"{max_score['name'].title()} won {max_score['score']}")

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)
