class Envelope:
    def __init__(self, money):
        """constructor"""
        self.money = money
        self.used = False

    @property
    def money(self):
        """returns the amount of money which is in the envelope"""
        return self._money# return the money

    @money.setter
    def money(self, amount):
        """sets the money amount in the envelope"""
        self._money = amount

    @property
    def used(self):
        """returns if the envelope was open or not"""
        return self._used

    @used.setter
    def used(self, used):
        """sets the used statement"""
        if not self._used:# if the envelope was not used yet
            self._used = used
        else:# if the envelope was already used
            print("the envelope was already opened")

    def display(self):
        """returns the object's properties in a format string"""
        return f'amount: {self.money}, used: {self.used}'
