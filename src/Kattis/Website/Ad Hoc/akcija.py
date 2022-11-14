books = [int(input()) for _ in range(int(input()))]
books.sort(reverse=True)
price = 0
counter = 1
for book in books:
    if counter < 3:
        price += book
    else:
        counter = 0
    counter += 1
print(price)
