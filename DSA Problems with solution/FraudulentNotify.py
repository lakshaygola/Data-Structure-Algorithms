"""Problem statement: - We have to find the number of notification bank will send the client. Bank will sent the
            notification only if the client spent >=  2 x median of the spending data of pervious d days
            expenditure[] - which store the values of the daily spend of the client
            d - Numbers of days bank collect the data of the client"""

# Function to solve the problem
def Notify(expend, d):



# Test case 1
expenditure1 = [10, 20, 30, 40, 50]
d1 = 6
print(Notify(expenditure1, d1))

# Test case 2
expenditure2 = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d2 = 5
print(Notify(expenditure2, d2))

# Test case 3
expenditure3 = [1, 1, 1, 1, 1, 1, 1, 1]
d3 = 3
print(Notify(expenditure3, d3))

# Test case 4
expenditure4 = [8, 5, 4, 6, 2, 7, 8, 9]
d4 = 8
print(Notify(expenditure3, d4))