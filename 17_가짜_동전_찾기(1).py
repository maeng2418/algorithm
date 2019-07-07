def weight(a, b, c, d):
    fake = 29 # 가짜 동전의 위치
    if a <= fake and fake <= b: # a~b에 가짜 동전이 있음
        return -1
    if c <= fake and fake <= d: # c~d에 가짜 동전이 있음
        return 1
    # 가짜 동전 없음
    return 0

def find_fakecoin(left, right):
    for i in range(left+1, right+1): # left+1부터 right까지
        result = weight(left, left, i, i) # 하나씩 비교하기
        if result == -1:
            return left
        elif result == 1:
            return i
    return -1

n = 100
print(find_fakecoin(0, n-1))