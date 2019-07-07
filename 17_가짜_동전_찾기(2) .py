def weight(a, b, c, d):
    fake = 7 # 가짜 동전의 위치
    if a <= fake and fake <= b: # a~b에 가짜 동전이 있음
        return -1
    if c <= fake and fake <= d: # c~d에 가짜 동전이 있음
        return 1
    # 가짜 동전 없음
    return 0

def find_fakecoin(left, right):
    if left == right:
        return left
    
    mid = (left+right) // 2
    
    result = weight(left, mid, mid+1, right)
    
    if result == -1:
        return find_fakecoin(left, mid)
    if result == 1:
        return find_fakecoin(mid+1, right)


n = 100
print(find_fakecoin(0, n-1))