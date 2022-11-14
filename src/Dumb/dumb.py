def main(x):
    if x < 5:
        return False
    elif x == 5:
        return 100
    else:
        return "Hello World"


if __name__ == "__main__":
    for i in range(4, 7):
        print(main(i))
