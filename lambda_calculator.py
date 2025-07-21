add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Not Divisable by zero"

if __name__ == "__main__":
    x = 10
    y = 5

    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))