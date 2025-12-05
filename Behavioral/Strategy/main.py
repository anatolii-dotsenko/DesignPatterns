from abc import ABC, abstractmethod

# --------------------------------------------------------------------------
# 1. The Strategy Interface
# --------------------------------------------------------------------------
class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported
    versions of some algorithm.
    """
    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass

# --------------------------------------------------------------------------
# 2. Concrete Strategies
# --------------------------------------------------------------------------
class ConcreteStrategyAdd(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b

class ConcreteStrategySubtract(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

class ConcreteStrategyMultiply(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a * b

# --------------------------------------------------------------------------
# 3. The Context
# --------------------------------------------------------------------------
class Context:
    """
    The Context maintains a reference to one of the Strategy objects.
    It interacts with the strategy via the interface only.
    """
    def __init__(self, strategy: Strategy = None): # type: ignore
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing the Strategy object at runtime.
        (Matches setStrategy in your pseudocode)
        """
        self._strategy = strategy

    def execute_strategy(self, a: int, b: int) -> int:
        """
        The Context delegates work to the Strategy object.
        """
        if self._strategy:
            return self._strategy.execute(a, b)
        else:
            print("Error: No strategy set.")
            return 0

# --------------------------------------------------------------------------
# 4. Client Code
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # Create context object
    context = Context()

    try:
        # Read inputs
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        action = input("Enter action (addition, subtraction, multiplication): ").strip().lower()

        # Select concrete strategy based on user input
        if action == "addition":
            context.strategy = ConcreteStrategyAdd()
        elif action == "subtraction":
            context.strategy = ConcreteStrategySubtract()
        elif action == "multiplication":
            context.strategy = ConcreteStrategyMultiply()
        else:
            print("Invalid action selected.")
            exit()

        # Execute
        result = context.execute_strategy(num1, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid integers.")