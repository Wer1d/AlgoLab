class Graph:
    class Vertex:
        def __init__(self, name):
            self.name = name
            self.neighbors = []
            self.color = "white"
            self.pi = None
            self.d = 0
            self.f = 0

    def __init__(self):
        self.vertices = []  # Store vertices in a list
        self.adj = []  # Adjacency matrix
        self.v = 0
        self.e = 0

    def addVertex(self, name):
        self.vertices.append(self.Vertex(name))
        self.v += 1

    def addEdge(self, u, v, c):
        # construct adj matrix
        if c == 2:
            self.adj[u - 1][v - 1] = 1
            self.adj[v - 1][u - 1] = 1
        elif c == 1:
            self.adj[u - 1][v - 1] = 1
        # construct adj list
        self.vertices[u - 1].neighbors.append(self.vertices[v - 1])

    def dfs_visit(self, vertex, time, scc):
        time += 1
        vertex.d = time
        vertex.color = "gray"
        scc.append(vertex.name)
        for neighbor in vertex.neighbors:
            if neighbor.color == "white":
                neighbor.pi = vertex
                self.dfs_visit(neighbor, time, scc)
        vertex.color = "black"
        time += 1
        vertex.f = time
    def dfs(self):
        for vertex in self.vertices:
            vertex.color = "white"
            vertex.pi = None
        time = 0
        for vertex in self.vertices:
            if vertex.color == "white":
                self.dfs_visit(vertex, time, [])

    def resetAdjacencyMatrix(self):
        self.adj = [[0 for _ in range(self.v)] for _ in range(self.v)]

    def printGraph(self):
        for row in self.adj:
            print(" ".join(map(str, row)))
    
    def find_scc(self):
        def dfs_first_pass(vertex):
            nonlocal time
            vertex.color = "gray"
            for neighbor in vertex.neighbors:
                if neighbor.color == "white":
                    dfs_first_pass(neighbor)
            time += 1
            vertex.f = time

        def dfs_second_pass(vertex, scc):
            vertex.color = "gray"
            scc.append(vertex.name)
            for neighbor in vertex.neighbors:
                if neighbor.color == "white":
                    dfs_second_pass(neighbor, scc)

        
        for vertex in self.vertices:
            vertex.color = "white"
        # First pass to compute finishing times
        time = 0
        for vertex in self.vertices:
            if vertex.color == "white":
                dfs_first_pass(vertex)
        for vertex in self.vertices:
            vertex.color = "white"
        # Sort vertices by finishing time in reverse order
        self.vertices.sort(key=lambda vertex: vertex.f, reverse=True)

        # Second pass to find SCCs
        scc_list = []
        for vertex in self.vertices:
            if vertex.color == "white":
                scc = []
                dfs_second_pass(vertex, scc)
                scc_list.append(scc)
        
        return scc_list

current_graph = None  
testName = "./lab6/6-1.txt"

with open(testName, "r") as f:
    for line in f:
        line = line.strip('\n')
        values = line.split()

        if len(values) == 2:  # New graph definition
            if current_graph:
                print("Graph:")
                current_graph.printGraph()
               
                scc_list = current_graph.find_scc()
                print(scc_list)
                
                current_graph = None

            v, e = map(int, values)
            current_graph = Graph()
            for i in range(v):
                current_graph.addVertex(i + 1)
            current_graph.v = v
            current_graph.e = e
            current_graph.resetAdjacencyMatrix()

        elif len(values) == 3:  # Add an edge
            u, w, c = map(int, values)
            current_graph.addEdge(u, w, c)