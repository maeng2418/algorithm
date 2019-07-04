# 큐와 스택없이 만들기

def palindrome(s):
    i = 0
    j = len(s)-1

    while i < len(s):
        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True


print(palindrome("Wow"))
print(palindrome("Tomato"))
print(palindrome("maam"))
