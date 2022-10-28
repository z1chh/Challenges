n, h, l = map(int, input().split())
default_horrors = list(map(int, input().split()))
movie_ratings = {}
for id in default_horrors:
    movie_ratings[id] = 0
to_do = []
for _ in range(l):
    id1, id2 = map(int, input().split())
    if id1 in movie_ratings:
        if id2 in movie_ratings:
            if movie_ratings[id1] < movie_ratings[id2]:
                movie_ratings[id2] = movie_ratings[id1] + 1
            elif movie_ratings[id2] < movie_ratings[id1]:
                movie_ratings[id1] = movie_ratings[id2] + 1
        else:
            movie_ratings[id2] = movie_ratings[id1] + 1
    else:
        if id2 in movie_ratings:
            movie_ratings[id1] = movie_ratings[id2] + 1
        else:
            to_do.append((id1, id2))
inc = 0
while to_do:
    id1, id2 = to_do.pop(0)
    if id1 in movie_ratings:
        if id2 in movie_ratings:
            if movie_ratings[id1] < movie_ratings[id2]:
                movie_ratings[id2] = movie_ratings[id1] + 1
            elif movie_ratings[id2] < movie_ratings[id1]:
                movie_ratings[id1] = movie_ratings[id2] + 1
        else:
            movie_ratings[id2] = movie_ratings[id1] + 1
    else:
        if id2 in movie_ratings:
            movie_ratings[id1] = movie_ratings[id2] + 1
        else:
            if len(to_do == 0):
                inc += 1
                break
            to_do.append((id1, id2))
id = n
lowest = 0
for k, v in movie_ratings.items():
    if v > lowest:
        lowest = v
        id = k
    elif v == lowest:
        if k < id:
            id = k
print(id if inc == 0 else id + 1)
