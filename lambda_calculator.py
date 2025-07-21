def add(a, b):
    return (lambda x, y: x + y)(a, b)

def subtract(a, b):
    return (lambda x, y: x - y)(a, b)

def multiply(a, b):
    return (lambda x, y: x * y)(a, b)

def divide(a, b):
    return (lambda x, y: x / y if y != 0 else "Error: Not Divisable by zero")(a, b)

if __name__ == "__main__":
    x = 10
    y = 5

    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y)) 