from envelope import Envelope


class BaseStrategy(Envelope):
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
        found = 1# used to know if the user has chosen an envelope
        count = 0# used to know if it is the last envelope
        for envelope in self.env_arr:
            count += 1# to know if it is the last envelope
            print(envelope.display())# display the user the envelope's details
            found = input("enter the digit 1 if you have chosen the current envelope or anything else to continue with the searching")
            if int(found) == 1 and not envelope.used:# if the client has chosen the current envelope and it hasn't been used yet
                envelope.used = True# change the used statement so the envelope will not be used again
                return envelope# return the amount of money which is in the envelope
            if int(found) == 1:# if the client chose an envelope which was already opened
                print("this envelope was already opened, try the next one!")
            if count == 100:# if it is the last envelope
                envelope.used = True# change the used statement so the envelope will not be used again
                return envelope# return the amount of money which is in the envelope


class More_then_N_percent_group_strategy(Envelope):
    def init(self, env_arr):
        """constructor"""
        self.env_arr = env_arr# the envelopes list

    def play(self, N_of_maxes=3):
        """
        function that finds the envelope with the biggest amount of money by replacing the current max envelope since
        the start of the list n times
        :param N_of_maxes: how much times will the max will be replaced since the strategy has started running
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

            if times_max_was_changed < N_of_maxes:
                # checking if there is a new maximum since last one
                if envelope.money > max_sum_of_money:
                    max_sum_of_money = envelope.money
                    max_envelope = envelope
                    # one more maximum added - getting closer to N times maximum needs to change to stop
                    times_max_was_changed += 1
            # if the n of times to change max reached stop the loop - if that never happens and loop ends last maximum
            # will be returned
            else:
                break

        return max_envelope




