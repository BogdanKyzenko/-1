
class Road:
    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight
 
 
class Graph:
    def __init__(self, n):
        self.n = n
        self.roads = []  
 
    def add_road(self, src, dst, weight):
        self.roads.append(Road(src, dst, weight))
 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
 
    def kruskal_mst(self):
        result = []  
        i = 0  
        e = 0  
        self.roads = sorted(self.roads, key=lambda road: road.weight)  
        parent = [i for i in range(self.n+1)]  
        rank = [0] * (self.n+1)  
        while e < self.n-1:  
            road = self.roads[i]
            i += 1
            root_src = self.find(parent, road.src)
            root_dst = self.find(parent, road.dst)
            if root_src != root_dst:  
                e += 1
                result.append(road)
                self.union(parent, rank, root_src, root_dst)                                          
        return result
 
 
def find_min_distance(n, m, roads):
    g = Graph(n)
    for src, dst, weight in roads:
        g.add_road(src, dst, weight)
    kruskal_roads = g.kruskal_mst()
    return sum(road.weight for road in kruskal_roads)


n = 5
m = 7
roads = [
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 3),
    (2, 4, 2),
    (2, 5, 5),
    (3, 4, 4),
    (4, 5, 1)
]
min_distance = find_min_distance(n, m, roads)
print(min_distance)
