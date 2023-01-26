# 45. Найти сумму чисел списка стоящих на нечетной позиции
list = [i for i in range(0,10)]
print(list)
sum_even = 0
sum_odd = 0

for ind,valu in enumerate(list):
    if ind%2 == 0:
        sum_even += valu
    else:
        sum_odd += valu
print('sum_even ', sum_even)
print('sum_odd ', sum_odd)