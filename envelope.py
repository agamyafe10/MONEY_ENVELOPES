import random


class Envelope:
    """
    creator: agam yafe
    """
    def __init__(self):
        """
        constructor
        :param: self
        """
        self._money = random.randrange(1, 101)# the amount of money in the envelope, if nothing is inserted it randoms the amount
        self._used = False# says if the envelope has been opened or not

    @property
    def money(self):
        """
        returns the amount of money which is in the envelope
        :param: self
        :returns: the object's money property
        """
        return self._money# return the money

    @money.setter
    def money(self, amount):
        """
        sets the money amount in the envelope
        :param: amount: an int
        """
        self._money = amount

    @property
    def used(self):
        """
        returns if the envelope was open or not
        :param: self
        :returns: the envelope's used property: a bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        sets the used statement to true if it was false, else print an alert
        :param: used: a bool
        """
        if not self._used:# if the envelope was not used yet
            self._used = used
        # else:# if the envelope was already used
        #     print("the envelope was already opened")

    def __repr__(self):
        return f'amount: {self._money}, used: {self._used}'

    @classmethod
    def display(cls):
        """
        returns the object's properties in a format string
        :param: self
        :returns: a formatted string: a string
        """
        return cls

    @staticmethod
    def play(self):
        """
        a function which meant to be override by the strategies classes
        :param: self
        :returns: an envelope on the other classes
        """
        print("an envelope can not be played by it self")

