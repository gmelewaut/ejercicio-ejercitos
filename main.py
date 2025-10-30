from civilization import Civilization
from army import battle

if __name__ == "__main__":
    army1 = Civilization.create_army("Chinese", "Red Dragons")
    army2 = Civilization.create_army("English", "Lionhearts")
    army3 = Civilization.create_army("Byzantine", "Imperial Guard")
    army4 = Civilization.create_army("Chinese", "Red Dragons 2")


    print(battle(army1, army4))

    print(army1.promote_troop(0))
    print(army1.promote_troop(0))
    print(army1.promote_troop(0))
    print(army1.train_troop(0))
    print(army1.train_troop(0))
    print(army1.train_troop(0))
    print(army1.train_troop(3))
    print(army1.train_troop(27))


    print(battle(army1, army2))
    print(battle(army1, army3))
    print(battle(army2, army3))
    print(army1, army1.history)
    print(army2, army2.history)
    print(army3, army3.history)
    print(army4, army4.history)


