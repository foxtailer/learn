itarable_obj = (1,2,3,4,5)

new_iterator = iter(itarable_obj)

while True:
    try:
        print(next(new_iterator))
    except:
        print("Stop iteration")
        break