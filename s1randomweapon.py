import random
weapon = [".52 Gal", ".52 Gal Deco", ".96 Gal", ".96 Gal Deco", "Aerospray MG", "Aerospray PG", "Aerospray RG", "Bamboozler 14 Mk I", "Bamboozler 14 Mk II", "Bamboozler 14 Mk III", "Bento Splat Charger", "Bento Splatterscope", "Berry Splattershot Pro", "Blaster", "Carbon Roller", "Carbon Roller Deco", "Cherry H-3 Nozzlenoze", "Classic Squiffer", "CoroCoro Splat Roller", "Custom Blaster", "Custom Dual Squelcher", "Custom E-liter 3K", "Custon E-liter 3K Scope", "Custom Hydra Splating", "Custom Jet Squelcher", "Custom Range Blaster", "Custom Splattershot Jr.", "Dual Squelcher", "Dynamo Roller", "E-liter 3K", "E-liter 3K Scope", "Forge Splattershot Pro", "Fresh Squiffer", "Gold Dynamo Roller", "Grim Range Blaster", "H-3 Nozzlenoze", "H-3 Nozzlenoze D", "Heavy Splatling", "Heavy Splatling Deco", "Heavy Splatling Remix", "Hero Charger Replica", "Hero Roller Replica", "Hero Shot Replica", "Hydra Splatling", "Inkbrush", "Inkbrush Nouveau", "Jet Squelcher", "Kelp Splat Charger", "Kelp Splatterscope", "Krak-On Splat Roller", "L-3 Nozzlenoze", "L-3 Nozzlenoze D", "Luna Blaster", "Luna Blaster Neo", "Mini Splatling", "N-ZAP '83", "N-ZAP '85", "N-ZAP '89", "Neo Splash-o-matic", "Neo Sploosh-o-matic", "New Squiffer", "Octobrush", "Octobrush Nouveau", "Octoshot Replica", "Permanent Inkbrush", "Range Blaster", "Rapid Blaster", "Rapid Blaster Deco", "Rapid Blaster Pro", "Rapid Blaster Pro Deco", "Refurbished Mini Splatling", "Slosher", "Slosher Deco", "Sloshing Machine", "Sloshing Machine Neo", "Soda Slosher", "Splash-o-matic", "Splat Charger", "Splat Roller", "Splatterscope", "Splattershot", "Splattershot Jr.", "Splattershot Pro", "Sploosh-o-matic", "Sploosh-o-matic 7", "Tempered Dynamo Roller", "Tentatek Splattershot", "Tri-Slosher", "Tri-Slosher Nouveau", "Wasabi Splattershot", "Zink Mini Splatling"]

def randomwep():
    print("------------------------------------")
    print(random.sample(weapon, 1,))
    keepgoing = input("Generate a new weapon? (y or n) ")
    if keepgoing == 'y' or keepgoing == 'Y' or keepgoing == 'n' or keepgoing == 'N':
            if keepgoing == 'y' or keepgoing == 'Y':
                randomwep()
            else:
                 print()
                 print()
                 menu()
    else:
        print("Error, answer must be either Y or N")
        randomwep()

def roulette():
    random.shuffle(weapon)
    roulcontinue = 1
    score = 0
    print("Welcome to weapon roulette! Try and win a battle with each weapon generated!")
    print()
    while roulcontinue ==1:
        print("------------------------------------")
        print("Points:",score)
        print(weapon[score])
        keepgoing = input("Generate a new weapon? (y or n) ")
        if keepgoing == 'y' or keepgoing == 'Y' or keepgoing == 'n' or keepgoing == 'N':
            if keepgoing == 'y' or keepgoing == 'Y':
                 score = score + 1
                 if score == 91:
                     roulcontinue = 0
                     print("Congratulations! You completed all the weapons! Your final score is 91!")
                     print()
                     print()
                     menu()
                 else:
                     roulcontinue = 1
            else:
                print(f"Congrats! Your final score is {score}!")
                print()
                print()
                roulcontinue = 0
                menu()
        else:
            print("Error, answer must be either Y or N")

def menu():
    print("------------------------------------")
    print("Splatoon 1 Random Weapon Generator")
    print("------------------------------------")
    print("Welcome to Lappy's Splatoon 1 Weapon Generator and Roulette!")
    print("To generate random weapons, type w, to try the roulette, type r")
    print("If you want to exit, type e")
    print("------------------------------------")
    choice = input()
    if choice == 'e' or choice == 'E':
        quit
    else:
        if choice == 'w' or choice == 'W' or choice == 'r' or choice == 'R':
                    if choice == 'w' or choice == 'W':
                        randomwep()
                    else:
                        roulette()
        else:
                    print("Error, answer must be either W or R")
                    menu()
menu()

