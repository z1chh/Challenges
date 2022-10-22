tc = int(input())
for _ in range(tc):
    k, n = map(int, input().split())
    list1 = [i for i in range(1, n + 1)]
    list2 = [i * 2 + 1 for i in range(0, n)]
    list3 = [i * 2 for i in range(1, n + 1)]
    print(k, sum(list1), sum(list2), sum(list3))
