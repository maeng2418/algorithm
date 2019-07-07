# 가장 쌀 때 사서 가장 비쌀 때 파는 것.
def max_profit(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]

    return max_profit
    

    return max_profit-min_profit


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))