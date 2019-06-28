def search(a, n):
    temp = []
    for i in range(len(a)):
        if a[i] == n:
            temp.append(i)
    return temp

num = [4,5,21,15,5,23,62,24, 15]

print(search(num, 15))
print(search(num, 0))