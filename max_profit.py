# General law: must buy first before selling
# To calculate the maximum profit that can happen in a array of daily stocks
def max_profit(price):
    l, r = 0, 1  # left = buy, right=sell
    maxP = 0

    while r < len(price):
        # is it profitable?
        if price[l] < price[r]:
            profit = price[r] - price[l]
            maxP = max(maxP, profit)
        else:
            l = r  # in the case that it is profitable
        r += 1  # we update the right pointer regardless
    return maxP


# to calculate the sum of profits that can gotten from an array of daily stock prices
def max_profit2(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit


# to calculate the maximum loss that can happen from a daily stock
def max_loss(prices):
    l, r = 0, 1
    maxL = 0

    while r < len(prices):
        if prices[l] > prices[r]:
            loss = prices[l] - prices[r]
            maxL = max(maxL, loss)
        else:
            l = r
        r += 1
    return maxL


# to calculate the total amount of loss that can happen
def max_loss2(prices):
    loss = 0

    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            loss += (prices[i] - prices[i - 1])
    return loss
