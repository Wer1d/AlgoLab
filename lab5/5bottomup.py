import math
import sys
# สังเกตว่า
# n-polygon มีได้ n-2 sub-triangle
# 6 เหลี่ยม มีได้ 3 เส้น -> 9 แบบ
# 5 เหลี่ยม มีได้ 2 เส้น -> 5 แบบ
# 4 เหลี่ยม มีได้ 1 เส้น -> 2 แบบ
# 3 เหลี่ยม มีได้ 0 เส้น
# Number of Diagonals= n(n−3)/2
def dist(coor1:list, coor2:list) -> float:
    x1,y1 = coor1
    x2,y2 = coor2
    return (((abs(x1-x2))**2 + (abs(y1-y2))**2))**0.5

def cost(coor1:list, coor2:list, coor3:list)-> float:
    return dist(coor1, coor2) + dist(coor2, coor3) + dist(coor3, coor1)

def polar_angle(coor1: list, coor2: list) -> float:
    x1, y1 = coor1
    x2, y2 = coor2
    return math.atan2(y2 - y1, x2 - x1)

def min_cost_triangulation(vertices : list) -> float:
    num_vertices = len(vertices)
    dp = [[0] * num_vertices for _ in range(num_vertices)]
    ref_vertex = min(vertices, key=lambda vertex: (vertex[1], vertex[0]))

    vertices.sort(key=lambda vertex: (polar_angle(ref_vertex, vertex), vertex))
    print(vertices)

    dp = [[0] * num_vertices for _ in range(num_vertices)]
    for diagonal in range(num_vertices):
        i = 0
        for j in range(diagonal, num_vertices):
            if j - i >= 2:
                dp[i][j] = sys.maxsize
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cost(vertices[i], vertices[k], vertices[j]))
                    # print(dp)
            i += 1
       
    return dp[0][-1]
vertices = []
with open('./lab5/test.txt', 'r') as f:
    num_vertices = int(f.readline().strip())
    for _ in range(num_vertices):
        vertices.append(list(map(float, f.readline().strip().split()) ))
print("num_vertices : " ,num_vertices)
print(min_cost_triangulation(vertices))
f.close()