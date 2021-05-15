import DWgraph as dw

# Function to update the weights of all the node from the current node
def update_weights(graph, distance, current):
    neighbours= graph.data[current]
    weights= graph.weights[current]

    for i, node in enumerate(neighbours):
        weight= weights[i]
        if distance[current] + weight < distance[node]:
            distance[node]= distance[current] + weight


# Function to select the next node from the current node
def selectNextNode(visited, distance):
    min_distance= float('inf')
    select_node= None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            select_node= node
            min_distance= distance[node]
    return select_node


# Function to find the shortest path
def shortestPath(graph, soruce, target):
    visited= [False] * len(graph.data)
    distance= [float('inf')] * len(graph.data)
    distance[soruce]= 0
    quene= [soruce]
    idx= 0
    while idx < len(quene) and not visited[target]:
        current= quene[idx]
        visited[current] = True
        idx += 1
        update_weights(graph, distance, current)
        next_node= selectNextNode(visited, distance)
        if next_node:
            quene.append(next_node)

    return distance[target]


# graph1 (Driected and weighted)
n_vert1= 6
edges1= [(0,1,4), (0,2,2), (1,2,5), (1,3,10), (2,4,3), (3,5,11), (4,3,4)]
graph1= dw.WDgraph(n_vert1, edges1, True)
print('Graph 1 :\n', graph1)
distance= shortestPath(graph1, 0, 5)
print('Shortest distance between the starting node and the target node is: ', distance)


# Graph2 (Undriected and weighted)
n_vert2= 9
edges2= [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
graph2= dw.WDgraph(n_vert2, edges2)
print('Graph2 : \n', graph1)
print('Shortest distance between the starting node and the target node is: ', shortestPath(graph2, 2, 8))