"""Problem statement: - We have different cites in the state and we have to build road from one city to another and also
we have to build the libraries such that all the citizen in each city can have access of the libraries
Citizen can access the library only if :
1. They can go the city in which library is already present.
2. Their city contains a library.

Numbers of variable we have in this problem
cities- number of cities we have
roads- total number os roads we can make
c_lib- cost to make the library
c_road- cost to make the road. """

n_nodes= 0

# Function to perform dfs
def dfs(source, visited, roadmap):
    global n_nodes
    visited[source] = True
    n_nodes += 1
    for node in roadmap[source]:
        if not visited[node]:
            dfs(node, visited, roadmap)
        else:
            return 0
    return n_nodes

# Solution of the problem
def RoadAndLibrary(roadmap, n, cc_lib, cc_road, ):
    visited = [False for _ in range(cities + 1)]
    nNodes, cost = 0, 0
    for node in range(1, n+1):
        if not visited[node]:
            nNodes = dfs(node, visited, roadmap)
            print('nNodes', nNodes)
        if cc_road > cc_lib:
            cost += (nNodes) * cc_lib
        else:
            cost += (nNodes-1) * cc_road + cc_lib

    return cost


cities = 8
roads = [[1,7], [1,3], [1,2], [2,3], [5,6], [6,8]]
c_lib, c_road = 3, 2

adjlist = [[] for _ in range(cities+1)]

for node1, node2 in roads:
    adjlist[node1].append(node2)
    adjlist[node2].append(node1)

cost = RoadAndLibrary(adjlist, cities, c_lib, c_road, )
print(cost)








