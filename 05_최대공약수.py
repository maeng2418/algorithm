"""
def gcd(a, b):
    i = min(a, b)
    while True:
        if a%i == 0 and b%i == 0:
            return i
        else:
            i-=1
        
"""

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(3, 6))
print(gcd(4, 5))