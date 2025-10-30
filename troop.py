class Troop:
    def __init__(self, points: int):
        self.points = points

    def training_cost(self) -> int:
        raise NotImplementedError("Subclasses must implement training_cost()")

    def train(self) -> None:
        raise NotImplementedError("Subclasses must implement train()")
    
    def promotion_cost(self) -> int:
        raise NotImplementedError("Subclasses must implement promotion_cost()")
    
    def promote(self):
        raise NotImplementedError("Subclasses must implement promote()")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.points} points"

class Pikeman(Troop):
    def __init__(self):
        super().__init__(points=5)
    
    def training_cost(self) -> int:
        return 10

    def train(self) -> None:
        self.points += 3
    
    def promotion_cost(self) -> int:
        return 30
    
    def promote(self) -> Troop:
        return Archer()

class Archer(Troop):
    def __init__(self):
        super().__init__(points=10)
    
    def training_cost(self) -> int:
        return 20

    def train(self) -> None:
        self.points += 7
    
    def promotion_cost(self) -> int:
        return 40
    
    def promote(self) -> Troop:
        return Knight()

class Knight(Troop):
    def __init__(self):
        super().__init__(points=20)

    def training_cost(self) -> int:
        return 30

    def train(self) -> None:
        self.points += 10
    
    def promotion_cost(self):
        raise Exception("Knights cannot be promoted")
    
    def promote(self):
        raise Exception("Knights cannot be promoted")
