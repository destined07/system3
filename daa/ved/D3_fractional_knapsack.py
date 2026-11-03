n = int(input("Enter number of items: "))
items = []

if n <= 0:
    print("Number of items must be positive.")
else:
    for i in range(n):
        weight = float(input("Enter weight of item " + str(i + 1) + ": "))
        value = float(input("Enter value of item " + str(i + 1) + ": "))

        if weight <= 0:
            print("Weight must be greater than zero.")
            break

        ratio = value / weight
        items.append([weight, value, ratio])
    else:
        capacity = float(input("Enter knapsack capacity: "))

        if capacity < 0:
            print("Capacity cannot be negative.")
        else:
            # Sort items by value/weight ratio in descending order.
            items.sort(key=lambda item: item[2], reverse=True)

            total_value = 0.0
            remaining_capacity = capacity

            for weight, value, ratio in items:
                if remaining_capacity == 0:
                    break

                if weight <= remaining_capacity:
                    total_value += value
                    remaining_capacity -= weight
                else:
                    fraction = remaining_capacity / weight
                    total_value += value * fraction
                    remaining_capacity = 0

            print("Maximum value:", round(total_value, 2))
