from army import Army
from troop import Archer, Pikeman, Knight


class Civilization:
    """Factory class that generates armies based on civilization name."""

    @staticmethod
    def create_army(civ_name: str, army_name: str) -> Army:
        civ_name = civ_name.lower()

        if civ_name == "chinese":
            troops = [Pikeman() for _ in range(2)] + \
                     [Archer() for _ in range(25)] + \
                     [Knight() for _ in range(2)]

        elif civ_name == "english":
            troops = [Pikeman() for _ in range(10)] + \
                     [Archer() for _ in range(10)] + \
                     [Knight() for _ in range(10)]

        elif civ_name == "byzantine":
            troops = [Pikeman() for _ in range(5)] + \
                     [Archer() for _ in range(8)] + \
                     [Knight() for _ in range(15)]

        else:
            raise ValueError(f"Unknown civilization: {civ_name}")

        return Army(name=army_name, troops=troops)
