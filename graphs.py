class graphs():
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for i in range(vertices)] for i in range(vertices)]

    def addedge(self, v1, v2):
        self.edges[v1][v2] = 1
        self.edges[v2][v1] = 1

    def removeedge(self, v1, v2):
        if self.edges[v1][v2] != 0:
            self.edges[v1][v2] = 0
            self.edges[v2][v1] = 0
        else:
            print("no edge is present")

    def print(self):
        print(self.edges)

    def containsedge(self, v1, v2):
        return True if self.edges[v1][v2] == 1 else False

    def helper_dfs(self, sv, visited):
        print(sv)
        visited[sv] = True
        for i in range(self.vertices):
            if self.edges[sv][i] > 0 and visited[i] == False:
                self.helper_dfs(i, visited)

    def dfs(self):
        visited = [False for i in range(self.vertices)]
        self.helper_dfs(0, visited)

    def bfs(self):
        a = []
        a.append(0)
        visited = [False for i in range(self.vertices)]
        visited[0] = True
        while len(a) != 0:
            b = a.pop(0)
            print(b)
            for i in range(self.vertices):
                if self.edges[i][b] > 0 and visited[i] == False:
                    a.append(i)
                    visited[i] = True

    def haspath(self, v1, v2):
        pass


g1 = graphs(6)
g1.addedge(0, 1)
g1.addedge(0, 2)
g1.addedge(0, 5)
g1.addedge(1, 3)
g1.addedge(1, 4)
# g1.bfs()
g1.dfs()
