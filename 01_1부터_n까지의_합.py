def sum_n(n):
    s = 0
    for i in range(1,n+1):
        s+=i
    return s

def sum(n):
    return n*(n+1)//2 #슬래시 두개는 정수 나눗셈

print(sum_n(10))
print(sum(10))