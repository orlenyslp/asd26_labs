"""
test_bowling.py — TDD test suite for the Bowling Game.
─────────────────────────────────────────────────────────────────────────────
HOW TO USE THIS FILE
─────────────────────────────────────────────────────────────────────────────
1. Keep all tests SKIPPED at the start — run pytest and confirm you see
   "5 skipped" and nothing else.

2. Enable tests ONE AT A TIME, strictly top-to-bottom:
   Remove (or comment out) the @pytest.mark.skip decorator for ONE test.

3. Run:  pytest test_bowling.py -v
   The enabled test must be RED (FAILED) before you write any code.
   If it is already green, something is wrong.

4. Write the minimum code in bowling.py to turn it GREEN.

5. Once GREEN, leave that test enabled and move to the next one.
   Never re-skip a passing test.

"""

import pytest
from bowling import score


# ── Step 1 ───────────────────────────────────────────────────────────────────

#@pytest.mark.skip(reason="Step 1 — enable first")
def test_gutter_game():
    """
    US-1: A player who misses every shot scores 0.

    The game: 20 rolls, all zeros.
    Each frame: [0, 0]. The 10th frame: [0, 0, None].

    TDD nudge: what is the simplest implementation of score() that
    makes this test pass? Start there — do not guess ahead.
    """
    game = [[0, 0]] * 9 + [[0, 0, None]]
    assert score(game) == 0


# ── Step 2 ───────────────────────────────────────────────────────────────────

#@pytest.mark.skip(reason="Step 2 — enable after Step 1 is GREEN")
def test_all_ones():
    """
    US-2: Knocking down one pin per roll across 20 turns scores 20.

    The game: 20 rolls, each knocking down 1 pin.
    Each frame: [1, 1]. The 10th frame: [1, 1, None].

    TDD nudge: your Step 1 implementation can no longer just return a
    constant. What does the test output tell you to do?
    """
    game = [[1, 1]] * 9 + [[1, 1, None]]
    assert score(game) == 20


# ── Step 3 ───────────────────────────────────────────────────────────────────

#@pytest.mark.skip(reason="Step 3 — enable after Step 2 is GREEN")
def test_one_spare():
    """
    US-3: A spare earns a bonus equal to the first roll of the next frame.

    The game:
      Frame 1: [5, 5]   → spare (5 + 5 = 10), bonus = first roll of frame 2
      Frame 2: [3, 0]   → first roll is 3, so frame 1 scores 10 + 3 = 13
      Frames 3–9: [0, 0]
      Frame 10: [0, 0, None]

    Expected: 13 + 3 + 0 + ... = 16

    TDD nudge: your Step 2 implementation gives 13 (just the sum of rolls),
    not 16. It does not know about spares. The test failure is telling you
    that score() must now detect spares and look ahead to the next roll.
    """
    game = [[5, 5], [3, 0]] + [[0, 0]] * 7 + [[0, 0, None]]
    assert score(game) == 16


# ── Step 4 ───────────────────────────────────────────────────────────────────

#@pytest.mark.skip(reason="Step 4 — enable after Step 3 is GREEN")
def test_one_strike():
    """
    US-4: A strike earns a bonus equal to the next two rolls.

    The game:
      Frame 1: [10, None]  → strike, bonus = next two rolls (3 + 4 = 7)
                             frame 1 scores 10 + 3 + 4 = 17
      Frame 2: [3, 4]      → frame 2 scores 3 + 4 = 7
      Frames 3–9: [0, 0]
      Frame 10: [0, 0, None]

    Expected: 17 + 7 + 0 + ... = 24

    TDD nudge: notice that a strike uses only ONE roll slot in the flat list
    (the None is not a real roll). This affects how you advance your index
    when scanning through rolls.
    """
    game = [[10, None], [3, 4]] + [[0, 0]] * 7 + [[0, 0, None]]
    assert score(game) == 24


# ── Step 5 ───────────────────────────────────────────────────────────────────

#@pytest.mark.skip(reason="Step 5 — enable after Step 4 is GREEN")
def test_perfect_game():
    """
    US-5: A player who strikes on every roll scores 300 (the perfect game).

    The game:
      Frames 1–9: [10, None]   → all strikes
      Frame 10:   [10, 10, 10] → three bonus rolls awarded in the 10th frame

    Each of frames 1–9 scores 10 + 10 + 10 = 30.
    Frame 10 scores 10 + 10 + 10 = 30 (no forward bonus applied).
    Total: 9 × 30 + 30 = 300.

    TDD nudge: frame 10 must be treated as a special case — it has no
    'next frame' to look ahead to. Its bonus rolls are already inside the
    frame itself.
    """
    game = [[10, None]] * 9 + [[10, 10, 10]]
    assert score(game) == 300

def test_two_strike():
    game = [[10, None], [10, None], [3, 4]] + [[0, 0]] * 6 + [[0, 0, None]]
    assert score(game) == 47