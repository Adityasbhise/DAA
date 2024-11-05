class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def Knapsack01(arr, W, n):
    # Create a 2D array to store the maximum profit at each n and capacity W
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if arr[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - arr[i - 1].weight] + arr[i - 1].profit)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

def main():
    n = int(input("Enter the number of items: "))  # Get the number of items
    arr = []

    for i in range(n):
        profit = int(input(f"Enter profit for item {i + 1}: "))  # Get profit for each item
        weight = int(input(f"Enter weight for item {i + 1}: "))  # Get weight for each item
        arr.append(Item(profit, weight))

    W = int(input("Enter the capacity of the knapsack: "))  # Get the capacity of the knapsack
    max_profit = Knapsack01(arr, W, n)
    print(f"The maximum profit that can be carried in the knapsack is: {max_profit}")

main()
