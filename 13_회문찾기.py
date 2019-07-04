# 회문이란? 순서대로 읽어도 거꾸로 읽어도 그 내용이 같은 낱말이나 문장
# Hint : Queue == Stack

# 큐 : FIFO (First In First Out) enqueue/dequeue    ex) qu.pop(0)
# 스택 : LIFO (Last In First Out) push/pop pop()    ex) st.pop()

def palindrome(s):
    qu = []
    st = []

    for w in s:
        if w.isalpha():
            qu.append(w.lower())
            st.append(w.lower())

    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True


print(palindrome("Wow"))
print(palindrome("Tomato"))



