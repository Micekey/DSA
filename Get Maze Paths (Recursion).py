def maze_paths(sr,sc,dr,dc):
    if sr > dr or sc > dc:
        return []
    elif sr == dr and sc == dc:
        return [""]
        
    vertical_paths = maze_paths(sr+1,sc,dr,dc)
    horizontal_paths = maze_paths(sr,sc+1,dr,dc)
    all_paths = []
    for path in vertical_paths:
        all_paths.append('v'+path)
    for path in horizontal_paths:
        all_paths.append('h'+path)
    
    return all_paths    

print(maze_paths(1,1,5,5))
