from troop import Troop

class Army:
    def __init__(self, name: str, troops: list[Troop] | None = None):
        self.name = name
        self.coins = 1000
        self.troops = troops if troops is not None else []

    def total_points(self) -> int:
        """Calculate total points of all troops."""
        return sum(t.points for t in self.troops)

    def __str__(self):
        return f"{self.name}"
