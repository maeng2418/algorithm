def find_min_idx(a):
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a: # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]

print(sel_sort(d))
