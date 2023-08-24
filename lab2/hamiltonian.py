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

    def findPath(self, u, v, current_path=[]):  # Pass the current path as an argument
        self.visited[u] = 1
        current_path.append(u)
        if u == v:
            self.path.append(current_path.copy())
        else:
            for available_node, is_connected in enumerate(self.matrix[u]):
                if is_connected and not self.visited[available_node]:
                    # Pass the current_path to the recursive call
                    self.findPath(available_node, v, current_path)

        self.visited[u] = 0
        current_path.pop()

    def findAllPath(self, u, v):
        self.path = []
        self.findPath(u, v)
        return self.path

# Read input as an adjacency matrix
with open('input.txt', 'r') as f:
    AdjMatrix = [[int(x) for x in line.strip().split(" ")] for line in f.readlines()]

myGraph = Graph(AdjMatrix)

print(myGraph.findAllPath(1, 3))
