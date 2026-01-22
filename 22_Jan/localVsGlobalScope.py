enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#local global variable


#global
player_health = 10

def drink_potion():
    potion_strenght = 2
    print(player_health)
    print(potion_strenght)

print(player_health)   #local variable so it will not print



#there is no block scope in python


game_level = 10
enemies = ["skelton", "zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level <5:
        new_enemy = enemies[0]
    print(new_enemy)    