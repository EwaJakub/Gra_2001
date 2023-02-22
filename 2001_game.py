from random import randint


def dice_throws():
    """
    Gives summary of values, of 2 random six sides dice throws
    :return: int summary value
    """
    return sum([randint(1, 6) for _ in range(2)])


def round_2_check(round_points, total_points):
    """
    If the player rolls a 7, he divides his number of points by this value, discarding the fractional part,
    If he rolls 11, he multiplies the current number of points by this value.
    :param round_points: int
    :param total_points: int
    :return: int
    """
    if round_points == 7:
        total_points //= 7
    elif round_points == 11:
        total_points *= 11
    else:
        total_points += round_points
    return total_points


def rounds():
    """
    Each player starts with 0 points.
    On his turn, a player rolls 2 dice (standard six-sided dice).
    The number of points rolled is added to the total number of points.
    The first player to reach 2001 points wins.
    """
    player_points = 0
    computer_points = 0
    while player_points < 2001 and computer_points < 2001:
        input('Press ENTER to roll the dice')
        if player_points == 0 and computer_points == 0:
            player_points += dice_throws()
            computer_points += dice_throws()
        elif player_points in range(0, 2000) and computer_points in range(0, 2000):
            round_player_points = dice_throws()
            player_points = round_2_check(round_player_points, player_points)
            round_computer_points = dice_throws()
            computer_points = round_2_check(round_computer_points, computer_points)
        print(f'Player points {player_points}')
        print(f'Computer points {computer_points}')
    if player_points >= 2001:
        print('You win!')
    elif computer_points >= 2001:
        print('Computer win!')


if __name__ == "__main__":
    rounds()
