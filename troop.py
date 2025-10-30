class Troop:
    def __init__(self, points: int):
        self.points = points
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.points} points"

class Pikeman(Troop):
    def __init__(self):
        super().__init__(points=5)

class Archer(Troop):
    def __init__(self):
        super().__init__(points=10)

class Knight(Troop):
    def __init__(self):
        super().__init__(points=20)
