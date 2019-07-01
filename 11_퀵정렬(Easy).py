def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[-1] # 편의상 마지막 값을 기준값으로 설정
    left = []
    right = []

    for i in range(len(a)-1):
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])

    return quick_sort(left) + [pivot] + quick_sort(right) # [1, 2] + [3] + [4, 5] = [1, 2, 3, 4, 5]
    

d = [2, 4, 5, 1, 3]

print(d)

print(quick_sort(d))