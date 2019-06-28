def search (a, n):
    for i in range(len(a)):
        if a[i] == n:
            print("The index is ", i)
            return
    print("There is no what I want")
    


num = [4,5,21,15,5,23,62,24]

search(num, 15)
search(num, 62)