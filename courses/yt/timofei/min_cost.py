def count_min_cost(N, price:list):
    C = [float("-inf"), price[1], price[1]+price[2]] + [0]*(N-2)
    for i in range(3,N+1):
        C[i]= price[i]+min(C[i-1], C[i-2])
    return C[N]

price = [2,1,3,5,6,7,32,2,5,9,8,66]
print(count_min_cost(5,price))