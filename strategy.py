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