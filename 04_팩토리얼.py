"""
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
"""

def fact(n):
    if n == 1 :
        return 1
    else:
        return n*fact(n-1)

print(fact(4))