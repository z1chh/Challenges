floatList = list(map(float, input().split()))
toreturn = abs(floatList[0] - floatList[2])*abs(floatList[1] - floatList[3])
print("{:.3f}".format(toreturn))
