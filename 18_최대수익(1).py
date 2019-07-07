# 가장 쌀 때 사서 가장 비쌀 때 파는 것.
def max_profit(prices):
    max_profit = 0

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit

    return max_profit


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))