from random import randint, choice
from flask import Flask, request, render_template


app = Flask(__name__)

def player_dice_throws(dice_1, dice_2):
    """
    Before each roll, give the player a choice.
    Let him choose 2 dice from the set: D3, D4, D6, D8, D10, D12, D20, D100.
    The dice can be repeated, or the player can use 2 different dice.
    :return:
    """
    chosen_dice_throw_1 = randint(1, int(dice_1))
    print(chosen_dice_throw_1)
    chosen_dice_throw_2 = randint(1, int(dice_2))
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


@app.route("/", methods=["GET", "POST"])
def rounds():
    """
     Each player starts with 0 points.
     On his turn, a player rolls 2 dice (standard six-sided dice).
     The number of points rolled is added to the total number of points.
     The first player to reach 2001 points wins.
     """
    if request.method == "GET":

        ctx = {
            'player_points': 0,
            'computer_points': 0,
            "round_player_points": 0,
            "round_computer_points": 0,
            "info": 'Start Game'
        }
        return render_template('home.html', ctx=ctx)
    if request.method == "POST":
        player_points = int(request.form['player_points'])
        computer_points = int(request.form['computer_points'])
        dice_1 = request.form['dice_1']
        dice_2 = request.form['dice_2']
        try:
            if player_points == 0 and computer_points == 0:
                round_player_points = player_dice_throws(dice_1, dice_2)
                player_points += round_player_points
                round_computer_points = computer_dice_throws()
                computer_points += round_computer_points
            elif player_points in range(0, 2000) and computer_points in range(0, 2000):
                round_player_points = player_dice_throws(dice_1, dice_2)
                player_points = round_2_check(round_player_points, player_points)
                round_computer_points = computer_dice_throws()
                computer_points = round_2_check(round_computer_points, computer_points)
            if player_points >= 2001:
                info = 'You win!'
                player_points = 0
                computer_points = 0
                round_player_points = 0
                round_computer_points = 0
            elif computer_points >= 2001:
                info = 'Computer win!'
                player_points = 0
                computer_points = 0
                round_player_points = 0
                round_computer_points = 0
            else:
                info = 'Try next round!'
        except UnboundLocalError:
            return render_template('home.html')
        ctx = {
            "player_points": player_points,
            "computer_points": computer_points,
            "round_player_points": round_player_points,
            "round_computer_points": round_computer_points,
            "info": info

        }
        return render_template('home.html', ctx=ctx)



if __name__ == "__main__":
    app.run(debug=True)
