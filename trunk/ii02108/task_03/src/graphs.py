class Graph:
    def __init__(self, adj_matr = None) -> None:
        self.vertexes_count = 0
        self.edges = []
        self.edges_count = 0

        if adj_matr is None:
            self.adjacency_matrix = []
        else:
            self.adjacency_matrix = [i.copy() for i in adj_matr]
            self.vertexes_count = len(self.adjacency_matrix)

            if adj_matr:
                for i in range(self.vertexes_count):
                    for j in range(self.vertexes_count):
                        if self.adjacency_matrix[i][j]:
                            self.edges.append([i, j, self.adjacency_matrix[i][j], self.adjacency_matrix[i][j]!=self.adjacency_matrix[j][i]])
                            self.edges_count += 1
                            if self.adjacency_matrix[i][j] == self.adjacency_matrix[j][i]:
                                self.adjacency_matrix[j][i] = 0
                self.adjacency_matrix = [i.copy() for i in adj_matr]


    # CREATE GRAPH ============================================================

    def add_vertex(self):
        self.vertexes_count += 1
        for i in range(self.vertexes_count-1):
            self.adjacency_matrix[i].append(0)
        self.adjacency_matrix.append([0 for i in range(self.vertexes_count)])

    def add_unorient_edge(self, vertex1: int, vertex2: int, weight=1):
        self.edges.append([vertex1, vertex2, weight, False])
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight
        self.edges_count += 1

    def add_orient_edge(self, vertex1: int, vertex2: int, weight=1):
        self.edges.append([vertex1, vertex2, weight, True])
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.edges_count += 1

    def del_vertex(self, vertex: int):
        self.vertexes_count -= 1
        self.adjacency_matrix.pop(vertex)
        for i in range(self.vertexes_count):
            self.adjacency_matrix[i].pop(vertex)
        for edge in self.edges:
            if edge[0] == vertex or edge[1] == vertex:
                self.edges.remove(edge)
                self.edges_count -= 1
        for edge in self.edges:
            if edge[0] > vertex:
                edge[0] -= 1
            if edge[1] > vertex:
                edge[1] -= 1

    def del_edge(self, vertex1: int, vertex2: int):
        for edge in self.edges:
            if edge[0] == vertex1 and edge[1] == vertex2:
                self.edges.remove(edge)
                self.edges_count -= 1
                break
        self.adjacency_matrix[vertex1][vertex2] = 0
        self.adjacency_matrix[vertex2][vertex1] = 0

    def get_vertexes_count(self):
        return self.vertexes_count

    def get_degree(self, vertex: int):
        degree = 0
        for i in range(self.vertexes_count):
            if self.adjacency_matrix[vertex][i]:
                degree += 1
        return degree

    def get_adj_matrix(self):
        return self.adjacency_matrix

    def get_inc_matrix(self):
        adj_matr = self.get_adj_matrix()
        incidence_matrix = [[0 for i in range(self.edges_count)] for j in range(self.vertexes_count)]
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                if adj_matr[i][j]:
                    for k in range(self.edges_count):
                        if self.edges[k][0] == i and self.edges[k][1] == j:
                            if adj_matr[i][j] == adj_matr[j][i]:
                                incidence_matrix[i][k] = adj_matr[i][j]
                                incidence_matrix[j][k] = adj_matr[i][j]
                            else:
                                incidence_matrix[i][k] = adj_matr[i][j]
                                incidence_matrix[j][k] = -adj_matr[i][j]
        return incidence_matrix

    def show_adj_matrix(self):
        adj_matr = ''
        for i in range(self.vertexes_count):
            for j in range(self.vertexes_count):
                adj_matr += str(self.adjacency_matrix[i][j]) + ' '
            adj_matr += '\n'
        return adj_matr

    def show_inc_matrix(self):
        inc_matr = self.get_inc_matrix()
        string = ''
        for i in range(self.vertexes_count):
            for j in range(self.edges_count):
                string += str(inc_matr[i][j]) + ' '
            string += '\n'
        return string


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
        if not self.is_connected():
            return None
        for i in range(self.vertexes_count):
            if self.get_degree(i) % 2 != 0:
                return None
        adj = [i.copy() for i in self.adjacency_matrix]
        path = []
        s = []
        poz = 0
        s.append(poz)
        while s:
            poz = s[-1]
            temp = False
            for i, _ in enumerate(adj[0]):
                if (adj[poz][i]):
                    adj[poz][i] = 0
                    adj[i][poz] = 0
                    s.append(i)
                    temp = True
                    break
            if not temp:
                path.append((poz))
                s.pop()
        return path

    def get_hamiltonian_cycle(self):
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
        '''смотрит на веса ребер'''
        paths = self.get_all_paths(vertex1, vertex2)
        lengths = [0 for _ in paths]
        for i, _ in enumerate(paths):
            for j, _ in enumerate(paths[i][:-1]):
                lengths[i] += self.adjacency_matrix[paths[i][j]][paths[i][j+1]]
        min_index = lengths.index(min(lengths))
        return paths[min_index]

    def get_distance(self, vertex1: int, vertex2: int):
        distance = 0
        path = self.get_shortest_path(vertex1, vertex2)
        for i, vertex in enumerate(path[:-1]):
            distance += self.adjacency_matrix[vertex][path[i+1]]
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
        return self.vertexes_count == self.edges_count + 1

    def is_full(self):
        return self.edges_count == self.vertexes_count * (self.vertexes_count - 1) / 2

    def is_connected(self):
        visited = [False for i in range(self.vertexes_count)]
        self.dfs(0, visited)
        return all(visited)

    def is_eulerian(self):
        return all(self.get_degree(i) % 2 == 0 for i in range(self.vertexes_count))

    def is_hamiltonian(self):
        return all(self.get_degree(i) >= 2 for i in range(self.vertexes_count))


def inc_to_adj(incidence_matrix):
    '''Translating Incident Matrix to Adjacency Matrix'''
    vertexes_count = len(incidence_matrix)
    edges_count = len(incidence_matrix[0])
    adjacency_matrix = [[0 for i in range(vertexes_count)] for j in range(vertexes_count)]
    for i in range(vertexes_count):
        for j in range(edges_count):
            if incidence_matrix[i][j] > 0:
                for k in range(vertexes_count):
                    if incidence_matrix[k][j] > 0 and k != i:
                        adjacency_matrix[i][k] = incidence_matrix[i][j]
                        adjacency_matrix[k][i] = incidence_matrix[i][j]
                    elif incidence_matrix[k][j] < 0 and k != i:
                        adjacency_matrix[i][k] = incidence_matrix[i][j]
                        adjacency_matrix[k][i] = 0
            elif incidence_matrix[i][j] < 0:
                for k in range(vertexes_count):
                    if incidence_matrix[k][j] > 0 and k != i:
                        adjacency_matrix[i][k] = 0
                        adjacency_matrix[k][i] = -incidence_matrix[i][j]
                    elif incidence_matrix[k][j] < 0 and k != i:
                        adjacency_matrix[i][k] = incidence_matrix[i][j]
                        adjacency_matrix[k][i] = incidence_matrix[i][j]
    return adjacency_matrix