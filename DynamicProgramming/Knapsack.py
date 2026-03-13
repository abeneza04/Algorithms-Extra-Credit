def knapsack(weights, values, capacity):
    n = len(weights)
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        
        for cap in range(1, capacity + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i - 1][cap], v + dp[i - 1][cap - w])
            else:
                dp[i][cap] = dp[i - 1][cap]
    
    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print(knapsack(weights, values, capacity))