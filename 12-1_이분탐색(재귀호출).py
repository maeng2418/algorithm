def binary_search(a, x, start, end):

    # 리스트 내에 없으면
    if start > end:
        return -1
    
    mid = (start+end)//2
    if a[mid] == x:
        return mid
    elif x > a[mid]:
        return binary_search(a, x, mid+1, end)
    else:
        return binary_search(a, x, start, mid-1) 

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(d, 25, 0, len(d)-1))
print(binary_search(d, 10, 0, len(d)-1))