def increment(x):
    print(f"Incrementing {x} by 1.")
    return x + 1

def main():
    a = 5
    b = increment(a)
    increment(10)
    print(a)
    print(increment(14))
    print(b)
    print(increment(a))

if __name__ == "__main__":
    main()