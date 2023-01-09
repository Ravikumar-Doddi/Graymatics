def knapsack(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n)]
    
    for i in range(n):
        for w in range(max_weight + 1):
            if items[i]['weight'] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], items[i]['value'] + dp[i-1][w-items[i]['weight']])
    
    return dp[n-1][max_weight]
    
result = knapsack([{ "name":"map", "weight":9, "value":150 }, { "name":"compass", "weight":13, "value":35 }, {
"name":"water", "weight":153, "value":200 }, { "name":"sandwich", "weight":50, "value":160 }, { "name":"glucose",
"weight":15, "value":60 }, { "name":"tin", "weight":68, "value": 45 }, { "name":"banana", "weight":27, "value":60 }, {
"name":"apple", "weight":39, "value":40 }],100)
