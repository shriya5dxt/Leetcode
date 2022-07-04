def maxProfit(prices):
    i=0
    len = 0
    for j in range(1,len(prices)-1):
        if prices[j]>prices[i]:
            if prices[j]-prices[i]>0:
                print(i)
                len = prices[j]-prices[i]
            print(i)
            i = i+1
    print(len)



maxProfit([7,6,4,3,1])