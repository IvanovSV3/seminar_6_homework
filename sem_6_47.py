# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)

n = int(input("введите чилсо N "))
res = [i*(-3) for i in range(1, n)]
res[0] = 1
print(res)
# print(n)
# j = -3
# res = [1]
# for i in range(1, n):
#     k = i * j
#     j = j*-1
#     res.append(k)
# print(res)