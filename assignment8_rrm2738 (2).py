#Assignment 8 RRM2738

# Question 1
class Characters:
    #This initializes the charecters with a name and health value

  def __init__(self, name, health):
    self.name = name
    self.health = health


  def __str__(self):
      #This puts the health and name on the same line when printed
      return self.name + ' (health=' + str(self.health) + ')'


  def take_damage(self, damage):
      #This subtracts the damage from the health
    self.health -= damage
    return self.health



class Hero(Characters):
    #This is a subclass for heroes from the class characters

  def __init__(self, name, health):
    super().__init__(name, health)
    self._inventory = []


  def restore_health(self, add):
    #This adds back the health when a health elixer is found
    self.health += add


  def add_inventory(self, item):
    #This adds the item found to the inventory
    self._inventory.append(item)


  def remove_inventory(self, item):
    #This removes an item from the inventory
    self._invetory.remove(item)


  def get_inventory(self):
    #shows what is in the Inventory
    return self._inventory



class Enemy(Characters):
    #This is a subclass for enemies from the class of characters

  def __init__(self, name, health, damage):
    super().__init__(name, health)
    self.name = name
    self.health = health
    self.damage = damage


def main():
    print('Start:')
    h = Hero("Han", 40)
    print(h)
    # Creates a hero with the name Han and health 40
    e = Enemy("Zombie",20,15)
    print(e)
    # Creates an enemy with the name Zombie, health 20 and damage of 15
    w = Enemy("Warewolf", 15, 10)
    print(w)
    # Creates an enemy with the name Warewolf, health 15 and damage of 10
    print('Battle 1:')
    h.take_damage(w.damage)
    print(h)
    w.take_damage(10)
    print(w)
    # The first battle with the hero and the enemy
    print('Battle 2:')
    h.take_damage(e.damage)
    e.take_damage(20)
    print(h)
    print(e)
    # the second battle between the hero and the enemy
    h.restore_health(5)
    print('Restore Health:')
    print(h)
    # restores the heroes health by 5
    print('Inventory:')
    h.add_inventory('gold coin')
    h.add_inventory('candle')
    print(h.get_inventory())
    # This returns the inventory 
if __name__ == '__main__':
    main()
