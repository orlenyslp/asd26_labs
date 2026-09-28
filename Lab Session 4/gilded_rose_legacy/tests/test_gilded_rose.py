"""
test_gilded_rose.py — Gilded Rose Test Suite
=============================================
This module is where you will write your test cases for the GildedRose
inventory system.  Each test case should correspond to one business
requirement from the Gilded Rose requirements specification in Section 2.1
of the lab handout.

Running the tests
-----------------
Run all tests::

    pytest tests/test_gilded_rose.py -v

Run with line and branch coverage::

    pytest tests/test_gilded_rose.py --cov=gilded_rose --cov-branch --cov-report=html -v

Open htmlcov/index.html in a browser to view the coverage report.
"""

import pytest
from gilded_rose import GildedRose
from item import Item


class TestGildedRose:
    """
    Test class for GildedRose.update_items.

    Write one test method per requirement listed in Section 3.2 of the lab
    handout.  Name each test so that the method name reads as a plain-English
    description of the requirement being tested, for example::

        def test_quality_of_item_is_never_negative(self):
            ...
    """

    # ------------------------------------------------------------------
    # Starter test — provided as a worked example.
    # Add your own tests below this one.
    # ------------------------------------------------------------------

    def test_at_end_of_day_system_lowers_both_values_for_every_item(self):
        """
        Requirement: At the end of each day our system lowers both values
        for every item.
        """
        item = Item("+5 Dexterity Vest", sell_in=10, quality=20)
        # Pass a single-element list and unpack the single result.
        [updated_item] = GildedRose.update_items([item])

        assert updated_item.sell_in == item.sell_in - 1
        assert updated_item.quality == item.quality - 1

    # ------------------------------------------------------------------
    # Add your tests here (Task 1)
    # ------------------------------------------------------------------

    def test_once_sell_by_date_passed_quality_degrades_twice_as_fast(self):
        items = [
            Item("+5 Dexterity Vest", sell_in=0, quality=20),
            Item("+5 Dexterity Vest", sell_in=-2, quality=20),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            ("+5 Dexterity Vest", -1, 18),
            ("+5 Dexterity Vest", -3, 18),
        ]

    def test_quality_of_item_is_never_negative(self):
        items = [
            Item("+5 Dexterity Vest", sell_in=0, quality=1),
            Item("+5 Dexterity Vest", sell_in=5, quality=0),
            Item("+5 Dexterity Vest", sell_in=0, quality=0),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            ("+5 Dexterity Vest", -1, 0),
            ("+5 Dexterity Vest", 4, 0),
            ("+5 Dexterity Vest", -1, 0),
        ]

    def test_aged_brie_increases_in_quality_the_older_it_gets(self):
        items = [
            Item("Aged Brie", sell_in=0, quality=10),
            Item("Aged Brie", sell_in=5, quality=20),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            ("Aged Brie", -1, 12),
            ("Aged Brie", 4, 21),
        ]

    def test_quality_of_item_is_never_more_than_50(self):
        items = [
            Item("Aged Brie", sell_in=0, quality=49),
            Item("Aged Brie", sell_in=-2, quality=50),
            Item("Aged Brie", sell_in=5, quality=50),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            ("Aged Brie", -1, 50),
            ("Aged Brie", -3, 50),
            ("Aged Brie", 4, 50),
        ]

    def test_sulfuras_never_has_to_be_sold_or_decreases_in_quality(self):
        name = "Sulfuras, Hand of Ragnaros"
        items = [
            Item(name, sell_in=0, quality=49),
            Item(name, sell_in=-2, quality=24),
            Item(name, sell_in=5, quality=10),
        ]

        result = GildedRose.update_items(items)

        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 0, 49),
            (name, -2, 24),
            (name, 5, 10),
        ]

    def test_backstage_passes_increase_quality_as_sellin_approaches(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(name, sell_in=56, quality=50),
            Item(name, sell_in=11, quality=26),
        ]

        result = GildedRose.update_items(items)

        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 55, 50),
            (name, 10, 27),
        ]

    def test_backstage_passes_quality_increases_by_2_when_10_days_or_less(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(name, sell_in=10, quality=26),
            Item(name, sell_in=8, quality=26),
            Item(name, sell_in=6, quality=26),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 9, 28),
            (name, 7, 28),
            (name, 5, 28),
        ]
        items = [
            Item(name, sell_in=8, quality=49),
            Item(name, sell_in=10, quality=50),
            Item(name, sell_in=6, quality=48),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 7, 50),
            (name, 9, 50),
            (name, 5, 50),
        ]

    def test_backstage_passes_quality_increases_by_3_when_5_days_or_less(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(name, sell_in=1, quality=45),
            Item(name, sell_in=5, quality=46),
            Item(name, sell_in=3, quality=20),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 0, 48),
            (name, 4, 49),
            (name, 2, 23),
        ]
        items = [
            Item(name, sell_in=1, quality=49),
            Item(name, sell_in=5, quality=50),
            Item(name, sell_in=4, quality=48),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, 0, 50),
            (name, 4, 50),
            (name, 3, 50),
        ]

    def test_backstage_passes_quality_drops_to_0_after_the_concert(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        items = [
            Item(name, sell_in=0, quality=50),
            Item(name, sell_in=-3, quality=47),
            Item(name, sell_in=-3, quality=20),
        ]
        result = GildedRose.update_items(items)
        assert [(i.name, i.sell_in, i.quality) for i in result] == [
            (name, -1, 0),
            (name, -4, 0),
            (name, -4, 0),
        ]

    # ------------------------------------------------------------------
    # Conjured items — skipped until Task 3 (do not modify)
    # ------------------------------------------------------------------

    @pytest.mark.skip(
        reason=(
            "Conjured items not yet implemented. "
            "Implement the Conjured item behaviour in gilded_rose.py, "
            "then remove this decorator."
        )
    )
    def test_conjured_items_degrade_in_quality_twice_as_fast_as_normal_items(self):
        """
        Requirement: "Conjured" items degrade in Quality twice as fast as
        normal items.

        This test is skipped because the feature has not been implemented yet.
        Come back to this after completing the refactoring in Task 3.
        """
        name_base = "Conjured Mana Cake"

        # --- Quality floor: result must be 0, never negative ---
        items_floor = [
            Item(name_base,       sell_in=0,  quality=3),
            Item(name_base + "1", sell_in=-3, quality=0),
            Item(name_base + "2", sell_in=4,  quality=1),
        ]
        result_floor = GildedRose.update_items(items_floor)
        assert result_floor == [Item(i.name, i.sell_in - 1, 0) for i in items_floor]

        # --- Post sell-by: degrade by 4 per day ---
        items_post = [
            Item(name_base, sell_in=0,  quality=10),
            Item(name_base, sell_in=-2, quality=33),
        ]
        result_post = GildedRose.update_items(items_post)
        assert result_post == [Item(i.name, i.sell_in - 1, i.quality - 4) for i in items_post]

        # --- Before sell-by: degrade by 2 per day ---
        items_pre = [
            Item(name_base, sell_in=6,  quality=10),
            Item(name_base, sell_in=45, quality=33),
        ]
        result_pre = GildedRose.update_items(items_pre)
        assert result_pre == [Item(i.name, i.sell_in - 1, i.quality - 2) for i in items_pre]
