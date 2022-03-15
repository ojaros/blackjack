from hand import Hand
from strategy import basic_strategy, double_on_7or8, stand_on_sixteen


class Player():
    def __init__(self, name, bankroll):
        self.hand = Hand()
        self.bankroll = bankroll
        self.name = name
        self.bet = 0

    def play_hand(self, dealer_card, strat):
        while True:
            if strat == 'basic':
                recommend = basic_strategy(
                    self.hand.value(), dealer_card.value(), self.hand.is_soft())
            elif strat == 'double_on_7or8':
                recommend = double_on_7or8(
                    self.hand.value(), dealer_card.value(), self.hand.is_soft())
            elif strat == 'stand_on_sixteen':
                recommend = stand_on_sixteen(
                    self.hand.value(), dealer_card.value(), self.hand.is_soft())

            if len(self.hand.cards) == 2:
                move = recommend
            else:
                # for simplicity. This is not true for soft 18.
                if recommend == 'double':
                    recommend = 'hit'
                move = recommend

            if move.startswith('h'):
                return 'hit'
            elif move.startswith('s'):
                return 'stand'
            elif move.startswith('d'):
                return 'double'

            print "Invalid move"

    def __str__(self):
        return '(%s, $%s)' % (self.name, self.bankroll)

    def is_bust(self):
        return self.hand.value() > 21
