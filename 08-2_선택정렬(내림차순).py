def sel_sort(a):
    for i in range(len(a)-1):
        max = a[i]
        for j in range(i+1, len(a)):
            if max < a[j]:
                max = a[j]
                a[j] = a[i]
                a[i] = max
    return a

d = [2, 4, 5, 1, 3]

print(d)
print(sel_sort(d))