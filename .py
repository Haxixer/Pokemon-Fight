import time
import numpy as np # type: ignore
import sys

# Delay Printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# This Creates The Pokemon Class
class Pokemon:
    def __init__(self, name, type, moves, EVs, health='=============='):
        self.name = name
        self.types = type
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20  # Amount of health bars

    def fight(self, Pokemon2):
        # Printing The Pokemon Info
        print("----Pokemon Battle----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3 * (1 + np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3 * (1 + np.mean([Pokemon2.attack, Pokemon2.defense])))

        time.sleep(2)

        # Type advantage logic
        version = ['Fire', 'Water', 'Grass']
        for i, k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's not very effective..."
                elif Pokemon2.types == version[(i + 1) % 3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "It's not very effective..."
                    string_2_attack = "It's super effective!"
                elif Pokemon2.types == version[(i + 2) % 3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "It's super effective!"
                    string_2_attack = "It's not very effective..."

        # This Is The Battle Loop
        while self.bars > 0 and Pokemon2.bars > 0:
            # This Prints The Health Bars
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            # Your Turn To Pick A Move
            print(f"{self.name}, choose a move:")
            for i, move in enumerate(self.moves):
                print(f"{i + 1}. {move}")
            while True:
                try:
                    index = int(input("Enter move number: ")) - 1
                    if 0 <= index < len(self.moves):
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter a number.")

            delay_print(f"{self.name} used {self.moves[index]}!\n")
            time.sleep(1)
            delay_print(string_1_attack)

            # This Calculates The Damage
            Pokemon2.bars -= self.attack
            Pokemon2.bars = max(0, Pokemon2.bars)  # Prevent negative health
            Pokemon2.health = "=" * int(Pokemon2.bars)

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            if Pokemon2.bars <= 0:
                delay_print(f"\n...{Pokemon2.name} fainted!")
                break

            # Pokemon2/ AI Turn
            print(f"{Pokemon2.name} is attacking!")
            move = np.random.choice(Pokemon2.moves)
            delay_print(f"{Pokemon2.name} used {move}!\n")
            time.sleep(1)
            delay_print(string_2_attack)

            # This Cauculates The Damage 
            self.bars -= Pokemon2.attack
            self.bars = max(0, self.bars)  # This Stops The Health From Going To A Negitive
            self.health = "=" * int(self.bars)

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            if self.bars <= 0:
                delay_print(f"\n...{self.name} fainted!")
                break

        # It Pays You Even If You Lose
        money = np.random.randint(0, 5000)
        delay_print(f"\nYour opponent paid you ${money}.")
        

# Main function
if __name__ == '__main__':
    # These Are The Pokemon Moves And What pokemon you can pick
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 10, 'DEFENSE': 8})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Solar Beam', 'Vine Whip', 'Petal Dance', 'Razor Leaf'], {'ATTACK': 11, 'DEFENSE': 7})
    Blastoise = Pokemon('Blastoise', 'Water', ['Hydro Pump', 'Surf', 'Waterfall', 'Aqua Jet'], {'ATTACK': 9, 'DEFENSE': 9})

    Quilava = Pokemon('Quilava', 'Fire', ['Flame Wheel', 'Ember', 'Lava Plume', 'Flame Charge'], {'ATTACK': 10, 'DEFENSE': 10})
    Bayleef = Pokemon('Bayleef', 'Grass', ['Razor Leaf', 'Solar Beam', 'Petal Dance', 'Vine Whip'], {'ATTACK': 6, 'DEFENSE': 12})
    Feraligatr = Pokemon('Feraligatr', 'Water', ['Claw', 'Surf', 'Waterfall', 'Aqua Jet'], {'ATTACK': 10, 'DEFENSE': 8})

    Blaziken = Pokemon('Blaziken', 'Fire', ['Flare Blitz', 'Fire Spin', 'Fire Punch', 'Ember'], {'ATTACK': 12, 'DEFENSE': 6})
    Sceptile = Pokemon('Sceptile', 'Grass', ['Leaf Blade', 'Solar Beam', 'Frenzy Plant', 'Leaf Storm'], {'ATTACK': 11, 'DEFENSE': 7})
    Swampert = Pokemon('Swampert', 'Water', ['Hydro Pump', 'Mud Shot', 'Water Gun', 'Aqua Tail'], {'ATTACK': 10, 'DEFENSE': 8})

    Rapidash = Pokemon('Rapidash', 'Fire', ['Flame Charge', 'Fire Spin', 'Ember', 'Flare Blitz'], {'ATTACK': 10, 'DEFENSE': 3})
    Dewgong = Pokemon('Dewgong', 'Water', ['Aqua Jet', 'Water Gun', 'Hydro Pump', 'Ice Beam'], {'ATTACK': 4, 'DEFENSE': 9})
    Kingler = Pokemon('Kingler', 'Water', ['Crabhammer', 'Bubble Beam', 'Water Gun', 'Vice Grip'], {'ATTACK': 6, 'DEFENSE': 7})
    Tangrowth = Pokemon('Tangrowth', 'Grass', ['Power Whip', 'Vine Whip', 'Leaf Storm', 'Solar Beam'], {'ATTACK': 4, 'DEFENSE': 8})
    Seaking = Pokemon('Seaking', 'Water', ['Horn Attack', 'Waterfall', 'Aqua Tail', 'Surf'], {'ATTACK': 5, 'DEFENSE': 8})
    Magmotar = Pokemon('Magmortar', 'Fire', ['Fire Blast', 'Flamethrower', 'Ember', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 6})

    Torterra = Pokemon('Torterra', 'Grass', ['Earthquake', 'Leaf Storm', 'Solar Beam', 'Wood Hammer'], {'ATTACK': 11, 'DEFENSE': 7})
    Infernape = Pokemon('Infernape', 'Fire', ['Flare Blitz', 'Close Combat', 'Flame Wheel', 'Ember'], {'ATTACK': 12, 'DEFENSE': 6})
    Empoleon = Pokemon('Empoleon', 'Water', ['Hydro Pump', 'Aqua Jet', 'Surf', 'Waterfall'], {'ATTACK': 10, 'DEFENSE': 8})

    Serperior = Pokemon('Serperior', 'Grass', ['Leaf Blade', 'Solar Beam', 'Leaf Storm', 'Vine Whip'], {'ATTACK': 11, 'DEFENSE': 7})
    Emboar = Pokemon('Emboar', 'Fire', ['Flare Blitz', 'Fire Punch', 'Ember', 'Heat Crash'], {'ATTACK': 12, 'DEFENSE': 6})
    Samurott = Pokemon('Samurott', 'Water', ['Hydro Pump', 'Aqua Jet', 'Surf', 'Waterfall'], {'ATTACK': 10, 'DEFENSE': 8})

    Chesnaught = Pokemon('Chesnaught', 'Grass', ['Wood Hammer', 'Hammer Arm', 'Seed Bomb', 'Vine Whip'], {'ATTACK': 11, 'DEFENSE': 7})
    Delphox = Pokemon('Delphox', 'Fire', ['Flamethrower', 'Fire Blast', 'Ember', 'Psychic'], {'ATTACK': 12, 'DEFENSE': 6})
    Greninja = Pokemon('Greninja', 'Water', ['Hydro Pump', 'Aqua Jet', 'Surf', 'Waterfall'], {'ATTACK': 10, 'DEFENSE': 8})

    Decidueye = Pokemon('Decidueye', 'Grass', ['Leaf Blade', 'Spirit Shackle', 'Razor Leaf', 'Sucker Punch'], {'ATTACK': 11, 'DEFENSE': 7})
    Incineroar = Pokemon('Incineroar', 'Fire', ['Darkest Lariat', 'Flare Blitz', 'Ember', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 6})
    Primarina = Pokemon('Primarina', 'Water', ['Sparkling Aria', 'Hydro Pump', 'Aqua Jet', 'Surf'], {'ATTACK': 10, 'DEFENSE': 8})   

    Rillaboom = Pokemon('Rillaboom', 'Grass', ['Grassy Glide', 'Wood Hammer', 'Drum Beating', 'Leaf Blade'], {'ATTACK': 11, 'DEFENSE': 7})
    Cinderace = Pokemon('Cinderace', 'Fire', ['Pyro Ball', 'Flame Charge', 'Ember', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 6})
    Inteleon = Pokemon('Inteleon', 'Water', ['Snipe Shot', 'Hydro Pump', 'Aqua Jet', 'Surf'], {'ATTACK': 10, 'DEFENSE': 8})

    Meowscarada = Pokemon('Meowscarada', 'Grass', ['Flower Trick', 'Leaf Blade', 'Razor Leaf', 'Vine Whip'], {'ATTACK': 11, 'DEFENSE': 7})
    Skeledirge = Pokemon('Skeledirge', 'Fire', ['Torch Song', 'Flamethrower', 'Ember', 'Fire Punch'], {'ATTACK': 12, 'DEFENSE': 6})
    Quaquaval = Pokemon('Quaquaval', 'Water', ['Aqua Step', 'Hydro Pump', 'Aqua Jet', 'Surf'], {'ATTACK': 10, 'DEFENSE': 8})
   
    # Picks Who Fights Change this to ______.fight(______)
    Charizard.fight(Venusaur)