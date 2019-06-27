name = ["Tom", "Jerry", "Mike"]

def make_couple(name):
    for i in range(len(name)-1):
        for j in range(i+1, len(name)):
            print(name[i], "-", name[j])


make_couple(name)