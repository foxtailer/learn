def fu():
    try:
        return 1  # python rememver 1
    finally:
        return 2  # then overvrite 1 by 2
    
print(fu() )
