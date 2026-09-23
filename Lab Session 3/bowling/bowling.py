"""
bowling.py — Starter file for the Bowling Game TDD lab.
─────────────────────────────────────────────────────────────────────────────
Do NOT read ahead in test_bowling.py.
Enable one test at a time and let the failing test tell you what to do next.
─────────────────────────────────────────────────────────────────────────────

DATA STRUCTURE
──────────────
A bowling game is represented as a list of 10 frames:

    game = [frame_1, frame_2, ..., frame_10]

Frames 1–9 are two-element lists:
    [roll1, roll2]

    Normal frame : [4, 3]          roll1 + roll2 < 10
    Strike frame : [10, None]      all 10 pins on the first roll;
                                   second slot is None (no roll was taken)

Frame 10 is a three-element list:
    [roll1, roll2, bonus_roll]

    bonus_roll is None when the player earns no bonus roll.

Quick reference:
    gutter_game  = [[0, 0]] * 9 + [[0, 0, None]]
    all_ones     = [[1, 1]] * 9 + [[1, 1, None]]
    one_spare    = [[5, 5], [3, 0]] + [[0, 0]] * 7 + [[0, 0, None]]
    one_strike   = [[10, None], [3, 4]] + [[0, 0]] * 7 + [[0, 0, None]]
    perfect_game = [[10, None]] * 9 + [[10, 10, 10]]
"""


def score(game):
    """
    Calculates the total score for a bowling game.

    Parameters
    ----------
    game : list of lists
        10 frames as described in the module docstring above.

    Returns
    -------
    int
        Total score for the game, including all strike and spare bonuses.
    """
    all_rolls = [roll for rolls in game for roll in rolls if roll is not None]
    i = 0
    total = 0
    for frame in range(10):
        if all_rolls[i] == 10:
            total += sum(all_rolls[i:i+3])
            i += 1
        else:
            f_sum = sum(all_rolls[i:i+2])
            if f_sum == 10:
                total += 10 + all_rolls[i+2]
            else:
                total += f_sum
            i += 2
    return total