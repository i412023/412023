def hello():
    print("Hello!")

def hello2(name: str):
    print(f"Hello, {name}!")

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    hello()
    hello2("Alice")
    result = add(5, 3)
    print(f"5 + 3 = {result}")