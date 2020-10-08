from envelope import Envelope
import random


class BaseStrategy(Envelope):
    """
    creator: agam yafe
    first strategy- passes one by one
    """
    def __init__(self, env_arr):
        """
        constructor: new envelope
        :param env_arr: envelopes' list
        """
        self.env_arr = env_arr# the envelopes list

    def play(self):
        """
        passes one by one on the envelopes list until the clients chooses an envelope, return the sum of money which was in the envelope
        :param: self
        :returns: the envelope the client has chosen
        """
        count = 0# used to know if it is the last envelope
        last_envelope_not_used = len(self.env_arr)-1# the index of the last envelope
        for i in range(last_envelope_not_used, -1, -1):# check for the last envelope which was not opened
            if not self.env_arr[i].used:# if the envelope was not opened save the index
                last_envelope_not_used = i
                break
            if i == 0:# if we have reached the first envelope and it was used too
                print("all the envelopes have been opened")
                return# quit the function we do not have any envelopes to ork with
        for envelope in self.env_arr:
            count += 1# to know if it is the last envelope
            if envelope.used:# if the envelope was already opened
                continue# skip to the next envelope
            print(envelope)# display the user the envelope's details
            envelope.used = True  # change the used statement so the envelope will not be used again
            found = input("enter the digit 1 if you have chosen the current envelope else: press any other key ")
            if found == '1':# if the client has chosen the current envelope and it hasn't been used yet
                return envelope# return the amount of money which is in the envelope
            if count == last_envelope_not_used+1:# if it is the last envelope which is not opened yet
                print("this was the last envelope which was not opened")
                return envelope# return the amount of money which is in the envelope


class N_max_strategy(Envelope):
    """
    creator: ariel chitiat
    passes over the envelope and changes N times the last max value that was found
    """
    def __init__(self, env_arr):
        """constructor"""
        self.env_arr = env_arr# the envelopes list
        self._N = 3# the number of times the strategy play() function will replace the max value

    @property
    def N(self):
        """
        :return: the N property
        """
        return self._N

    @N.setter
    def N(self, N):
        """
        sets the N value
        :param N: an int
        """
        if N > 0:
            self._N = N
        else:
            raise ValueError("you can not run the function with a negative or 0 number")

    def play(self):
        """
        function that finds the envelope with the biggest amount of money by replacing the current max envelope since
        the start of the list n times
        :return: the envelope with biggest amount of money after n times of replacing the max
        """

        # the biggest amount found - for start 0
        max_sum_of_money = 0
        # the envelope with the biggest amount of money that was found - just for start random envelope for sure will be
        # replaced
        max_envelope = Envelope()
        # the number of times that the max had changed - for start 0
        times_max_was_changed = 0

        for envelope in self.env_arr:
            if times_max_was_changed < self.N:
                # checking if the envelope was not opened
                if not envelope.used:
                    envelope.used = True
                    # checking if there is a new maximum since last one
                    if envelope.money > max_sum_of_money:
                        max_sum_of_money = envelope.money
                        max_envelope = envelope
                        # one more maximum changed - getting closer to N times maximum needs to change to stop
                        times_max_was_changed += 1
            # if the n of times to change max reached stop the loop - if that never happens and loop ends last maximum
            # will be returned
            else:
                break

        return max_envelope


class Automatic_BaseStrategy(Envelope):
    """
    creator: yoav levin
    returns a random envelope
    """
    def __init__(self, env_arr):
        """constructor"""
        self.env_arr = env_arr# the envelopes list

    def play(self):
        """
        choose a random envelope
        :param: self
        :return: a random envelope
        """

        x = random.randrange(0, 100)# the random index of an envelope

        while self.env_arr[x].used:
            x = random.randrange(0, 100)# the random index of an envelope

        self.env_arr[x].used = True# change the used statement so the envelope will not be used again
        return self.env_arr[x]


class More_then_N_percent_group_strategy(Envelope):
    """
    creator: yoav levin
    finding the maximum value in the part the client inserted, and pass over the rest envelopes, if there is a better envelope
    """
    def __init__(self, env_arr):
        """constructor"""
        self.env_arr = env_arr  # the envelopes list
        self._percent = 0.25# the group size

    @property
    def percent(self):
        """
        :return: the percent property
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """
        sets the percent value
        :param percent: an int
        """
        percent = round(percent, 2)# round the number to prevent errors
        self._percent = percent

    def play(self, percent_num=0.25):
        """
        The user choose percent of envelopes to open, and in them he finds the maximum amount of money.
        After he finished opening them, he open the rest of the envelopes, and he choose the first envelope with more money than the maximum price
        :param percent_num: the percent of envelopes that will open automatically
        :return: envelope object
        """
        envelopes_to_open = percent_num * 100# find the amount of envelopes to open
        max_money = 0# the max amount of money, now 0
        open_count = 0# find how many envelopes were opened

        for envelope in self.env_arr:
            open_count += 1# updating the number of envelopes that were opened
            if open_count < envelopes_to_open:# if the percent of envelopes the user asked to open first weren't open already
                envelope.used = True# submit it was open
                if envelope.money > max_money:
                    max_money = envelope.money# update the max money sum
            else:# if the percent of envelopes the user asked to open first were open already
                envelope.used = True# submit it was open
                if envelope.money > max_money:# if we found the one with more money then the max one
                    return envelope
            if open_count == 100:# if he didn't found an envelope with more money, the last one has to be returned
                return envelope