class Graph:
    class Vertex:
        def __init__(self, name): # set property for vertex
            self.name = name
            self.neighbors = []
            self.color = "white"
            self.pi = None
            self.d = 0
            self.f = 0

    def __init__(self,v,e):  # set property for graph
        self.vertices = []  # Store vertices in a list
        self.v = v
        self.e = e
        self.adj = [[0 for _ in range(self.v)] for _ in range(self.v)]  # Adjacency matrix

    def addVertex(self, name):
        self.vertices.append(self.Vertex(name))

    def addEdge(self, u, v, c):
        # construct adj matrix
        if c == 2: # bidirectional
            self.adj[u - 1][v - 1] = 1
            self.adj[v - 1][u - 1] = 1
            # add neighbors : u can travel to v and v can travel to u
            self.vertices[u - 1].neighbors.append(self.vertices[v - 1])
            self.vertices[v - 1].neighbors.append(self.vertices[u - 1])
        elif c == 1:
            self.adj[u - 1][v - 1] = 1
            self.vertices[u - 1].neighbors.append(self.vertices[v - 1])

    def find_scc(self):
        # reset color for all vertex เพราะ dfs ครั้งแรกทำงานไปแล้ว
        for vertex in self.vertices:
            vertex.color = "white"
        time = 0
        scc_list = []
        # DFS again but this time sort by finishing time 
        for vertex in self.vertices:
            if vertex.color == "white":
                print('vertex:', vertex.name, 'pass')
                scc = []
                self.dfs_visit(vertex, time, scc)
                scc_list.append(scc)
                # reset color for all vertex เพราะ dfs ครั้งที่สองทำงานไปแล้ว กับทุก vertex
                # ถ้าไม่รีค่า color กลับมาเป็น white จะทำให้เข้า if vertex.color == "white": ไม่ได้
                for vertex in self.vertices:
                    vertex.color = "white"
        return scc_list    
    
    # from textbook
    def dfs_visit(self, vertex, time, scc):
        time += 1
        vertex.d = time
        vertex.color = "gray"
        scc.append(vertex.name)
        print("scc append:", vertex.name, "neighbors:", [neighbor.name for neighbor in vertex.neighbors])
        
        for neighbor in vertex.neighbors:
            if neighbor.color == "white":
                neighbor.pi = vertex
                self.dfs_visit(neighbor, time, scc)
        vertex.color = "black"
        time += 1
        vertex.f = time

    # from textbook
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

    
current_graph = None  
testName = "./lab6/6-1.txt"
with open(testName, "r") as f:
    for line in f:
        line = line.strip('\n')
        values = line.split()

        if len(values) == 2:  # New graph definition
            if current_graph: # Print previous graph
                print("")
                print(current_graph.adj)
                print("Graph:")
                current_graph.printGraph()
                current_graph.dfs() # Run DFS
                for vertex in current_graph.vertices:
                    print("vertex : " ,vertex.name, "start time : " ,vertex.d, "end : ",vertex.f)
                current_graph.vertices.sort(key=lambda vertex: vertex.f, reverse=True) # Sort vertices by finishing time in reverse order
                
                scc_list = current_graph.find_scc() # Find SCCs (DFS is inside this function)
                
                # Print vertices in SCCs based on their f values
                vertex_to_scc = {}

                # Iterate through the vertices and SCCs
                for vertex, scc in zip(current_graph.vertices, scc_list):
                    vertex_to_scc[vertex.name] = scc

                # Print SCC for each vertex
                for vertex, scc in vertex_to_scc.items():
                    print(f"Vertex {vertex} has SCC: {scc}")
                
                # Sort the SCCs for checking in next step
                sorted_scc_list = [sorted(scc) for scc in scc_list]

                # check that ans is 1 or 0 
                all_equal = all(scc == sorted_scc_list[0] for scc in sorted_scc_list)
                print("output = 1" if all_equal else "output = 0")

                # reset the current graph
                current_graph = None

            v, e = map(int, values)
            current_graph = Graph(v,e) # Create a new graph
            for i in range(v):
                current_graph.addVertex(i + 1) # Add vertices to the graph
            current_graph.v = v
            current_graph.e = e
            current_graph.resetAdjacencyMatrix() # Reset the adjacency matrix to ensure

        elif len(values) == 3:  # read edges
            u, w, c = map(int, values)
            current_graph.addEdge(u, w, c) # Add edges to the graph
