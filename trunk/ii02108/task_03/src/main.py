from customtkinter import *
from tkinter import Menu, PhotoImage
from graphs import *
from config import *

def create_circle(canvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

class Vertex:
    def __init__(self, canvas, name: int | str, x: int, y: int) -> None:
        self.name = str(name)
        self.x = x
        self.y = y
        self.radius = 15
        self.color = 'black'
        self.text_color = 'white'

        self.canvas = canvas

        self.circle = create_circle(self.canvas, self.x, self.y, self.radius, fill=self.color)
        self.text = self.canvas.create_text(self.x, self.y, text=self.name, font='Arial 10', fill=self.text_color)

    
    def show_properties(self, event):
        props_vert = CTk()
        props_vert.wm_attributes('-topmost', '1')
        props_vert.title(f'Vertex: {self.name} properties')
        props_vert.geometry(f'300x300+{event.x-250}+{event.y-800}')

        name_entry = CTkEntry(props_vert, text='Enter name', justify='center')
        name_entry.insert(0, self.name)
        name_entry.place(anchor='n', relx=0.5, rely=0.1)
        name_entry.bind('<Return>', lambda event: self.rename(name_entry.get()))

        clrbtn_1 = CTkButton(props_vert, corner_radius=0, fg_color='red', text='', command=lambda: self.change_color('red'))
        clrbtn_2 = CTkButton(props_vert, corner_radius=0, fg_color='purple', text='', command=lambda: self.change_color('purple'))
        clrbtn_3 = CTkButton(props_vert, corner_radius=0, fg_color='blue', text='', command=lambda: self.change_color('blue'))
        clrbtn_4 = CTkButton(props_vert, corner_radius=0, fg_color='green', text='', command=lambda: self.change_color('green'))
        clrbtn_5 = CTkButton(props_vert, corner_radius=0, fg_color='yellow', text='', command=lambda: self.change_color('yellow'))
        clrbtn_6 = CTkButton(props_vert, corner_radius=0, fg_color='orange', text='', command=lambda: self.change_color('orange'))
        clrbtn_7 = CTkButton(props_vert, corner_radius=0, fg_color='brown', text='', command=lambda: self.change_color('brown'))
        clrbtn_8 = CTkButton(props_vert, corner_radius=0, fg_color='black', text='', command=lambda: self.change_color('black'))
        clrbtn_9 = CTkButton(props_vert, corner_radius=0, fg_color='#FF00FF', text='', command=lambda: self.change_color('#FF00FF'))
        clrbtn_10= CTkButton(props_vert, corner_radius=0, fg_color='#00FF00', text='', command=lambda: self.change_color('#00FF00'))

        clrbtn_1.place(anchor='nw', relx=0, rely=0.28, relheight=0.2)
        clrbtn_2.place(anchor='nw', relx=0.33, rely=0.28, relheight=0.2)
        clrbtn_3.place(anchor='nw', relx=0.66, rely=0.28, relheight=0.2)
        clrbtn_4.place(anchor='nw', relx=0, rely=0.48, relheight=0.2)
        clrbtn_5.place(anchor='nw', relx=0.33, rely=0.48, relheight=0.2)
        clrbtn_6.place(anchor='nw', relx=0.66, rely=0.48, relheight=0.2)
        clrbtn_7.place(anchor='nw', relx=0, rely=0.68, relheight=0.2)
        clrbtn_8.place(anchor='nw', relx=0.33, rely=0.68, relheight=0.2)
        clrbtn_9.place(anchor='nw', relx=0.66, rely=0.68, relheight=0.2)
        clrbtn_10.place(anchor='nw', relx=0, rely=0.88, relwidth=1, relheight=0.2)
        
        props_vert.mainloop()


    def rename(self, name):
        self.name = name
        self.canvas.delete(self.text)
        self.text = self.canvas.create_text(self.x, self.y, text=self.name, font='Arial 10', fill=self.text_color)
        '''перерисовать вершину''' # <====================================================

    def change_color(self, color):
        self.color = color
        self.canvas.delete(self.circle)
        self.canvas.delete(self.text)
        self.circle = create_circle(self.canvas, self.x, self.y, self.radius, fill=self.color)
        if color in ['red', 'purple', 'blue', 'brown', 'black', 'green']:
            self.text_color = 'white'
        else:
            self.text_color = 'black'
        self.text = self.canvas.create_text(self.x, self.y, text=self.name, font='Arial 10', fill=self.text_color)

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
        self.is_loop = self.vertex1x == self.vertex2x and self.vertex1y == self.vertex2y

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
        self.id_vert = 0

        self.add_vert_btn = CTkButton(root, text='Добавить вершину', command=self.add_vertex, bg_color=btns_color) # <====================================================
        self.add_edge_btn = CTkButton(root, text='Добавить ребро', command=lambda: print('Добавить ребро'), bg_color=btns_color) # <====================================================
        self.del_vert_btn = CTkButton(root, text='Удалить вершину', command=lambda: print('Удалить вершину'), bg_color=btns_color) # <====================================================
        self.del_edge_btn = CTkButton(root, text='Удалить ребро', command=lambda: print('Удалить ребро'), bg_color=btns_color) # <====================================================

        

        self.is_tab_opened = True
        self.canvas = CTkCanvas(root, width=1445, height=1755, bg='#D3D3D3')


        self.tab_btn = CTkButton(root, text=self.name[0:12], command=self.SHOW, bg_color=btns_color,
                                 fg_color='white')
        self.close_tab_btn = CTkButton(root, image=PhotoImage(file=path_to_img_close_tab), 
                                    text='', bg_color=btns_color, fg_color=close_tab_button, hover_color='darkred',
                                    command=self.DEL)
        self.tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*len(workspaces), width=110)
        self.close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*len(workspaces), width=30)

        self.canvas.bind('<Button-3>', self.show_properties)

        self.SHOW()
        '''рисовать все канвасы и т.д.''' # <====================================================

    def exit(self, event):
        print(6567)

    def show_properties(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                vertex.show_properties(event)
                break
        else:
            print('Свойства ребра')
    
    def add_vertex(self):
        # operation = 'add_vertex'
        """при нажатии на кнопку будет вылезать окно и спрашивать имя вершины"""
        self.canvas.bind('<Button-1>', self.add_vertex_click)
        '''после добавления вершины надо ее отрисовать''' # <========================================================

    def add_vertex_click(self, event):
        self.graph.add_vertex()
        self.vertexes.append(Vertex(self.canvas, self.id_vert, event.x, event.y))
        self.id_vert += 1
        

    def add_edge(self, vertex1: int, vertex2: int, weight=1, oriented: bool = False):
        operation = 'add_edge'
        # """при нажатии на кнопку будет вылезать окно и спрашивать вес ребра и ориентированность"""
        # if oriented:
        #     self.graph.add_orient_edge(vertex1, vertex2, weight)
        # else:
        #     self.graph.add_unorient_edge(vertex1, vertex2, weight)
        # vertex1_coords = (self.vertexes[vertex1].x, self.vertexes[vertex1].y)
        # vertex2_coords = (self.vertexes[vertex2].x, self.vertexes[vertex2].y)
        # self.edges.append(Edge(vertex1_coords, vertex2_coords, weight, oriented))
        # '''после добавления ребра надо его отрисовать(линию и стрелку(если надо))''' # <=========================================================


    def save(self):
        pass

    def export_to_text(self):
        pass

    def import_from_text(self):
        pass


    def HIDE(self):
        self.canvas.place_forget()
        self.tab_btn.configure(fg_color=default_btn_clr)

        self.add_vert_btn.place_forget()
        self.add_edge_btn.place_forget()
        self.del_vert_btn.place_forget()
        self.del_edge_btn.place_forget()

    def SHOW(self):
        for workspace in workspaces:
            workspace.HIDE()
        self.canvas.place(anchor='w')

        self.tab_btn.configure(fg_color=selected_tab_clr)
        
        self.add_vert_btn.place(anchor='ne', relx=0.997, rely=0.01)
        self.add_edge_btn.place(anchor='ne', relx=0.997, rely=0.05)
        self.del_vert_btn.place(anchor='ne', relx=0.997, rely=0.09)
        self.del_edge_btn.place(anchor='ne', relx=0.997, rely=0.13)

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


    create_new_graph_btn = CTkButton(root, text='', bg_color=btns_color, fg_color=add_tab_button,
                                    image=PhotoImage(file=path_to_img_create_new_tab), 
                                    corner_radius=5, command=add_new_tab)
    create_new_graph_btn.place(anchor='w', relx=0.9097, rely=0.3)

    root.bind('q', ex)
    root.mainloop()


def add_new_tab():
    for workspace in workspaces:
        workspace.is_tab_opened = False
        workspace.tab_btn.configure(fg_color=default_btn_clr)
    graph = Workspace()
    workspaces.append(graph)


workspaces = []
operation = ''
def ex(event):
    global root
    root.destroy()

main()
