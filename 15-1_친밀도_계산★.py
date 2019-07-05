def print_all_friends(g, start):
    qu = []
    done = set()
    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, c) = qu.pop(0)
        print(p, c)
        for x in g[p]:
            if x not in done:
                done.add(x)
                qu.append((x, c+1))



fr_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}
            
print_all_friends(fr_info, 'Summer')