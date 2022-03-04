import sys
def bestTime(prices):
    profit=0
    minm=sys.maxsize
    for i in range(len(prices)):

        if prices[i]<minm: 
            minm=prices[i]
        elif (prices[i]-minm) > profit:
            profit= prices[i]-minm
    print(profit)
    return profit



prices = [7,1,5,3,6,4]
bestTime(prices)
prices = [7,6,4,3,1]
bestTime(prices)
