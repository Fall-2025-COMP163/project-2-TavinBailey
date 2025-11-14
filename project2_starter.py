"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Tavin Bailey
Date: 11/11/2025

AI Usage: AI helped with modifying the "MAIN PROGRAM FOR TESTING" tab of my python file to ensure usability and
verification of the 2 new classes I made: Archer and Healer. All things added or modified have a comment beside it
displaying "BONUS CLASS FOR EXTRA CREDIT" to help with readability and for my own sake when explaining what I added.

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"\n🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"\n🏆 {self.char2.name} wins!")
        else:
            print("\n🤝 It's a tie!")

# ============================================================= ===============
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        # TODO: Set the character's name, health, strength, and magic
        # These should be stored as instance variables
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        # TODO: Implement basic attack
        # Damage should be based on self.strength
        # Use target.take_damage(damage) to apply damage
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage! ⚔️")

    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        # TODO: Implement taking damage
        # Reduce self.health by damage amount
        # Make sure health doesn't go below 0
        self.health -= damage
        if self.health < 0:
            self.health = 0 # prevents negative health
        print(f"{self.name} takes {damage} damage! ⚔️ | {self.health} health remains! ❤️‍🩹")

    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        # TODO: Print character's name, health, strength, and magic
        # Make it look nice with formatting
        print()
        print("====== Character Stats ======")
        print()
        print(f"Name:\t\t{self.name}")
        print(f"Health:\t\t{self.health}")
        print(f"Strength:\t{self.strength}")
        print(f"Magic:\t\t{self.magic}")

class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        # TODO: Call super().__init__() with the basic character info
        # TODO: Store the character_class (like "Warrior", "Mage", etc.)
        # TODO: Add any other player-specific attributes (level, experience, etc.)
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0

    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        # TODO: Call the parent's display_stats method using super()
        # TODO: Then print additional player info like class and level
        super().display_stats()
        print(f"Class:\t\t{self.character_class}")
        print(f"Level:\t\t{self.level}")
        print(f"Experience:\t{self.experience}")

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """
        # TODO: Call super().__init__() with warrior-appropriate stats
        # Suggested stats: health=120, strength=15, magic=5
        super().__init__(name, character_class = "Warrior", health = 120, strength = 15, magic = 5)
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """
        # TODO: Implement warrior attack
        # Should do more damage than basic attack
        # Maybe strength + 5 bonus damage?
        damage = self.strength + 5 # boosts damage to 20, which is stronger than the base stat of 15 strength for the Warrior class.
        target.take_damage(damage)
        print(f"{self.name} performs a heavy strike on {target.name} for {damage} damage! 🗡️")
        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """
        # TODO: Implement power strike
        # Should do significantly more damage than regular attack
        damage = self.strength + 10 # boosts damage to 25, which is stronger than the base stat of 15 strength for the Warrior class.
        target.take_damage(damage)
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage! 🗡️")

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """
        # TODO: Call super().__init__() with mage-appropriate stats
        # Suggested stats: health=80, strength=8, magic=20
        super().__init__(name, character_class = "Mage", health = 80, strength = 8, magic = 20)
        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """
        # TODO: Implement mage attack
        # Should use self.magic for damage calculation instead of strength
        damage = self.magic + 5  # boosts damage to 25, which is stronger than the base stat of 20 magic for the Mage class.
        target.take_damage(damage)
        print(f"{self.name} casts magic on {target.name} for {damage} damage! 🧙‍♂️")
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # TODO: Implement fireball spell
        # Should do magic-based damage with bonus
        damage = self.magic + 10 # boosts damage to 30, which is stronger than the base stat of 20 magic for the Mage class.
        target.take_damage(damage)
        print(f"{self.name} uses FIREBALL on {target.name} for {damage} damage! 🔥")

class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """

    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """
        # TODO: Call super().__init__() with rogue-appropriate stats
        # Suggested stats: health=90, strength=12, magic=10
        super().__init__(name, character_class = "Rogue", health = 90, strength = 12, magic = 10)
        
    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        # TODO: Implement rogue attack
        # Could add a chance for critical hit (double damage)
        # Hint: use random.randint(1, 10) and if result <= 3, it's a crit
        import random
        damage = self.strength
        if random.randint(1, 10) <= 3: # boosts damage by a multiple of 2 if a random integer between 1 and 10 is generated and less than of equal to 3.
            damage *= 2 # boosts damage by a multiple of 2, resulting in 24 damage which is stronger than the base stat of 12 strength for the rogue class.
            print(f"CRITICAL HIT! ⚡")
        target.take_damage(damage)
        print(f"{self.name} strikes {target.name} for {damage} damage! 🤺")
        
    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """
        # TODO: Implement sneak attack
        # Should always do critical damage
        damage = self.strength * 2 # boosts damage by a multiple of 2, resulting in 24 damage which is stronger than the base stat of 12 strength for the rogue class.
        target.take_damage(damage)
        print(f"{self.name} uses SNEAK ATTACK on {target.name} for {damage} damage! 🥷")

class Archer(Player): # BONUS CLASS FOR EXTRA CREDIT
    """Archer class - ranged physical fighter"""

    def __init__(self, name):
        super().__init__(name, "Archer", health=85, strength=14, magic=5)

    def attack(self, target):
        damage = self.strength + 3 # boosts damage to 17, which is stronger than the base stat of 14 magic for the Archer class.
        target.take_damage(damage)
        print(f"{self.name} shoots an arrow at {target.name} for {damage} damage! 🏹")

    def rain_of_arrows(self, targets):
        """Hits all targets with a volley of arrows"""
        damage_per_target = self.strength # sets initial damage to base stat = 14 damage
        total_damage = damage_per_target * len(targets) # calculates sum (total damage) by adding the damage done to each target.
        print(f"{self.name} uses RAIN OF ARROWS! on {len(targets)} targets for a total of {total_damage} damage! 🎯")
        for target in targets:
            target.take_damage(damage_per_target) # sends 14 damage to each target


class Healer(Player): # BONUS CLASS FOR EXTRA CREDIT
    """Healer class - supports allies"""

    def __init__(self, name):
        super().__init__(name, "Healer", health=90, strength=5, magic=18)

    def attack(self, target):
        damage = self.magic // 2
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} with light magic for {damage} damage! ✨")

    def heal(self, target):
        """Restore health to a character"""
        amount = self.magic + 10
        target.health += amount
        print(f"{self.name} heals {target.name} for {amount} health! 💖")

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # TODO: Store weapon name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # TODO: Print weapon name and damage bonus
        print(f"{self.name} has {self.damage_bonus} damage bonus.")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    archer = Archer("Green Arrow") # BONUS CLASS FOR EXTRA CREDIT
    healer = Healer("Mercy") # BONUS CLASS FOR EXTRA CREDIT

    # TODO: Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    archer.display_stats() # BONUS CLASS FOR EXTRA CREDIT
    healer.display_stats() # BONUS CLASS FOR EXTRA CREDIT
    
    # TODO: Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)

    for character in [warrior, mage, rogue, archer, healer]: # included archer and healer classes into the for loop to test polymorphism and account for BONUS CLASS FOR EXTRA CREDIT
         print(f"\n{character.name} attacks the dummy:")
         character.attack(dummy_target)
         dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)

    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    archer.rain_of_arrows([target1, target2, target3]) # BONUS CLASS FOR EXTRA CREDIT
    healer.heal(warrior) # BONUS CLASS FOR EXTRA CREDIT
    
    # TODO: Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)

    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # TODO: Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
