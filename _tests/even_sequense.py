top1 = 16
top2 = -16

def even_seq(top:int) -> list:
    if top < 0:
        _step = -2
    else: 
        _step = 2
        
    return list(range(0,top,_step))

print(even_seq(top1))
print(even_seq(top2))