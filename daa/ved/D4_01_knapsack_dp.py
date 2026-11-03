def knapsack_dp(values, weights, capacity):
    n = len(values)

    # dp[i][w] = maximum value using first i items with capacity w
    dp = [[0 for w in range(capacity + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include_item = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude_item = dp[i - 1][w]
                dp[i][w] = max(include_item, exclude_item)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

if n <= 0:
    print("Number of items must be positive.")
else:
    values = []
    weights = []

    for i in range(n):
        value = int(input("Enter value of item " + str(i + 1) + ": "))
        weight = int(input("Enter weight of item " + str(i + 1) + ": "))

        if weight < 0:
            print("Weight cannot be negative.")
            break

        values.append(value)
        weights.append(weight)
    else:
        capacity = int(input("Enter knapsack capacity: "))

        if capacity < 0:
            print("Capacity cannot be negative.")
        else:
            answer = knapsack_dp(values, weights, capacity)
            print("Maximum value:", answer)
