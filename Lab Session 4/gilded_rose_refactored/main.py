"""
main.py — Gilded Rose Demo
===========================
A short demonstration script showing how the GildedRose.update_items function
works across one day of inventory updates.

Run this script to see one day's worth of inventory updates:

    python main.py
"""

from item import Item
from gilded_rose import GildedRose


def main():
    # Build the standard Gilded Rose inventory from the requirements example.
    items = [
        Item("+5 Dexterity Vest",                        sell_in=10, quality=20),
        Item("Aged Brie",                                sell_in=2,  quality=0),
        Item("Elixir of the Mongoose",                   sell_in=5,  quality=7),
        Item("Sulfuras, Hand of Ragnaros",               sell_in=0,  quality=80),
        Item("Backstage passes to a TAFKAL80ETC concert",sell_in=15, quality=20),
        Item("Conjured Mana Cake",                       sell_in=3,  quality=6),
    ]

    print("=== Gilded Rose — Inventory Update Demo ===\n")
    print(f"{'Item':<52} {'sell_in':>8} {'quality':>8}")
    print("-" * 70)

    print("BEFORE:")
    for item in items:
        print(f"  {item.name:<50} {item.sell_in:>8} {item.quality:>8}")

    updated = GildedRose.update_items(items)

    print("\nAFTER (one day later):")
    for item in updated:
        print(f"  {item.name:<50} {item.sell_in:>8} {item.quality:>8}")


if __name__ == "__main__":
    main()
