def tower_builder(n_floors):
    line_width = int(n_floors/2 * (1 + (1 + (n_floors-1)*2)))
    result = []
    floor = "*"
    
    for _ in range(n_floors):
        result.append(floor.center(line_width, " "))
        floor += "*"*2
    return result
print(tower_builder(3))
