#def task_1_numbers(a, b):
#     if a == b:
#         print(a)
#     elif a < b:
#         print(a)
#         task_1_numbers(a + 1, b)
#     else:
#         print(a)
#         task_1_numbers(a - 1, b)
# a = int(input())
# b = int(input())
# task_1_numbers(a, b)

#def numbers_list(n):
#    if n == 1:
#        return [1]
#   else:
#        return numbers_list(n - 1) + [n]
#
#n = int(input("Введите число n: "))
#numbers = numbers_list(n)
#print("Список чисел от 1 до", n, ":", numbers)

#def two(n):
#    if n == 1:
#        return True
#    if n < 1 or n % 2 != 0:
#        return False
#    return two(n // 2)
#n = int(input())
#if two(n):
#    print("YES")
#else:
#    print("NO")