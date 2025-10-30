from troop import Troop

class Army:
    def __init__(self, name: str, troops: list[Troop] | None = None):
        self.name = name
        self.coins = 1000
        self.troops = troops if troops is not None else []
        self.history = []

    def total_points(self) -> int:
        """Calculate total points of all troops."""
        return sum(t.points for t in self.troops)

    def train_troop(self, index: int) -> str:
        """Train a single troop at position `index`."""
        if index < 0 or index >= len(self.troops):
            raise IndexError("Invalid troop index")
        
        cost = self.troops[index].training_cost()

        if (self.coins < cost):
            return f"Not enough coins to train: {self.troops[index]}"

        self.troops[index].train()
        self.coins -= cost
        return f"Succesfully trained: {self.troops[index]}"

    def __str__(self):
        return f"{self.name}"

def battle(army1: Army, army2: Army) -> str:
    points1 = army1.total_points()
    points2 = army2.total_points()

    if points1 == points2:
        # Tie: both lose their highest troop
        for army in (army1, army2):
            if army.troops:
                army.troops.sort(key=lambda t: t.points, reverse=True)
                removed = army.troops.pop(0)
                army.history.append(f"Tied with {army2.name if army == army1 else army1.name}, lost {removed}")
        return f"Battle tied between {army1.name} and {army2.name}"

    winner, loser = (army1, army2) if points1 > points2 else (army2, army1)
    winner.coins += 100

    # Loser loses two highest troops
    loser.troops.sort(key=lambda t: t.points, reverse=True)
    removed = loser.troops[:2]
    loser.troops = loser.troops[2:]

    # Update history
    winner.history.append(f"Won against {loser.name}")
    loser.history.append(f"Lost to {winner.name} and lost {', '.join(str(t) for t in removed)}")

    return f"{winner.name} wins the battle against {loser.name}"
