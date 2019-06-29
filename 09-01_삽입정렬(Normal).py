def ins_sort(a):
    for i in range(len(a)):
        for j in range(i):
            if a[i] < a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

d = [2, 4, 5, 1, 3]
print(ins_sort(d))      