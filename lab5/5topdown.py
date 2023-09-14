import math
import sys
def dist(coor1: list, coor2: list) -> float:
    x1, y1 = coor1
    x2, y2 = coor2
    return (((abs(x1 - x2)) ** 2 + (abs(y1 - y2)) ** 2)) ** 0.5

def cost(coor1: list, coor2: list, coor3: list) -> float:
    return dist(coor1, coor2) + dist(coor2, coor3) + dist(coor3, coor1)

def polar_angle(coor1: list, coor2: list) -> float:
    x1, y1 = coor1
    x2, y2 = coor2
    return math.atan2(y2 - y1, x2 - x1)

def min_cost_triangulation(vertices: list) -> float:
    def dp(i, j):
        if j - i < 2:
            return 0  # No triangles to form
        print(memo)
        if memo[i][j] != 0:
            return memo[i][j]

        min_cost = sys.maxsize
        for k in range(i + 1, j):
            
            costt = dp(i, k) + dp(k, j) + cost(vertices[i], vertices[k], vertices[j])
            min_cost = min(min_cost, costt)
            
        memo[i][j] = min_cost
        
        return min_cost

    num_vertices = len(vertices)
    ref_vertex = min(vertices, key=lambda vertex: (vertex[1], vertex[0]))
    vertices.sort(key=lambda vertex: (polar_angle(ref_vertex, vertex), vertex))

    memo = [[0] * num_vertices for _ in range(num_vertices)]
    return dp(0, num_vertices - 1) # start from problem size

vertices = []
with open('./lab5/test.txt', 'r') as f:
    num_vertices = int(f.readline().strip())
    for _ in range(num_vertices):
        vertices.append(list(map(float, f.readline().strip().split())))

print("vertices:", vertices)
print(min_cost_triangulation(vertices))
f.close()
