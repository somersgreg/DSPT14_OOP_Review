import random
import time

# Classes are always upper Camel-case with first letter capped. DF, Series are also classes
class BaseCharacter:
    # First first always write doc string.
    # This says the parameter is 'name', its a string, and what it 'is'.
    """
    This is a base character model for our game.

    :param name: str - Name of the character
    """
    # Every class needs a constructor, dunder init, is first thing you need.
    # 'Self' is there so everything can be 'aware of everything else - worth researching.
    def __init__(self, name):
        # In the constructor using reflection (self) we instantiate the 'name' attribute.
        self.name = name
        # . . . as well as these attributes.
        self.level = 1

        random_stat = self._rollD20()
        self.intel = random_stat
        self.stam = random_stat
        self.strn = random_stat
        self.agi = random_stat

    def _rollD20(self):
        """An internal method which simulates the rolling of a 20-sided die"""

        print(f'Determining stats for {self.name}...')
        time.sleep(1)

        print('Rolling a 20-sided die...')
        time.sleep(2)

        die_value = random.randint(1, 20)
        print(f'Rolled a {die_value}!')

        return die_value

    def _rollD10(self):
        """An internal method which simulates the rolling of a 20-sided die"""

        print(f'Determining bonus stats for {self.name}...')
        time.sleep(1)

        print('Rolling a 10-sided die...')
        time.sleep(2)

        die_value = random.randint(1, 10)
        print(f'Rolled a {die_value}!')

        return die_value
    # (self, identifier = random.randint) to get a rnd default value.
    # Import random for this or `from random import randint`
    # generate an integer between 3 and 9 (inclusive range).
    # (see randrange for exclusive range)
    # print(randint(3, 9))
    def level_up(self, increment=1):
        """
        Levels up a character by an increment

        :param increment: int (default=1) - the number of levels to level up a character
        """
        # Exceptions: rnd must be greater or equal to 1
        if increment < 1:
            raise Exception('Parameter "increment" must be an integer greater than or equal to 1.')

        # We're getting a python dictionary of all the keys and values (self.name,self.int,etc) associated with self.
        # This is above stat_increase so it includes stat_increase.
        # dict_items = {'a':3, 'b':2, 'c':1} then
        # >>> dict_items.keys() gives dict_keys(['a', 'b', 'c'])
        # >>> dict_items.values() gives dict_values([3, 2, 1])
        # >>> dict_items.items() gives dict_keys([('a',3), ('b',2), ('c',1)])
        # which we need as its a iterable list of two variables, (k, v).
        # Also, if we enter `dict_items['b'] += 1` then b will = 3.
        dict_items = vars(self)
        # Each level stats increase 3 times the increment #
        stat_increase = 3 * increment
        # We create a for loop that will iterate the class attributes and increment the main stats (int,str,agi,...)
        # by stat_increase and the level, by the value of increment.
        for k, v in list(dict_items.items()):
            # if 'v'(value) is an int and 'k'(key) doesn't equal current level:
            if type(v) == int and k != 'level':
            # if its not an int like 'name' then do nothing till next elif.
                # Then we're going to increment that value by our stat increase which is 3x increment.
                dict_items[k] += stat_increase
            # Otherwise if its 'level' then we only raise that by 1x the increment.
            elif k == 'level':
                dict_items[k] += increment
            # 'name' doesnt get changed.

        self.__dict__.update(dict_items)

        if __name__ == '__main__':
            print(f'{self.name} has reached level {self.level}!')
            print(f'Intellect has increased by {stat_increase} to {self.intel}')
            print(f'Stamina has increased by {stat_increase} to {self.stam}')
            print(f'Strength has increased by {stat_increase} to {self.strn}')
            print(f'Agility has increased by {stat_increase} to {self.agi}')
        else:
            return self


class Mage(BaseCharacter):
    """A class that inherits from BaseCharacter"""

    def __init__(self, name):
        super().__init__(name)
        time.sleep(2)

        bonus_stats = self._rollD10()
        self.intel += bonus_stats  # -> self.intel = self.intel + bonus_stats
        self.stam += bonus_stats  # -> self.stam = self.stam + bonus_stats
        self.health = 50 + (self.stam * 5)
        self.mana = 80 + (self.intel * 5)

    def display_stats(self):
        print(f"{self.name}'s stats\n")
        print(f'\tTotal Health: {self.health}')
        print(f'\tTotal Mana:   {self.mana}')


if __name__ == '__main__':
    m0 = Mage('Jim')

    print(m0.__dict__)
