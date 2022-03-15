def basic_strategy(player_total, dealer_value, soft):
    """ This is a simple implementation of Blackjack's
        basic strategy. It is used to recommend actions
        for the player. """

    if 4 <= player_total <= 8:
        return 'hit'
    if player_total == 9:
        if dealer_value in [1, 2, 7, 8, 9, 10]:
            return 'hit'
        return 'double'
    if player_total == 10:
        if dealer_value in [1, 10]:
            return 'hit'
        return 'double'
    if player_total == 11:
        if dealer_value == 1:
            return 'hit'
        return 'double'
    if soft:
        # we only double soft 12 because there's no splitting
        if player_total in [12, 13, 14]:
            if dealer_value in [5, 6]:
                return 'double'
            return 'hit'
        if player_total in [15, 16]:
            if dealer_value in [4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 17:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 18:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            if dealer_value in [2, 7, 8]:
                return 'stand'
            return 'hit'
        if player_total >= 19:
            return 'stand'

    else:
        if player_total == 12:
            if dealer_value in [1, 2, 3, 7, 8, 9, 10]:
                return 'hit'
            return 'stand'
        if player_total in [13, 14, 15, 16]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            return 'hit'

        if player_total >= 17:
            return 'stand'


def double_on_seven_or_8(player_total, dealer_value, soft):
    """ This is a deviation of Blackjack's
        basic strategy. In this deviation, we will
        double on seven or 8 if dealer is showing a six. """

    if 4 <= player_total <= 6:
        return 'hit'
    if player_total in [7, 8]:
        if dealer_value == 6:
            return 'double'
        return 'hit'
    if player_total == 9:
        if dealer_value in [1, 2, 7, 8, 9, 10]:
            return 'hit'
        return 'double'
    if player_total == 10:
        if dealer_value in [1, 10]:
            return 'hit'
        return 'double'
    if player_total == 11:
        if dealer_value == 1:
            return 'hit'
        return 'double'
    if soft:
        # we only double soft 12 because there's no splitting
        if player_total in [12, 13, 14]:
            if dealer_value in [5, 6]:
                return 'double'
            return 'hit'
        if player_total in [15, 16]:
            if dealer_value in [4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 17:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 18:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            if dealer_value in [2, 7, 8]:
                return 'stand'
            return 'hit'
        if player_total >= 19:
            return 'stand'

    else:
        if player_total == 12:
            if dealer_value in [1, 2, 3, 7, 8, 9, 10]:
                return 'hit'
            return 'stand'
        if player_total in [13, 14, 15, 16]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            return 'hit'

        if player_total >= 17:
            return 'stand'


def stand_on_sixteen(player_total, dealer_value, soft):
    """ This is a deviation of Blackjack's
        basic strategy. In this deviation, we will
        stand on 16 if dealer is showing 10. """

    if 4 <= player_total <= 8:
        return 'hit'
    if player_total == 9:
        if dealer_value in [1, 2, 7, 8, 9, 10]:
            return 'hit'
        return 'double'
    if player_total == 10:
        if dealer_value in [1, 10]:
            return 'hit'
        return 'double'
    if player_total == 11:
        if dealer_value == 1:
            return 'hit'
        return 'double'
    if soft:
        # we only double soft 12 because there's no splitting
        if player_total in [12, 13, 14]:
            if dealer_value in [5, 6]:
                return 'double'
            return 'hit'
        if player_total in [15, 16]:
            if dealer_value in [4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 17:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 18:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            if dealer_value in [2, 7, 8]:
                return 'stand'
            return 'hit'
        if player_total >= 19:
            return 'stand'

    else:
        if player_total == 12:
            if dealer_value in [1, 2, 3, 7, 8, 9, 10]:
                return 'hit'
            return 'stand'
        if player_total in [13, 14, 15]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            return 'hit'

        # optimal strategy says to hit hard 16 against 10, but doesn't take into account multi-card 16
        if player_total == 16:
            if dealer_value in [2, 3, 4, 5, 6, 10]:
                return 'stand'
            return 'hit'

        if player_total >= 17:
            return 'stand'
