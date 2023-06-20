A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if A > B:
    print("A должно быть меньше B")
else:
    print("Четные числа на отрезке:", *[i for i in range(A, B) if i % 2 == 0])
       
