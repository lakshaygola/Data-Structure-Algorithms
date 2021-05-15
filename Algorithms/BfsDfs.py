# Class which used to represent the graph (adjacency list representation)
class AdjacencyGraph:
    def __init__(self, n_vertices, edges):
        self.adjlist= [[] for _ in range(n_vertices)]

        for v1, v2 in edges:
            self.adjlist[v1].append(v2)
            self.adjlist[v2].append(v1)

    # Function to represent the graph
    def __repr__(self):
        result= ''
        for node, edeges in enumerate(self.adjlist):
            result += str(node) + ':' + str(edeges) + '\n'
        return result

    def __str__(self):
        return self.__repr__()


# Function to transversal to the graph (BFS)
def BfsTrans(graph, source):
    # Mention the node in which we are currently
    current= source
    # Type of quene which help to store the nodes which are visited
    visited= [False] * len(graph.adjlist)
    # List to store the node which we have to visit next
    quene= [current]
    visited[current]= True
    i = 0
    while i < len(quene):
        current= quene[i]
        for v in graph.adjlist[current]:
            if not visited[v]:
                quene.append(v)
                visited[v]= True
        i += 1
    return quene

# Function to transversal the graph (DFS)

'''1. Create the stack have one element that  is source.
2. Pop the last element for the stack mark it visited then add the neighbour elements into the stack.
3. Repeat the step till stack is empty'''

def DfsTrans(graph, source):
    stack= [source]
    visited= [False] * len(graph.adjlist)
    parent= [None] * len(graph.adjlist)
    parent[source]= -1
    result= []
    while len(stack) > 0:
        current= stack.pop()
        if not visited[current]:
            result.append(current)
        visited[current]= True
        for v in graph.adjlist[current]:
            if not visited[v]:
                stack.append(v)
                parent[v]= current
    return result, parent


# Function to check weather there is a cycle in the graph or not
def isCylcic(graph, source):
    stack = [source]
    visited= [False] * len(graph.adjlist)
    parent= [None] * len(graph.adjlist)
    parent[source]= -1

    while len(stack) > 0:
        current= stack.pop()
        if not visited[current]:
            visited[current]= True

        for node in graph.adjlist[current]:
            if not visited[node]:
                stack.append(node)
                parent[node]= current
            elif visited[node] == True and parent[current] !=  node:
                return 'This Graph contain the cycle'
    return 'This graph doesnt contain the cycle'



# Function to check weather all the nodes are connected or not
def completeGraph(graph, n_vert, edges):
    result= BfsTrans(graph, edges[1][0])

    if len(result) == n_vert:
        return 1
    else:
        return 0


if __name__ == '__main__':

    # Graph1 (undirected, unweighted and contain cycle)
    n_vert1= 5
    edges1= [(0,1), (0,4), (1,4), (1,2), (2,3), (3,1), (4,3)]
    graph1= AdjacencyGraph(n_vert1, edges1)
    print('This the Graph: \n', graph1.adjlist)
    completeGraph(graph1, n_vert1, edges1)
    result1= isCylcic(graph1, 0)
    print(result1)



    # Graph2 (undirected, unweighted and contain cycle)
    n_vert2= 5
    edges2= [(1,0), (1,2), (2,0), (3,0), (3,4)]
    graph2= AdjacencyGraph(n_vert2, edges2)
    print('Graph 2: \n', graph2.adjlist)
    completeGraph(graph2, n_vert2, edges2)
    result2= isCylcic(graph2, 0)
    print(result2)


    # Graph3 (undirected, unweighted and don't contain cycle)
    n_vert3= 6
    edges3= [(0,3), (1,3), (2,3), (3,4), (4,5)]
    graph3= AdjacencyGraph(n_vert3, edges3)
    print('Graph 3: \n', graph3.adjlist)
    completeGraph(graph3, n_vert3, edges3)
    result3= isCylcic(graph3, 0)
    print(result3)



