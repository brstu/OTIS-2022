from random import randint
from customtkinter import *
from tkinter import Menu, PhotoImage, filedialog, Text
from graphs import *
# from algorithms import *
from config import *
from math import sqrt


import json

def create_circle(canvas: CTkCanvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def line_intersect_circle(x1, y1, x2, y2):
    '''Возвращает координаты точек пересечения прямой и двух окружностей'''
    main_gipotenusa = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenusa - vertex_radius) * main_dx / main_gipotenusa
    dy = (main_gipotenusa - vertex_radius) * main_dy / main_gipotenusa

    return x2 - dx, y2 - dy, x1 + dx, y1 + dy
    
class Vertex:
    def __init__(self, canvas, name: int | str, x: int, y: int, id_vert: int, color: str = 'black') -> None:
        self.name = str(name)
        self.id_vert = id_vert
        self.x = x
        self.y = y
        self.radius = vertex_radius
        self.color = color

        self.canvas = canvas
        
        # сделать выделение вершин (добавить окантовку)
        self.is_selected = False

        self.circle = create_circle(self.canvas, self.x, self.y, self.radius, fill=self.color)
        self.text = self.canvas.create_text(self.x, self.y, text=self.name, font=f'Arial {self.radius-5}', fill='white')

    
    def show_properties(self, event):
        props_vert = CTk()
        props_vert.wm_attributes('-topmost', '1')
        props_vert.title(f'Vertex: {self.name} properties')
        props_vert.geometry(f'300x300+{event.x+250}+{event.y}')

        name_entry = CTkEntry(props_vert, text='Введите имя', justify='center')
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
        self.canvas.itemconfig(self.text, text=self.name)

    def change_color(self, color):
        self.color = color
        self.canvas.itemconfig(self.circle, fill=self.color)
        if self.color in ('red', 'purple', 'blue', 'brown', 'black', 'green'):
            self.canvas.itemconfig(self.text, fill='white')
        else:
            self.canvas.itemconfig(self.text, fill='black')

    def move(self, x, y):
        self.x = x
        self.y = y
        if self.x < self.radius:
            self.x = self.radius
        elif self.x > 1445 - self.radius:
            self.x = 1445 - self.radius
        if self.y < self.radius:
            self.y = self.radius
        elif self.y > 875 - self.radius:
            self.y = 875 - self.radius
        self.canvas.coords(self.circle, self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)
        self.canvas.coords(self.text, self.x, self.y)

        


