from customtkinter import *
from tkinter import Menu, PhotoImage
from random import  randint
from graphs import *
from config import *



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
    
    def change_color(self, color):
        self.color = color
        '''перерисовать ребро''' # <====================================================
    
    def move(self, vertex1: tuple, vertex2: tuple):
        self.vertex1x, self.vertex1y = vertex1
        self.vertex2x, self.vertex2y = vertex2
        '''перерисовать ребро''' # <====================================================

    


class Workspace:
    def __init__(self, name: str = 'Безымянный') -> None:
        self.name = name
        self.graph = Graph()
        self.vertexes = []
        self.edges = []

        self.is_tab_opened = True
        self.canvas = CTkCanvas(root, width=1445, height=1755, bg='#D3D3D3')
        self.canvas.place(anchor='w')


        self.tab_btn = CTkButton(root, text=self.name[0:12], command=self.SHOW, bg_color=btns_color,
                                 fg_color='white')
        self.close_tab_btn = CTkButton(root, image=PhotoImage(file=path_to_img_close_tab), 
                                    text='', bg_color=btns_color, fg_color=close_tab_button, hover_color='darkred',
                                    command=self.DEL)
        self.tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*len(workspaces), width=110)
        self.close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*len(workspaces), width=30)

        '''рисовать все канвасы и т.д.''' # <====================================================

    
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
        self.canvas.place_forget()
        self.tab_btn.configure(fg_color=default_btn_clr)

    def SHOW(self):
        for workspace in workspaces:
            workspace.HIDE()
        self.canvas.place(anchor='w')

        self.tab_btn.configure(fg_color=selected_tab_clr)
        print(self.name.upper())

    def DEL(self):
        self.canvas.destroy()
        self.tab_btn.destroy()
        self.close_tab_btn.destroy()
        workspaces.remove(self)
        for i in range(len(workspaces)):
            workspaces[i].tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*i, width=110)
            workspaces[i].close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*i, width=30)



def main():

    global workspaces
    workspaces = []

    global root
    root = CTk()
    root.title('Graphs Editor Pro')
    root.geometry("1600x900+150+100")
    root.resizable(False, False)
    root.set_appearance_mode(main_theme)

    # Раздел меню
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Новый", command=lambda: print('Открыть')) # <====================================================
    filemenu.add_command(label="Открыть", command=lambda: print('Открыть')) # <====================================================
    filemenu.add_command(label="Сохранить", command=lambda: print('Сохранить')) # <====================================================
    filemenu.add_separator()
    filemenu.add_command(label="Экспорт в текст", command=lambda: print('Экспорт в текст')) # <====================================================
    filemenu.add_command(label="Импорт из текста", command=lambda: print('Импорт из текста')) # <====================================================

    algsmenu = Menu(mainmenu, tearoff=0)
    algsmenu.add_command(label="Кол-во вершин", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Степени вершин", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Матрица смежности", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Матрица инцидентности", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Граф - дерево?", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Граф полный?", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Граф эйлеров?", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Граф гамильтонов?", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_separator()
    algsmenu.add_command(label="Поиск кратчайшего пути", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Нахождение наименьшего расстояния", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Нахождние центра", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Нахождние диаметра", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Нахождние радиуса", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Нахождние радиуса", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Поиск эйлерова цикла", command=lambda: print('Алгоритм Дейкстры')) # <====================================================
    algsmenu.add_command(label="Поиск гамильтонова цикла", command=lambda: print('Алгоритм Дейкстры')) # <====================================================

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Алгоритмы", menu=algsmenu)


    # Раздел редактора
    add_vert_btn = CTkButton(root, text='Добавить вершину', command=lambda: print('Добавить вершину'), bg_color=btns_color) # <====================================================
    add_edge_btn = CTkButton(root, text='Добавить ребро', command=lambda: print('Добавить ребро'), bg_color=btns_color) # <====================================================
    del_vert_btn = CTkButton(root, text='Удалить вершину', command=lambda: print('Удалить вершину'), bg_color=btns_color) # <====================================================
    del_edge_btn = CTkButton(root, text='Удалить ребро', command=lambda: print('Удалить ребро'), bg_color=btns_color) # <====================================================

    add_vert_btn.place(anchor='ne', relx=0.997, rely=0.01)
    add_edge_btn.place(anchor='ne', relx=0.997, rely=0.05)
    del_vert_btn.place(anchor='ne', relx=0.997, rely=0.09)
    del_edge_btn.place(anchor='ne', relx=0.997, rely=0.13)




    create_new_graph_btn = CTkButton(root, text='', bg_color=btns_color, fg_color=add_tab_button,
                                    image=PhotoImage(file=path_to_img_create_new_tab), 
                                    corner_radius=5, command=add_new_tab)
    create_new_graph_btn.place(anchor='w', relx=0.9097, rely=0.3)

    root.mainloop()


def add_new_tab():
    for workspace in workspaces:
        workspace.is_tab_opened = False
        workspace.tab_btn.configure(fg_color=default_btn_clr)
    graph = Workspace()
    workspaces.append(graph)


workspaces = []


main()
