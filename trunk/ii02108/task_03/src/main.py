from customtkinter import *
from  graphs import *
from  random import  randint



class Vertex:
        def __init__(self, name: str) -> None:
            self.name = name
            self.x = randint(0, 1000)#поменять на нормальные значения
            self.y = randint(0, 1000)#поменять на нормальные значения
            self.radius = 15
            self.color = 'black'


        def rename(self, name):
            self.name = name
            '''перерисовать вершину''' # <====================================================

        def move(self, x, y):
            self.x = x
            self.y = y
            '''перерисовать вершину''' # <====================================================


class Edge:
    def __init__(self, vertex1: tuple, vertex2: tuple, weight: int, oriented: bool) -> None:
        self.weight = weight
        self.vertex1x, self.vertex1y = vertex1
        self.vertex2x, self.vertex2y = vertex2

        self.is_oriented = oriented
        self.is_loop = True if self.vertex1x == self.vertex2x and self.vertex1y == self.vertex2y else False

        self.color = 'black'
        self.thickness = 2


    def change_weight(self, weight):
        self.weight = weight
        '''перерисовать ребро''' # <====================================================
    
    def move(self, vertex1: tuple, vertex2: tuple):
        self.vertex1x, self.vertex1y = vertex1
        self.vertex2x, self.vertex2y = vertex2
        '''перерисовать ребро''' # <====================================================


class Workspace:
    def __init__(self) -> None:
        self.graph = Graph()
        self.vertexes = []
        self.edges = []
    
    
    def add_vertex(self, name):
        """при нажатии на кнопку будет вылезать окно и спрашивать имя вершины"""
        self.graph.add_vertex()
        self.vertexes.append(Vertex(name))
        '''после добавления вершины надо ее отрисовать''' # <========================================================

    def add_edge(self, vertex1: int, vertex2: int, weight=1, oriented: bool = False):
        """при нажатии на кнопку будет вылезать окно и спрашивать вес ребра и ориентированность"""
        if oriented:
            self.graph.add_orient_edge(vertex1, vertex2, weight)
        else:
            self.graph.add_unorient_edge(vertex1, vertex2, weight)
        vertex1_coords = (self.vertexes[vertex1].x, self.vertexes[vertex1].y)
        vertex2_coords = (self.vertexes[vertex2].x, self.vertexes[vertex2].y)
        self.edges.append(Edge(vertex1_coords, vertex2_coords, weight, oriented))
        '''после добавления ребра надо его отрисовать(линию и стрелку(если надо))''' # <=========================================================


    def save(self):
        pass

    def export_to_text(self):
        pass

    def import_from_text(self):
        pass


    def HIDE(self):
        pass

    def SHOW(self):
        pass



def main():
    root = CTk()
    root.title('Graphs Editor Pro')
    root.geometry("1600x900+150+100")
    root.resizable(False, False)

    

    root.mainloop()

main()
