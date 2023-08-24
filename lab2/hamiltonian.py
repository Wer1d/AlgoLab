# goals : check that Path(u,v) exists or not, if exist return the path
#         check that Hamiltonian cycle and path exists or not, if exist return the cycle    

# Definition : 1. Path = ซ้ำ vertex ได้ แต่ไม่ซ้ำ edge
#              2. Cycle = path ที่ จุดเริ่มต้น = จุดสุดท้าย
#              3. Hamiltonian cycle = cycle ที่ผ่านทุก vertex เพียง 1 ครั้ง
#              4. Hamiltonian path = path ที่ต้องผ่านทุก vertexเพียง 1 ครั้ง
 
# steps : 1. ต้องมีตัวเช็คว่า visite vertex ไปยัง
#         2. เริ่มจาก vertex 0 แล้วเช็คว่า visited อันไหนบ้าง ถ้าไปได้ append to path

class Graph:

    # constructor like Java
    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = [0 for i in range(len(matrix))] # 0 = not visited, 1 = visited
        self.path = []

    # find single path(u,v) แบบ DFS --> เก็บ path แบบวิ่งลงเรื่อยๆ เลยต้อง implement stack 
    def findPathFrom(self, u, v, current_path=[]):  
        self.visited[u] = 1 # set visited at index = u(start index) to 1 (visited)
        current_path.append(u) # add u vertex u to current_path
        if u == v:
            self.path.append(current_path.copy()) 
            # use .copy() ทำให้ไปเก็บที่ memory ใหม่ ทำให้ค่า immutable แก้ไขไม่ได้ ถ้าไม่ใช้ .copy() จะเป็นการเก็บที่ memory เดิม ทำให้เป็น mutable แก้ไขได้
        else:
            for available_node, is_connected in enumerate(self.matrix[u]): # index,value = enumerate()
                if is_connected > 0 and not self.visited[available_node]: # ถ้า is_connected = 1(value from matrix) และ vertex นั้นยังไม่เคยถูกเดิน
                    self.findPathFrom(available_node, v, current_path) 
                    # ให้เดินไปยัง vertex ถัดไป start vertex รอบนี้เป็น available_node และมี current_path เป็น knowledge ส่งไป
                    # recursive call เหมือนเดินไปเรื่อยๆ จนกว่าจะเจอ available_node = v จะ append current_path ทุกอันที่เจอเข้าไปใน path
        self.visited[u] = 0 # set back visited at index = u(start index) to 0 (not visited) ทำให้เริ่มต้น path ใหม่ได้
        # print("current_path before pop: ", current_path)
        current_path.pop() # backtracking

    # find all path from u to v
    def findAllPathFrom(self, u, v):
        self.path = []
        self.findPathFrom(u, v)
        self.visited = [0 for i in range(len(self.matrix))]
        return self.path
    
    # find all path via brute force -> หา path(0,0) path(0,1),...,path(n,n)
    def findAllPath(self):
        self.path = []
        allPath = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.findPathFrom(i, j)
        allPath.append(self.path.copy())
            
        self.visited = [0 for i in range(len(self.matrix))] # set visited to 0 again ทำให้เรียกใช้ method หลายครั้งหรือใช้อันอื่นได้
        return allPath
    
    # เลือกจาก all path เอาตัวที่ มีจำนวน vertex เท่ากับจำนวน vertex ทั้งหมด
    def findHamiltonianPath(self):
        allPath = self.findAllPath()
        hamilPath = []
        
        for path in allPath[0]:
            
            if len(path) == len(self.matrix):
                hamilPath.append(path)
        return hamilPath

    # hamiltonian path มาเช็คว่าตำแหน่ง start กับ end มี edge ไหม ถ้ามี adjacency[start][end] = 1
    def findHamiltonianCycle(self): 
        allHamiltonianPath = self.findHamiltonianPath()
        hamilCycle = []
        for hamilPath in allHamiltonianPath:
                start =  hamilPath[0] 
                stop = hamilPath[-1]
                if self.matrix[start][stop] > 0 :
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