class Edge:
    def __init__(self, canvas, weight: int, vertex1: Vertex, vertex2: Vertex, oriented: bool, color='black') -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2

        self.weight = weight
        self.x1, self.y1 = vertex1.x, vertex1.y
        self.x2, self.y2 = vertex2.x, vertex2.y

        self.is_oriented = oriented
        self.is_loop = self.x1 == self.x2 and self.y1 == self.y2

        self.color = color
        self.thickness = vertex_radius // 5

        self.canvas = canvas

        
        if self.is_oriented:
            if self.is_loop:
                pass
            else:
                self.line = self.canvas.create_line(*line_intersect_circle(self.x1, self.y1, self.x2, self.y2), fill=self.color, width=self.thickness, arrow='last', arrowshape=(20, 15, 5))
                self.rect = self.canvas.create_rectangle((self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13, (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13, fill='white', width=0)
                self.text = self.canvas.create_text((self.x1+self.x2)/2, (self.y1+self.y2)/2, text=self.weight, font=('Arial', 18), fill='black', )
        else:
            if self.is_loop:
                pass
            else:
                self.line = self.canvas.create_line(*line_intersect_circle(self.x1, self.y1, self.x2, self.y2), fill=self.color, width=self.thickness)
                self.rect = self.canvas.create_rectangle((self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13, (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13, fill='white', width=0)
                self.text = self.canvas.create_text((self.x1+self.x2)/2, (self.y1+self.y2)/2, text=self.weight, font=('Arial', 18), fill='black')
        



    def change_weight(self, weight):
        self.weight = weight
        self.canvas.itemconfig(self.text, text=self.weight)
    
    def change_color(self, color):
        self.color = color
        self.canvas.itemconfig(self.line, fill=self.color)
            
    
    def move(self):
        self.x1, self.y1 = self.vertex1.x, self.vertex1.y
        self.x2, self.y2 = self.vertex2.x, self.vertex2.y
        self.canvas.coords(self.line, line_intersect_circle(self.x1, self.y1, self.x2, self.y2))
        self.canvas.coords(self.rect, (self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13, (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13)
        self.canvas.coords(self.text, (self.x1+self.x2)/2, (self.y1+self.y2)/2)

    def show_properties(self, event):
        props_edge = CTkToplevel()
        props_edge.wm_attributes('-topmost', '1')
        props_edge.title(f'Edge properties')
        props_edge.geometry(f'300x300+{event.x+250}+{event.y}')

        name_entry = CTkEntry(props_edge, text='Введите вес', justify='center')
        name_entry.insert(0, str(self.weight))
        name_entry.place(anchor='n', relx=0.5, rely=0.1)
        name_entry.bind('<Return>', lambda event: self.change_weight(int(name_entry.get())))

        clrbtn_1 = CTkButton(props_edge, corner_radius=0, fg_color='red', text='', command=lambda: self.change_color('red'))
        clrbtn_2 = CTkButton(props_edge, corner_radius=0, fg_color='purple', text='', command=lambda: self.change_color('purple'))
        clrbtn_3 = CTkButton(props_edge, corner_radius=0, fg_color='blue', text='', command=lambda: self.change_color('blue'))
        clrbtn_4 = CTkButton(props_edge, corner_radius=0, fg_color='green', text='', command=lambda: self.change_color('green'))
        clrbtn_5 = CTkButton(props_edge, corner_radius=0, fg_color='yellow', text='', command=lambda: self.change_color('yellow'))
        clrbtn_6 = CTkButton(props_edge, corner_radius=0, fg_color='orange', text='', command=lambda: self.change_color('orange'))
        clrbtn_7 = CTkButton(props_edge, corner_radius=0, fg_color='brown', text='', command=lambda: self.change_color('brown'))
        clrbtn_8 = CTkButton(props_edge, corner_radius=0, fg_color='black', text='', command=lambda: self.change_color('black'))
        clrbtn_9 = CTkButton(props_edge, corner_radius=0, fg_color='#FF00FF', text='', command=lambda: self.change_color('#FF00FF'))
        clrbtn_10= CTkButton(props_edge, corner_radius=0, fg_color='#00FF00', text='', command=lambda: self.change_color('#00FF00'))

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

        props_edge.mainloop()
    


class Workspace:
    def __init__(self, name: str = 'Безымянный') -> None:
        self.name = name
        self.graph = Graph()
        self.vertexes = []
        self.edges = []
        self.id_vert = 0


        self.add_vert_btn = CTkButton(root, text='Добавить вершину', command=self.add_vertex_mode, bg_color=btns_color) # <====================================================
        self.add_edge_btn = CTkButton(root, text='Добавить ребро', command=self.add_edge, bg_color=btns_color) # <====================================================
        self.del_vert_btn = CTkButton(root, text='Удалить вершину', command=lambda: print('Удалить вершину'), bg_color=btns_color) # <====================================================
        self.del_edge_btn = CTkButton(root, text='Удалить ребро', command=lambda: print('Удалить ребро'), bg_color=btns_color) # <====================================================
        self.default_btn = CTkButton(root, text='По умолчанию', command=self.default_mode, bg_color=btns_color) # <====================================================

        

        self.is_tab_opened = True
        self.canvas = CTkCanvas(root, width=1445, height=875, bg='#D3D3D3')


        self.tab_btn = CTkButton(root, text=self.name[0:12], command=self.SHOW, bg_color=btns_color,
                                 fg_color='white')
        self.close_tab_btn = CTkButton(root, image=PhotoImage(file=path_to_img_close_tab), 
                                    text='', bg_color=btns_color, fg_color=close_tab_button, hover_color='darkred',
                                    command=self.DEL)
        self.tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*len(workspaces), width=110)
        self.close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*len(workspaces), width=30)

        
        self.canvas.bind('<Button-3>', self.show_properties)

        self.SHOW()

    def update_from_adj(self, adj: list) -> None:
        self.graph = Graph(adj)
        self.canvas.delete('all')
        self.vertexes.clear()
        self.edges.clear()
        self.id_vert = 0
        for i in range(len(adj)):
            self.add_vertex_from_adj(x=randint(0, 1445-vertex_radius), y=randint(0, 875-vertex_radius))
        for i in range(len(adj)):
            for j in range(len(adj)):
                if adj[i][j] != 0:
                    self.add_edge_from_matr(self.vertexes[i], self.vertexes[j], adj[i][j], adj[i][j] != adj[j][i])
                    if adj[i][j] == adj[j][i]:
                        adj[j][i] = 0

    def default_mode(self):
        self.canvas.bind('<Button-1>', None)
        self.canvas.bind('<B1-Motion>', self.move_vertex)

    def add_vertex_mode(self):
        self.canvas.bind('<Button-1>', self.add_vertex_click)
        self.canvas.bind('<B1-Motion>', None)
        self.add_vertex()


    def show_properties(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                vertex.show_properties(event)
                break
        else:
            for edge in self.edges:
                # проверить попадает ли курсор в линию
                if (edge.x2 - edge.x1)**2 + (edge.y2 - edge.y1)**2+20 >= (x - edge.x1)**2 + (y - edge.y1)**2 + (x - edge.x2)**2 + (y - edge.y2)**2:
                    edge.show_properties(event)
                    break

    
    def move_vertex(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2 * 2:
                vertex.move(x, y)
                
                for edge in self.edges:
                    if edge.vertex1 is vertex or edge.vertex2 is vertex:
                        edge.move()
                break

    def add_vertex_from_adj(self, x, y):
        self.vertexes.append(Vertex(self.canvas, self.id_vert, x, y, self.id_vert))
        self.id_vert += 1

    def add_vertex_click(self, event):
        x, y = event.x, event.y
        self.graph.add_vertex()
        self.vertexes.append(Vertex(self.canvas, name=self.id_vert, x=x, y=y, id_vert=self.id_vert))
        self.id_vert += 1
    
    def add_vertex_from_file(self, name: str, x: int, y: int, color: str):
        self.graph.add_vertex()
        self.vertexes.append(Vertex(self.canvas, name, x, y, self.id_vert, color))
        self.id_vert += 1

    def add_edge_from_matr(self, vertex1: Vertex, vertex2: Vertex, weight: int, is_oriented: bool=False):
        self.edges.append(Edge(self.canvas, weight, vertex1, vertex2, is_oriented))

    def add_edge(self):
        self.canvas.bind('<Button-1>', self.add_edge_click)

    def add_edge_click(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                self.edge_vertex1 = vertex
                break
        else:
            return
        self.canvas.bind('<Button-1>', self.add_edge_click2)
    
    def add_edge_click2(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                self.edge_vertex2 = vertex
                break
        else:
            return
        props = CTk()
        props.geometry('300x200')
        props.title('Свойства ребра')
            

        def create_edge(weight: int, is_oriented: bool):
            weight = entry.get()
            if weight.isdigit():
                weight = int(weight)

            if is_oriented:
                self.graph.add_orient_edge(self.edge_vertex1.id_vert, self.edge_vertex2.id_vert, weight)
            else:
                self.graph.add_unorient_edge(self.edge_vertex1.id_vert, self.edge_vertex2.id_vert, weight)
            self.edges.append(Edge(self.canvas, weight, self.edge_vertex1, self.edge_vertex2, is_oriented))
            props.destroy()


        weight = 1
        entry = CTkEntry(props, text='Введите вес', justify='center')
        entry.place(anchor='n', relx=0.5, rely=0.1)
        
        btn_or = CTkButton(props, text='Ориентированное', command=lambda: create_edge(weight, True))
        btn_unor = CTkButton(props, text='Неориентированное', command=lambda: create_edge(weight, False))
        btn_or.place(anchor='n', relx=0.5, rely=0.5)
        btn_unor.place(anchor='n', relx=0.5, rely=0.7)

        props.mainloop()

        self.canvas.bind('<Button-1>', self.add_edge_click)

    def add_edge_from_file(self, weight: int, vertex1: Vertex, vertex2: Vertex, is_oriented: bool, color: str):
        if is_oriented:
            self.graph.add_orient_edge(vertex1.id_vert, vertex2.id_vert, weight)
        else:
            self.graph.add_unorient_edge(vertex1.id_vert, vertex2.id_vert, weight)
        self.edges.append(Edge(self.canvas, weight, vertex1, vertex2, is_oriented, color))


    def recovery_from_dict(self, dict):
        self.name = dict['graph_name']
        self.tab_btn.configure(text=self.name)
        for vertex in range(len(dict['name'])):
            self.add_vertex_from_file(dict['name'][vertex], dict['coords'][vertex][0], dict['coords'][vertex][1], dict['color'][vertex])
        for edge in dict['edges']:
            for vertex in self.vertexes:
                if vertex.x == edge[0][0] and vertex.y == edge[0][1]:
                    vertex1 = vertex
                elif vertex.x == edge[1][0] and vertex.y == edge[1][1]:
                    vertex2 = vertex
            self.add_edge_from_file(edge[2], vertex1, vertex2, edge[3], edge[4])
        


    def save_graph(self):
        path = filedialog.asksaveasfilename(defaultextension='.graph', filetypes=(('Графы', '*.graph'), ('Все файлы', '*.')), initialdir=get_script_dir())
        if path:
            self.name = path.split('/')[-1].replace('.graph', '')
            self.tab_btn.configure(text=self.name)

            dict = {}
            dict['graph_name'] = self.name
            dict['name'] = []
            dict['coords'] = []
            dict['color'] = []
            dict['edges'] = []

            for vertex in self.vertexes:
                dict['name'].append(vertex.name)
                dict['coords'].append((vertex.x, vertex.y))
                dict['color'].append(vertex.color)
            for edge in self.edges:
                dict['edges'].append(((edge.x1,edge.y1), (edge.x2, edge.y2), edge.weight, edge.is_oriented, edge.color))

            with open(path, 'w') as file:
                file.write(json.dumps(dict))

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
        self.canvas.place(anchor='nw')

        self.tab_btn.configure(fg_color=selected_tab_clr)
        
        self.add_vert_btn.place(anchor='ne', relx=0.997, rely=0.01)
        self.add_edge_btn.place(anchor='ne', relx=0.997, rely=0.05)
        self.del_vert_btn.place(anchor='ne', relx=0.997, rely=0.09)
        self.del_edge_btn.place(anchor='ne', relx=0.997, rely=0.13)
        self.default_btn.place(anchor='ne', relx=0.997, rely=0.17)

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
    filemenu.add_command(label="Новый", command=add_new_tab) # <====================================================
    filemenu.add_command(label="Открыть", command=open_file) # <====================================================
    filemenu.add_command(label="Сохранить", command=save_file) # <====================================================
    filemenu.add_separator()
    filemenu.add_command(label="Экспорт в текст", command=lambda: print('Экспорт в текст')) # <====================================================
    filemenu.add_command(label="Импорт из текста", command=lambda: print('Импорт из текста')) # <====================================================

    algsmenu = Menu(mainmenu, tearoff=0)
    algsmenu.add_command(label="Кол-во вершин", command=vertexes_count) # <====================================================
    algsmenu.add_command(label="Кол-во вершин", command=edges_count) # <====================================================
    algsmenu.add_command(label="Степени вершин", command=edges_count) # <====================================================
    algsmenu.add_command(label="Матрица смежности", command=get_adj_matrix) # <====================================================
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
    return graph

def open_file():
    graph = add_new_tab()
    path = filedialog.askopenfilename(initialdir=get_script_dir(), filetypes=(('Графы', '*.graph'), ('Все файлы', '*.')), title='Открыть граф')
    if path:
        with open(path, 'r') as file:
            dict = json.load(file)
        graph.recovery_from_dict(dict)

def save_file():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.save_graph()


def vertexes_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            print( len(workspace.vertexes))

def edges_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            print(len(workspace.edges))

def get_adj_matrix():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            matrix = workspace.graph.get_adj_matrix()
            sring = ''
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    sring += str(matrix[i][j]) + ' '
                sring += '\n'
            win = CTk()
            win.title('Матрица смежности')
            win.geometry('300x300')
            win.resizable(False, False)
            text = Text(win, width=30, height=15)
            text.insert(1.0, sring[0:-1])
            text.place(anchor='center', relx=0.5, rely=0.5)


            # считать матрицу смежности и построить граф
            def read_matrix():
                matrix = []
                strings = text.get(1.0, END).split('\n')
                for i in range(len(strings)):
                    matrix.append(strings[i].split(' '))
                for i in matrix:
                    if i == ['']:
                        matrix.remove(i)
                    for j in i:
                        if j == '':
                            i.remove(j)
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        matrix[i][j] = int(matrix[i][j])
                win.destroy()
                workspace.update_from_adj(matrix) 

            CTkButton(win, text='Построить граф', bg_color=btns_color, fg_color=add_tab_button,
                        corner_radius=5, command=read_matrix).place(anchor='center', relx=0.5, rely=0.9)
            


            win.mainloop()


workspaces = []
def ex(event):
    global root
    root.destroy()

main()
