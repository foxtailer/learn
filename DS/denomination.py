def coin_changing(L, amount):
    denomination = []
    i=0
    while(i<len(L)):
      num = int(amount/L[i]) 
      amount = amount - num*L[i]
      denomination.append(num)
      i+=1 
    return denomination
 L=[500, 100, 50, 20, 10, 5, 2, 1]
 print(len(L)) 
 den=coin_changing(L, 657)
 print(den)
