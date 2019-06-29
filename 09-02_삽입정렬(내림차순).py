def ins_sort(a):
    for i in range(1, len(a)):
        for j in range(i):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    return a

d = [2, 4, 5, 1, 3]
print(ins_sort(d))      