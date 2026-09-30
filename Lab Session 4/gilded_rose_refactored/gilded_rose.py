"""
gilded_rose.py — Gilded Rose Inventory Update Logic
=====================================================
This module contains the daily inventory update logic for the Gilded Rose inn.

The update logic is intentionally written in an imperative style with nested
conditionals and a hard-to-follow structure. This is deliberate: the purpose
of this lab session is to first add comprehensive test cases and then safely
refactor the code into a cleaner design.

Design note: this implementation creates *new* Item objects rather than
mutating the originals. This means callers can safely compare the original
item with the returned item without worrying about hidden state changes.

Usage example::

    from item import Item
    from gilded_rose import GildedRose

    items = [
        Item("+5 Dexterity Vest",                     sell_in=10, quality=20),
        Item("Aged Brie",                              sell_in=2,  quality=0),
        Item("Elixir of the Mongoose",                 sell_in=5,  quality=7),
        Item("Sulfuras, Hand of Ragnaros",             sell_in=0,  quality=80),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        Item("Conjured Mana Cake",                     sell_in=3,  quality=6),
    ]

    updated = GildedRose.update_items(items)
    for i in updated:
        print(i)
"""

from item import Item


class GildedRose:
    """
    Manages the daily quality and sell_in updates for all inventory items
    at the Gilded Rose inn.

    The class has a single static method, ``update_items``.
    """

    @staticmethod
    def _increase_quality(item: Item, factor: int = 1) -> Item:
        return Item(item.name, item.sell_in, min(50, item.quality + factor))

    @staticmethod
    def _decrease_quality(item: Item, factor: int = 1) -> Item:
        return Item(item.name, item.sell_in, max(0, item.quality - factor))

    @staticmethod
    def _decrease_sell_in(item: Item) -> Item:
        return Item(item.name, item.sell_in - 1, item.quality)

    @staticmethod
    def update_items(items: list) -> list:
        result = []

        for item in items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                result.append(item)
                continue
            factor = 1 if item.sell_in > 0 else 2
            if item.name == "Aged Brie":
                item = GildedRose._increase_quality(item, factor)
            elif item.name.startswith("Conjured"):
                item = GildedRose._decrease_quality(item, 2 * factor)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item = Item(item.name, item.sell_in, 0)
                else:
                    item = GildedRose._increase_quality(item, max(1, 3 - (item.sell_in - 1) // 5))
            else:
                item = GildedRose._decrease_quality(item, factor)

            result.append(GildedRose._decrease_sell_in(item))

        return result
