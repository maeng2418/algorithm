def find_name(n):
    d = {39 : "Justin", 14 : "John", 67 : "Mike", 105 : "Summer"}

    for num in d:
        if num == n:
            return d[num]
    return "?"

print(find_name(67))
print(find_name(100))