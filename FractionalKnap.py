class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def FractionalKnapsack(arr, W):
    # Sort items based on profit/weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    
    ans = 0.0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            ans += item.profit 
        else:
            ans += item.profit * (W / item.weight)  # Use float division here
            break
            
    return ans

def main():
    n = int(input("Enter the number of items: "))  # Get the number of items
    arr = []

    for i in range(n):
        profit = float(input(f"Enter profit for item {i + 1}: "))  # Get profit for each item
        weight = float(input(f"Enter weight for item {i + 1}: "))  # Get weight for each item
        arr.append(Item(profit, weight))

    W = float(input("Enter the capacity of the knapsack: "))  # Get the capacity of the knapsack
    max_profit = FractionalKnapsack(arr, W)
    print(f"The maximum profit is: {max_profit}")

main()

# def main():
#     arr = [Item(20, 15), Item(40, 40), Item(50, 70)]
#     print(FractionalKnapsack(arr, 50))
# ans=55
