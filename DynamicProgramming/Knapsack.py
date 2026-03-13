"""
Problem: Knapsack Problem
Given a list of weights and values of items, and a maximum capacity, determine the maximum value
that can be obtained by selecting a subset of the items such that the total weight does not exceed the capacity.
Result is in the README
"""

def knapsack(weights, values, capacity):
    n = len(weights)    
    # Creating a dp table, 
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        w = weights[i - 1] # weight of the current item and value
        v = values[i - 1]
        for cap in range(1, capacity + 1):

            if w <= cap:
                dp[i][cap] = max(dp[i - 1][cap], v + dp[i - 1][cap - w])
            else:
                dp[i][cap] = dp[i - 1][cap]
    # The value in the bottom right cell of the dp table will be the maximum value that can be obtained with the given capacity
    return dp[n][capacity]
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Weights:", weights)
print("Values: ", values)
print("Capacity:", capacity)
print("Maximum value:", knapsack(weights, values, capacity))