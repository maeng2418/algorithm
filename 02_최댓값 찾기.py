def max_val(a):
    m = 0
    for i in range(len(a)):
        if m < a[i]:
            m = a[i]
    return m

def max_index(a):
    max_idx = 0
    for i in range(len(a)):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx

a = [5, 7, 9, 10, 2, 12, 20, 0]

print(max_val(a))
print(max_index(a))