from abc import ABC, abstractmethod

# --------------------------------------------------------------------------
# 1. Abstract Products
# --------------------------------------------------------------------------
class Knight(ABC):
    """Abstract Product A"""
    @abstractmethod
    def attack(self) -> None:
        pass

class Mage(ABC):
    """Abstract Product B"""
    @abstractmethod
    def cast_spell(self) -> None:
        pass

# --------------------------------------------------------------------------
# 2. Concrete Products (Fire Theme)
# --------------------------------------------------------------------------
class FireKnight(Knight):
    def attack(self) -> None:
        print("Fire Knight strikes with a flaming sword! (Burn Damage)")

class FireMage(Mage):
    def cast_spell(self) -> None:
        print("Fire Mage casts a fireball! (Explosion)")

# --------------------------------------------------------------------------
# 3. Concrete Products (Ice Theme)
# --------------------------------------------------------------------------
class IceKnight(Knight):
    def attack(self) -> None:
        print("Ice Knight strikes with a frost blade! (Slow Effect)")

class IceMage(Mage):
    def cast_spell(self) -> None:
        print("Ice Mage casts a blizzard! (Area Freeze)")

# --------------------------------------------------------------------------
# 4. Abstract Factory
# --------------------------------------------------------------------------
class UnitFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products.
    """
    @abstractmethod
    def create_knight(self) -> Knight:
        pass

    @abstractmethod
    def create_mage(self) -> Mage:
        pass

# --------------------------------------------------------------------------
# 5. Concrete Factories
# --------------------------------------------------------------------------
class FireUnitFactory(UnitFactory):
    def create_knight(self) -> Knight:
        return FireKnight()

    def create_mage(self) -> Mage:
        return FireMage()

class IceUnitFactory(UnitFactory):
    def create_knight(self) -> Knight:
        return IceKnight()

    def create_mage(self) -> Mage:
        return IceMage()

# --------------------------------------------------------------------------
# 6. Client Code
# --------------------------------------------------------------------------
def spawn_and_activate_army(factory: UnitFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types (ABCs). This allows you to pass any factory or product subclass.
    """
    # Create units using the factory
    knight = factory.create_knight()
    mage = factory.create_mage()

    # Use the units
    knight.attack()
    mage.cast_spell()

if __name__ == "__main__":
    print("=== Abstract Factory Pattern Demo ===\n")

    # Scenario 1: The user selects the Fire Faction
    print("[System] Spawning Fire Faction units...")
    fire_factory = FireUnitFactory()
    spawn_and_activate_army(fire_factory)

    print()

    # Scenario 2: The user selects the Ice Faction
    print("[System] Spawning Ice Faction units...")
    ice_factory = IceUnitFactory()
    spawn_and_activate_army(ice_factory)

    print("\n=== Demo Complete ===")