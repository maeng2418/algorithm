def merge_sort(a):
    if len(a) <= 1:
        return a
        
    mid = len(a) // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

d = [2, 4, 5, 1, 3]

print(d)
print(merge_sort(d))