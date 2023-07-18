available_jump_lengths = [1,5,2,3,4]
def get_paths(n):
    if n == 0:
        return [""]
    if n < 0:
        return ""
        
    total_paths = []
    for jump in available_jump_lengths:
        for path in get_paths(n-jump):
            total_paths.append(str(jump)+path)
    
    return total_paths    

print(get_paths(10))
