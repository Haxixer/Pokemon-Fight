import time
import numpy as np
import sys

# Delay Printing
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Create the Pokemon class
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
        # Print fight information
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

        # Fight loop
        while self.bars > 0 and Pokemon2.bars > 0:
            # Print health
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            # Player's turn
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

            # Calculate damage
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

            # Pokemon2's turn
            print(f"{Pokemon2.name} is attacking!")
            move = np.random.choice(Pokemon2.moves)
            delay_print(f"{Pokemon2.name} used {move}!\n")
            time.sleep(1)
            delay_print(string_2_attack)

            # Calculate damage
            self.bars -= Pokemon2.attack
            self.bars = max(0, self.bars)  # Prevent negative health
            self.health = "=" * int(self.bars)

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(0.5)

            if self.bars <= 0:
                delay_print(f"\n...{self.name} fainted!")
                break

        # Reward
        money = np.random.randint(0, 5000)
        delay_print(f"\nYour opponent paid you ${money}.")
        

# Main function
if __name__ == '__main__':
    # Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK': 10, 'DEFENSE': 8})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Solar Beam', 'Vine Whip', 'Petal Dance', 'Razor Leaf'], {'ATTACK': 11, 'DEFENSE': 7})
    Blastoise = Pokemon('Blastoise', 'Water', ['Hydro Pump', 'Surf', 'Waterfall', 'Aqua Jet'], {'ATTACK': 9, 'DEFENSE': 9})

    Quilava = Pokemon('Quilava', 'Fire', ['Flame Wheel', 'Ember', 'Lava Plume', 'Flame Charge'], {'ATTACK': 10, 'DEFENSE': 10})
    Bayleef = Pokemon('Bayleef', 'Grass', ['Razor Leaf', 'Solar Beam', 'Petal Dance', 'Vine Whip'], {'ATTACK': 6, 'DEFENSE': 12})
    Feraligatr = Pokemon('Feraligatr', 'Water', ['Hydro Pump', 'Surf', 'Waterfall', 'Aqua Jet'], {'ATTACK': 10, 'DEFENSE': 8})

    

    # Start a battle
    Charizard.fight(Venusaur)
      