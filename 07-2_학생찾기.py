def find_stud (list, num):
    for i in range(len(list[0])):
        if str(num) == list[0][i]:
            return list[1][i]



code = [["39", "14", "67", "105"],
["Justin", "John", "Mike", "Summer"]]

print(find_stud(code, 39))
print(find_stud(code, 14))