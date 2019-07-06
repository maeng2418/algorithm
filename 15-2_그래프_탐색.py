def graph_search(g, start):
    if len(g[start]) == 0:
        return
    
    for i in range(len(g[start])):
        print(start, ' -> ', g[start][i])

    for i in range(len(g[start])):
        graph_search(g, g[start][i])



g = {
    1 : [2, 3],
    2 : [4, 5],
    3 : [],
    4 : [],
    5 : []
}

graph_search(g, 1)