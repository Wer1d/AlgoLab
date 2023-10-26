class Graph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix

    def __str__(self):
        result = ""
        for row in self.adj_matrix:
            result += "\t".join(map(str, row)) + "\n"
        return result

    def find_quietest_paths(self):
        n = len(self.adj_matrix)
        noise = [[0 if i == j else float("inf") if self.adj_matrix[i][j] == 0 else self.adj_matrix[i][j] for j in range(n)] for i in range(n)]
        # travel itself = 0, no path = inf, else = noise from adj matrix
        pi = [[j if noise[i][j] != float("inf") else -1 for j in range(n)] for i in range(n)]
        # ถ้ามีเส้นทางจะเก็บ j ไว้ ถ้าไม่มีเส้นทางจะเก็บ -1 ไว้ ใช้เพื่อเก็บเส้นทางที่เดินไปแล้ว ใช้ในการ reconstruct path
        # for reconstruction

        # floyd warshall
        for k in range(n):
            # D(k) i,j 
            # k = 1 แปลว่าแวะที่ vertex 1 
            for i in range(n):
                for j in range(n):
                    alternative_path_noise = max(noise[i][k], noise[k][j]) # มองเป็นเดินจาก i->j ผ่าน k แล้วเก็บ weight มากสุด
                    if alternative_path_noise < noise[i][j]: # ถ้า noise ที่เดินผ่าน k มากกว่า noise เดิม
                        noise[i][j] = alternative_path_noise
                        pi[i][j] = pi[i][k] 
                        # เช่น D(1)1,4 ตอนแรกจะเป็น inf แต่พอ k = 2 มันจะเดินผ่านได้ แล้วเก็บ max ระหว่าง 1->2 กับ 2->4 มาเป็น D(2)1,4 แทน ถ้าของใหม่ < เก่า 
                        # จากนั้นก็เก็บ pi ว่า 1->4 มาจาก 1->2 
                    # For Debug
                    # if k == 1 and i < 3 :
                    #     print(f"Noise matrix for k = {k+1} i = {i} j = {j} : ")
                    #     for row in noise:
                    #         print("\t".join(map(str, row)))
                    #     print()
            
        return noise, pi

    def find_quietest_path(self, i, j):
        i = i-1
        j = j-1
        noise, pi = self.find_quietest_paths() # matrix noise
        
        print("i", i, "j", j)
        if i < 0 or j < 0 or i >= len(noise) or j >= len(noise):
            return "Invalid input"
        elif noise[i][j] == float("inf"):
            return "No path"
        elif noise[i][j] == 0:
            return "Same town"
        else:
            return str(noise[i][j]) # noise from i to j city

    def reconstruct_path(self, u, v):
        noise, pi = self.find_quietest_paths()
        path = []
        print(len(pi))
        u = u-1
        v = v-1
        if pi[u][v] == -1:
            return path  # no path between u and v
        path.append(u + 1)
        while u != v:
            u = pi[u][v]
            path.append(u + 1)
        return path

def main():
    num_town, num_road, num_ans = 0, 0, 0
    graph = None
    adj_matrix = None
    ans = None
   
    with open("./lab7/input.txt", "r") as file:
        lines = file.readlines()
        num_town, num_road, num_ans = map(int, lines[0].split())
        adj_matrix = [[0 for _ in range(num_town)] for _ in range(num_town)]
        for i in range(1, num_road + 1):
            u, v, noise = map(int, lines[i].split())
            u, v = u - 1, v - 1
            adj_matrix[u][v] = noise
            adj_matrix[v][u] = noise
        ans = [list(map(int, line.split())) for line in lines[num_road + 1:]] # store path to find

   
    graph = Graph(adj_matrix)
    print(graph)
    for i in range(len(ans)):
        print(f"From {ans[i][0]} to {ans[i][1]}")
        print("Weight:", graph.find_quietest_path(ans[i][0], ans[i][1])) # ans ที่ใส่ไปเป็น params ยังไม่ปรับเป็นเริ่มจาก index 0 
        # หาเส้นทาง

        print("Path:", graph.reconstruct_path(ans[i][0], ans[i][1]))
        # สร้าง path วิธีเดิน
        print("-----------------------------------------------------------")

if __name__ == "__main__":
    main()
