def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

        
d = [2, 4, 5, 1, 3]
print(d)
bubble_sort(d)
print(d)