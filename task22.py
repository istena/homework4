# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12


first_size=int(input("Введите количество элементов в первом наборе: "))
second_size=int(input("Введите количество элементов в втором наборе: "))
list1=[0]*first_size
list2=[0]*second_size
for i in range(first_size):
    list1[i]=int(input(f" 1.{i+1}) "))
for i in range(second_size):
    list2[i]=int(input(f" 2.{i+1}) "))
result=[]
set1=set(list1)
set2=set(list2)
temp=0
for numbers in set1:
    if numbers in set2:
        result.append(numbers)
for i in range(len(result)):
    for j in range(len(result)-1):
        if result[j]>result[i]:
            temp=result[i]
            result[i]=result[j]
            result[j]=temp
print(result)


