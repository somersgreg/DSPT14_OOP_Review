import random


class Product:

    """
    This is the base model to which all item attributes apply.

    :param name: str - Name of the item.
    """

    # def __init__(self, name):
    #     self.name = name
    #     self.price = 10
    #     self.weight = 20
    #     self.flammability = 0.5
    #     self.identifier = random.randint(1000000, 9999999)

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """An internal method which estimates likelihood of theft"""
        dear = self.price / self.weight
        if dear < 0.5:
            print("Not so stealable...")
        elif dear >= 0.5 < 1.0:
            print("Kinda stealable.")
        else:
            print("Very stealable!")


    def explode(self):
        """Safety check method"""

        if self.flammability * self.weight < 10:
            print("...fizzle")
        elif self.flammability * self.weight > 9 < 50:
            time.sleep(1)
            print("...boom!")
        else:
            time.sleep(2)
            print("...BABOOM!!")

class BoxingGlove(Product):
    """
    This is a subclass of the Product class.

    :param < >: <type> - <description>
    """
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10

    def explode(self):
        """You know. . . for kids!"""
        print("...it's a glove.")

    def punch(self):
        """Punch method"""
        if self.weight < 5:
            print("That tickles.")
        elif self.weight >= 4 < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")

