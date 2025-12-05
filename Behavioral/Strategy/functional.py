# Functional Approach (More Pythonic for simple logic)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

class Context:
    def __init__(self, strategy_func):
        self.strategy = strategy_func

    def execute(self, a, b):
        return self.strategy(a, b)

# Client use
context = Context(multiply) 
print(context.execute(5, 5)) # Output: 25

context.strategy = add
print(context.execute(5, 5)) # Output: 10