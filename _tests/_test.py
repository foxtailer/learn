def fu(hand):
    match hand:
        case hand if (straight_result := hand)[0] and (flush_result := hand)[0]:
            # Access the second elements in the tuples for whatever you need
            return 'qq', straight_result[1]
        
print(fu((True, 'ww')))
