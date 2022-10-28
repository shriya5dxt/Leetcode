def max_profit(prices):
    temp = []
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):

            