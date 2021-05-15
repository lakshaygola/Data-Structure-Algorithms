# This file contain the code and the basic concept of the graph

# Class which used to represent the graph (adjacency list representation)
class adjacency_graph:
    def __init__(self, n_vertices, edges):
        self.data= [[] for _ in range(n_vertices)]

        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)

    # Function to represent the graph
    def __repr__(self):
        result= ''
        for node, edeges in enumerate(self.data):
            result += str(node) + ':' + str(edeges) + '\n'
        return result

    def __str__(self):
        return self.__repr__()


# Function to add the edge into the graph
def addEdge(graph, v1, v2):
    graph.matrix[v2][v1]= 1
    graph.matrix[v1][v2]= 1

    return graph


# Function to remove the edge from the graph
def removeEdge(graph, v1, v2):
    graph.matrix[v1][v2]= 0
    graph.matrix[v2][v1]= 0

    return graph

# Class to represent the graph (Matrix representation)
class matrix_graph:
    def __init__(self, n_vertices, edges):
        self.vertices= n_vertices
        self.matrix= [[0 for _ in range(n_vertices)] for _ in range(n_vertices)]

        for i in range(n_vertices):
            for j in range(n_vertices):
                for v1, v2 in edges:
                    if i == v1 and j == v2:
                        self.matrix[i][j]= 1
                    elif j == v1 and i == v2:
                        self.matrix[i][j]= 1


# Function to print the matrix of the graph representation
def matrixRep(graph, vertices):
    for v1 in range(vertices):
        for v2 in range(vertices):
            print(graph.matrix[v1][v2],' ', end='')
        print('')



# Main
n_vert= 5
edges= [(0,1), (0,4), (1,4), (1,2), (2,3), (3,1), (4,3)]

graph1= matrix_graph(n_vert, edges)
print('Before adding the edge: ')
matrixRep(graph1, n_vert)

graph1= addEdge(graph1, 2, 4)
print('After adding the edge: ')
matrixRep(graph1, n_vert)

graph1= removeEdge(graph1, 2, 4)
print('After remove the edge from the graph: ')
matrixRep(graph1, n_vert )