def max(a, n):
    if n == 1:
        return a[0]
    else:
        max_val = max(a, n-1)
    
    if max_val > a[n-1]:
        return max_val
    else:
        return a[n-1]

num = [1,2,3,4,4,20,12,24,5,5]

print(max(num, len(num)))