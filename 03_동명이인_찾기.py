name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]

def find_same_name(name):
    result = []
    #result = set()
    for i in range(len(name)):
        for j in range(i+1, len(name)):
            if name[i]==name[j]:
                result.append(name[i])
                #result.add(name[i])
    return result

print(find_same_name(name))