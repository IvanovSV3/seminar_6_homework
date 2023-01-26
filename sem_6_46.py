# 46. Найти произведение пар чисел списка
# (парой считаем первый и последний, второй предпоследний и тд
import random
a = [random.randint(1,10) for j in range(8)]
itog_2 = [a[i] * a[len(a) - i -1] for i in range(round(len(a)/2))]
print(a)
print(itog_2)

# itog = [] #===============
# for i in range(round(len(a)/2)): #===============
#     # print(i)
#     # k = len(a) - i -1
#     # print(k)
#     if (len(a) - i -1) >= i: #===============
#         # k_1 = a[i] * a[k]
#         itog.append(a[i] * a[len(a) - i -1])           #===============
# print(itog)  #===============
