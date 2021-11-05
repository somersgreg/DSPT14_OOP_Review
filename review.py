import random
import time


class BaseCharacter:
    """
    This is a base character model for our game.

    :param name: str - Name of the character
    """

    def __init__(self, name):
        self.name = name
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

    def level_up(self, increment=1):
        """
        Levels up a character by an increment

        :param increment: int (default=1) - the number of levels to level up a character
        """
        if increment < 1:
            raise Exception('Parameter "increment" must be an integer greater than or equal to 1.')

        dict_items = vars(self)
        stat_increase = 3 * increment

        for k, v in list(dict_items.items()):
            if type(v) == int and k != 'level':
                dict_items[k] += stat_increase
            elif k == 'level':
                dict_items[k] += increment

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
