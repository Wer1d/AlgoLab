# goals : check that Path(u,v) exists or not, if exist return the path
#         check that Hamiltonian cycle and path exists or not, if exist return the cycle    

# Definition : 1. Path = ซ้ำ vertex ได้ แต่ไม่ซ้ำ edge
#              2. Cycle = path ที่ จุดเริ่มต้น = จุดสุดท้าย
#              3. Hamiltonian cycle = cycle ที่ผ่านทุก vertex เพียง 1 ครั้ง
#              4. Hamiltonian path = path ที่ต้องผ่านทุก vertexเพียง 1 ครั้ง
 
# steps : 1. ต้องมีตัวเช็คว่า visite vertex ไปยัง
#         2. เริ่มจาก vertex 0 แล้วเช็คว่า visited อันไหนบ้าง ถ้าไปได้ append to path 

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = [0 for i in range(len(matrix))]
        self.path = []

    def findPathFrom(self, u, v, current_path=[]):  # Pass the current path as an argument
        self.visited[u] = 1
        current_path.append(u)
        if u == v:
            self.path.append(current_path.copy())
        else:
            for available_node, is_connected in enumerate(self.matrix[u]):
                if is_connected and not self.visited[available_node]:
                    # Pass the current_path to the recursive call
                    self.findPathFrom(available_node, v, current_path)

        self.visited[u] = 0
        current_path.pop()

    def findAllPathFrom(self, u, v):
        self.path = []
        self.findPathFrom(u, v)
        self.visited = [0 for i in range(len(self.matrix))]
        return self.path
    
    def findAllPath(self):
        self.path = []
        allPath = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.findPathFrom(i, j)
        allPath.append(self.path.copy())
            
        self.visited = [0 for i in range(len(self.matrix))]
        return allPath
    
    def findHamiltonianPath(self):
        allPath = self.findAllPath()
        hamilPath = []
        
        for path in allPath[0]:
            
            if len(path) == len(self.matrix):
                hamilPath.append(path)
        return hamilPath

    def findHamiltonianCycle(self): 
        allHamiltonianPath = self.findHamiltonianPath()
        hamilCycle = []
        for hamilPath in allHamiltonianPath:
                start =  hamilPath[0] 
                stop = hamilPath[-1]
                if self.matrix[start][stop] == 1:
                    hamilCycle.append(hamilPath)
        return hamilCycle
    
# Read input as an adjacency matrix
with open('input.txt', 'r') as f:
    AdjMatrix = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

myGraph = Graph(AdjMatrix)

print(myGraph.findAllPathFrom(0, 3))
print(myGraph.findAllPath())
print("Hamil Path : \n" , myGraph.findHamiltonianPath())
print("Hamil Cycle : \n " , myGraph.findHamiltonianCycle())
