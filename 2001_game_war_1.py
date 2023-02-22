from random import randint, choice


def player_dice_throws():
    """
    Before each roll, give the player a choice.
    Let him choose 2 dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.
    The dice can be repeated, or the player can use 2 different dice.
    Let the choice of dice be done by entering the appropriate string of characters (one for each dice) by the player.
    :return:
    """
    dice_types = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    dice_one = input("Choose the type of dice 1: D3, D4, D6, D8, D10, D12, D20, D100")
    dice_two = input("Choose the type of dice 2: D3, D4, D6, D8, D10, D12, D20, D100")
    while dice_one not in dice_types:
        dice_one = input("Choose again the correct type of dice 1: D3, D4, D6, D8, D10, D12, D20, D100")
    while dice_two not in dice_types:
        dice_two = input("Choose again the correct type of dice 2: D3, D4, D6, D8, D10, D12, D20, D100")
    chosen_dice_throw_1 = randint(1, int(dice_one[1::]))
    print(chosen_dice_throw_1)
    chosen_dice_throw_2 = randint(1, int(dice_two[1::]))
    print(chosen_dice_throw_2)
    return sum([chosen_dice_throw_1, chosen_dice_throw_2])


def computer_dice_throws():
    """
    Two throws in range of random dice type
    :return: int
    """
    return sum([randint(1, choice([3, 4, 6, 8, 10, 12, 20, 100])) for _ in range(2)])


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
            player_points += player_dice_throws()
            computer_points += computer_dice_throws()
        elif player_points in range(0, 2000) and computer_points in range(0, 2000):
            round_player_points = player_dice_throws()
            player_points = round_2_check(round_player_points, player_points)
            round_computer_points = computer_dice_throws()
            computer_points = round_2_check(round_computer_points, computer_points)

        print(f'Player points {player_points}')
        print(f'Computer points {computer_points}')
    if player_points >= 2001:
        print('You win!')
    elif computer_points >= 2001:
        print('Computer win!')


if __name__ == "__main__":
    rounds()
