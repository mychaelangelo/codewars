class Warrior:
    max_level = 100
    ranks = [
        "Pushover", 
        "Novice", 
        "Fighter", 
        "Warrior", 
        "Veteran", 
        "Sage", 
        "Elite", 
        "Conqueror", 
        "Champion", 
        "Master", 
        "Greatest"
    ]

    def __init__(self):
        self.level = 1 # start level
        self.rank = "Pushover"
        self.experience = 100 # start xp
        self.achievements = []
    
    def get_level(self):
        return self.level

    def update_rank(self):
        self.rank = Warrior.ranks[self.level // 10]

    def update_level(self):
        self.level = self.experience // 100
    
    def up_xp(self, xp):
        if (self.experience + xp) <= 10000:
            self.experience += xp
            self.update_level()
            self.update_rank()
        else: # cap at 10,000
            self.experience = 10000
            self.update_level()
            self.update_rank()


    def battle(self, enemy_level):
        if enemy_level not in range(1,101):
            return "Invalid level"
                
        enemy_diff = enemy_level - self.level
        
        enemy_rank = Warrior.ranks[enemy_level // 10]
        enemy_rank_diff = Warrior.ranks.index(enemy_rank) - Warrior.ranks.index(self.rank)

        if enemy_diff >= 5 and enemy_rank_diff >=1 :
            return "You've been defeated"

        if enemy_diff == 0:
            self.up_xp(10)
            return "A good fight"
        elif enemy_diff == -1:
            self.up_xp(5)
            return "A good fight"
        elif enemy_diff <= -2:
            self.up_xp(0)
            return "Easy fight"
        elif enemy_diff > 0:
            self.up_xp(20 * enemy_diff * enemy_diff)
            return "An intense fight"
    
    def training(self, training_list):
        if self.level >= training_list[2]:
            self.up_xp(training_list[1]) # set xp points
            self.achievements.append(training_list[0]) # set the achievement
            return training_list[0]
        else:
            return "Not strong enough"




bruce_lee = Warrior()
print(bruce_lee.level)
print(bruce_lee.experience)
print(bruce_lee.rank)
print(bruce_lee.achievements)
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
print(bruce_lee.experience)
print(bruce_lee.level)
print(bruce_lee.rank)
print(bruce_lee.battle(90) )