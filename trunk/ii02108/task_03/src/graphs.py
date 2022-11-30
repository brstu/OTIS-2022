class Graph:
    def __init__(self) -> None:
        self.vertexes_count = 0
        self.adjacency_matrix = []
        self.edges = []
        self.edges_count = 0
        self.number = 0

    # CREATE GRAPH ============================================================

    def add_vertex(self):
        self.vertexes_count += 1
        for i in range(self.vertexes_count-1):
            self.adjacency_matrix[i].append(0)
        self.adjacency_matrix.append([0 for i in range(self.vertexes_count)])

    def add_unorient_edge(self, vertex1: int, vertex2: int, weight=1):
        self.edges.append((vertex1, vertex2, weight))
        self.edges.append((vertex2, vertex1, weight))
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight
        self.edges_count += 2

    def add_orient_edge(self, vertex1: int, vertex2: int, weight=1):
        self.edges.append((vertex1, vertex2, weight))
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.edges_count += 1

    def del_vertex(self, vertex: int):
        self.vertexes_count -= 1
        self.adjacency_matrix.pop(vertex)
        for i in range(self.vertexes_count):
            self.adjacency_matrix[i].pop(vertex)
    
    def del_edge(self, edge : tuple):
        self.edges.remove(edge)
        self.adjacency_matrix[edge[0]][edge[1]] = 0
        self.adjacency_matrix[edge[1]][edge[0]] = 0

    def get_vertexes_count(self):
        return self.vertexes_count

    def get_degree(self, vertex: int):
        degree = 0
        for i in range(self.vertexes_count):
            if self.adjacency_matrix[vertex][i]:
                degree += 1
        return degree
    
    def get_incidence_matrix(self): # TODO
        incidence_matrix = [[0 for i in range(self.edges_count)] for j in range(self.vertexes_count)]
        for i, edge in enumerate(self.edges):
            incidence_matrix[edge[0]][i] = self.edges[2]
            incidence_matrix[edge[1]][i] = self.edges[2]
        return incidence_matrix

    def show_adj_matr(self):
        adj_matr = ''
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                adj_matr += str(self.adjacency_matrix[i][j]) + ' '
            adj_matr += '\n'
        return adj_matr
    
    def show_inc_matr(self):
        inc_matr = ''
        for i in range(self.vertexes_count):
            for j in range(self.edges_count):
                inc_matr += str(self.incidence_matrix[i][j]) + ' '
            inc_matr += '\n'
        return inc_matr


    # ALGORITHMS ================================================================

    def dfs(self, vertex: int, visited: list):
        visited[vertex] = True
        for i in range(self.vertexes_count):
            if self.adjacency_matrix[vertex][i] and not visited[i]:
                self.dfs(i, visited)
    
    def bfs(self, vertex: int, visited: list):
        queue = [vertex]
        visited[vertex] = True
        while queue:
            vertex = queue.pop(0)
            for i in range(self.vertexes_count):
                if self.adjacency_matrix[vertex][i] and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def get_components(self):
        '''Получить компоненты связности'''
        visited = [False for i in range(self.vertexes_count)]
        components = []
        for i in range(self.vertexes_count):
            if not visited[i]:
                component = []
                self.dfs(i, visited)
                for j in range(self.vertexes_count):
                    if visited[j]:
                        component.append(j)
                components.append(component)
        return components
    
    def get_eulerian_cycle(self):
        '''Получить Эйлеров цикл'''
        if not self.is_connected():
            return None
        for i in range(self.vertexes_count):
            if self.get_degree(i) % 2:
                return None
        cycle = [0]
        visited = [False for i in range(self.vertexes_count)]
        visited[0] = True
        while len(cycle) < self.edges_count:
            for i in range(self.vertexes_count):
                if self.adjacency_matrix[cycle[-1]][i] and not visited[i]:
                    cycle.append(i)
                    visited[i] = True
                    break
            else:
                return None
        return cycle
    
    def get_hamiltonian_cycle(self):
        '''Получить Гамильтонов цикл'''
        if not self.is_connected():
            return None
        cycle = [0]
        visited = [False for i in range(self.vertexes_count)]
        visited[0] = True
        while len(cycle) < self.vertexes_count:
            for i in range(self.vertexes_count):
                if self.adjacency_matrix[cycle[-1]][i] and not visited[i]:
                    cycle.append(i)
                    visited[i] = True
                    break
            else:
                return None
        return cycle

    def get_all_paths(self, vertex1: int, vertex2: int):
        paths = []
        stack = [(vertex1, [vertex1])]
        while stack:
            vertex, path = stack.pop()
            for i in range(self.vertexes_count):
                if self.adjacency_matrix[vertex][i] and i not in path:
                    if i == vertex2:
                        paths.append(path + [i])
                    else:
                        stack.append((i, path + [i]))
        return paths
    
    def get_shortest_path(self, vertex1: int, vertex2: int):
        paths = self.get_all_paths(vertex1, vertex2)
        if not paths:
            return None
        return min(paths, key=len)
    
    def get_distance(self, vertex1: int, vertex2: int):
        distance = 0
        for i in self.get_shortest_path(vertex1, vertex2):
            distance += self.adjacency_matrix[i][i+1]
        return distance
    
    def get_diameter(self):
        diameter = 0
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                if i != j:
                    diameter = max(diameter, self.get_distance(i, j))
        return diameter
    
    def get_radius(self):
        radius = float('inf')
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                if i != j:
                    radius = min(radius, self.get_distance(i, j))
        return radius

    def get_center(self):
        center = []
        radius = self.get_radius()
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                if i != j and self.get_distance(i, j) == radius:
                    center.append(i)
                    break
        return center


    # CHECKS ====================================================================    
    
    def is_tree(self):
        '''Является ли граф деревом'''
        return self.vertexes_count == self.edges_count + 1

    def is_full(self):
        '''Является ли граф полным'''
        return self.edges_count == self.vertexes_count * (self.vertexes_count - 1) / 2
    
    def is_connected(self):
        '''Является ли граф связным'''
        visited = [False for i in range(self.vertexes_count)]
        self.dfs(0, visited)
        return all(visited)
    
    def is_eulerian(self):
        '''Является ли граф Эйлеровым'''
        return all(self.get_degree(i) % 2 == 0 for i in range(self.vertexes_count))

    def is_hamiltonian(self):
        '''Является ли граф Гамильтоновым'''
        return all(self.get_degree(i) >= 2 for i in range(self.vertexes_count))
    


def main():
    a = Graph()
    a.add_vertex()
    a.add_vertex()
    a.add_vertex()
    # a.add_vertex()

    a.add_orient_edge(0, 1, 4)
    a.add_orient_edge(0, 2, 3)
    a.add_orient_edge(1, 2, 5)

    print(a.adjacency_matrix)
    print(a.get_degree(0))
    print(a.get_degree(1))
    print(a.get_degree(2))

    print(a.get_eulerian_cycle())

# main()
