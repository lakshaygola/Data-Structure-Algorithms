"""Problem statement: - we have a bag of capacity 'c' and we have different objects and each object have certain weight
                        and profit attached with them. We have to fill the bag with the objects such that capacity of b-
                        ag do not get exceed and also profit should be maximize."""


# Function to perform 0/1 knapsack problem using recursion
def recursive_knapsack(capacity, weights, profit, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] <= capacity:
        # Case in which we are including our object in the bag
        option1= profit[idx] + recursive_knapsack(capacity-weights[idx], weights, profit, idx+1)

        # Case in which we are not adding the objects in the bag
        option2= recursive_knapsack(capacity, weights, profit, idx+1)
        return max(option1, option2)
    else:
        return recursive_knapsack(capacity, weights, profit, idx+1)


# Function to perform 0/1 knapsack problem using memoization
def memo_knapsack(capacity, weights, profit):
    memo= {}

    def knapsack(capacity, idx=0):
        if idx == len(weights):
            return 0
        key= (capacity, weights[idx])
        if key in memo:
            return memo[key]
        if weights[idx] <= capacity:
            option1= profit[idx] + knapsack(capacity-weights[idx], idx+1)
            option2= knapsack(capacity, idx+1)
            memo[key] = max(option1, option2)
        else:
            memo[key]= knapsack(capacity, idx+1)

        return memo[key]
    return knapsack(capacity, 0)


# Function to apply the same but in more effective manner using dynamic programming
def dynamic_knapsack(capacity, weights, profit):
    result= [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]

    for idx in range(len(weights)):
        for c in range(capacity+1):
            if weights[idx] <= c:
                option1= profit[idx]+ result[idx][c-weights[idx]]
                option2= result[idx][c]
                result[idx+1][c]= max(option1, option2)
            else:
                result[idx+1][c]= result[idx][c]

    return result[-1][-1]

capacity= 15
weights= [4, 5, 1, 3, 2, 5]
profits= [2, 3, 1, 5, 4, 7]

print('Total profit you get for these set of objects(using memo): ', memo_knapsack(capacity, weights, profits))
print('Total profit you get for these set of objects(using recursive): ', recursive_knapsack(capacity, weights, profits, 0))
print('Total profit you get for these set of objects(using dynamic): ', dynamic_knapsack(capacity, weights, profits))










