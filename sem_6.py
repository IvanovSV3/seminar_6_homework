# a = [12, 34, 567, 671]
# a_1 = sorted(a, reverse = True)
# print(a_1)



# a = [12, 34, 567, 671]
# def sort(x):
#     if x%2 == 0:
#         return True
#     return False

# a_1 = sorted(a, key=sort)
# print(a_1) #[567, 671, 12, 34]

# a = [12, 34, 567, 671]
# def sort(x):
#     if x%2 == 0:
#         return False
#     return True

# a_1 = sorted(a, key=sort)
# print(a_1) #[12, 34, 567, 671]

# a = ["adevx", "lkjwi", "sw", "lwih"]
# a_1 = sorted(a, key = len)
# print(a_1) #['sw', 'lwih', 'adevx', 'lkjwi']

# a = ["adevx", "lkjwi", "sw", "lwih"]
# a_1 = sorted(a, key = lambda x:x[0])
# print(a_1) # ['adevx', 'lkjwi', 'lwih', 'sw']

# a = {4:"2fss", 2:"ljsf", 5:"wewru"}
# a_1 = sorted(a)
# print(a_1) # [2, 4, 5]

# a = [(2,4,7), (9,2,6), (24,65,3)]
# a_1 = sorted(a, key = lambda x:x[2])
# print(a_1) # [(24, 65, 3), (9, 2, 6), (2, 4, 7)]

# 41) Напишите программу, которая сортирует элементы массива по возрастанию последней 
# цифры десятичной записи чисел.
# Входные данные

# a = "219 234 890 81 73 96"

# a_1 = list(map(int,a.split()))
# a_resalt = sorted(a_1, key= lambda x: x%10)
# print(a_resalt) # [890, 81, 73, 234, 96, 219]

# Сортирует по сумме чисел элементов.

# a = "219 234 890 81 73 96"
# a = list(map(int, a.split()))
# def summ(x):
#     temp = 0
#     while x != 0:
#         temp = temp + x%10
#         x = x//10
#     return temp
# a_resalt = sorted(a, key= summ, reverse=True)
# print(a_resalt) # [890, 96, 219, 73, 234, 81]

a = [3, 1, 2,5,4,6]
h = [1 if i%2==0 else 0 for i in a]
print(h)
print(a)
het = [i for i in a if i%2==0]
print(het)
non_het = [i for i in a if i%2==1]
print(non_het)

het.sort(reverse=True)
non_het.sort()
print(non_het)
print(het)

for ind,valu in enumerate(h):
    if valu == 1:
        h[ind] = het.pop(0)
    else:
        h[ind] = non_het.pop(0)

print(h)

