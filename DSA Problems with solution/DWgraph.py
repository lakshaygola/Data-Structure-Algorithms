# Class used to store the weighted and directed graph
class WDgraph:
    def __init__(self, n_vertices, edges, directed= False):
        self.vertices= n_vertices
        self.edges= edges
        # Making the list to store the tree (using adjancey list method)
        self.data= [[] for _ in range(self.vertices)]
        # Making the list of the weights of the edges
        self.weights= [[] for _ in range(self.vertices)]
        for e in edges:
            # If lenght of the edge is 3 that means it a weighted data
            if len(e) == 3:
                v1, v2, w= e
                self.data[v1].append(v2)
                self.weights[v1].append(w)
                if not directed:
                    self.data[v2].append(v1)
                    self.weights[v2].append(w)
            else:
                v1, v2= e
                self.data[v1].append(v2)
                if not directed:
                    self.data[v2].append(v1)

    # Function to represent the graph
    def __repr__(self):
        result= ''
        if len(self.edges[0]) == 3:
            for idx, (node, weights) in enumerate(zip(self.data, self.weights)):
                result += '{}: {}\n'.format(idx, list(zip(node, weights)))
        else:
             for idx, node in enumerate(self.data):
                 result += '{}: {}\n'.format(idx, node)
        return result

if __name__ == '__main__':

    # Directed Graph (graph1)
    vert1 = 5
    edges1 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
    graph1= WDgraph(vert1, edges1, True)
    print('Graph1: \n', graph1)


    # Weighted graph (graph2)
    # Graph with weights
    vert2 = 9
    edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
              (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]
    graph2= WDgraph(vert2, edges2)
    print('Graph2: ', graph2)



