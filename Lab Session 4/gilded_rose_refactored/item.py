"""
item.py — Gilded Rose Inventory Item
=====================================
This module defines the Item class used to represent inventory items
in the Gilded Rose inn.

IMPORTANT: Do NOT modify this class during the refactoring exercise.
It belongs to the goblin in the corner who will instakill you if you
touch it (no shared code ownership policy applies here)!
"""


class Item:
    """
    Represents a single inventory item at the Gilded Rose inn.

    Attributes:
        name     (str): The descriptive name of the item.
        sell_in  (int): The number of days remaining in which the item
                        can still be sold.
        quality  (int): A numeric measure of how valuable the item is.
                        Valid range is 0–50.
    """

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        """Return an unambiguous string representation useful for debugging."""
        return (
            f"Item(name={self.name!r}, sell_in={self.sell_in}, quality={self.quality})"
        )

    def __eq__(self, other: object) -> bool:
        """
        Two Item objects are equal when all three fields match.

        This allows tests to compare items directly using ==, for example::

            assert updated_item == Item(name="Aged Brie", sell_in=4, quality=21)
        """
        if not isinstance(other, Item):
            return NotImplemented
        return (
            self.name == other.name
            and self.sell_in == other.sell_in
            and self.quality == other.quality
        )
