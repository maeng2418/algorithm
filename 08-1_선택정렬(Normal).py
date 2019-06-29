def sel_sort(a):
    for i in range(len(a)-1):
        min = a[i]
        for j in range(i+1, len(a)):
            if min > a[j]:
                min = a[j]
                a[j] = a[i]
                a[i] = min
    return a
    
d = [2, 4, 5, 1, 3]

print(d)
print(sel_sort(d))