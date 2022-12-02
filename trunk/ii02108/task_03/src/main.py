from customtkinter import *
from tkinter import Menu, PhotoImage, filedialog, Text
from main_components import *
from graphs import Graph, inc_to_adj
from random import randint

import json
import pyperclip

class Workspace:
    def __init__(self, name: str = 'Безымянный') -> None:
        self.name = name
        self.graph = Graph()
        self.vertexes = []
        self.edges = []
        self.selected_vertexes = []
        self.id_vert = 0


        self.add_vert_btn = CTkButton(root, text='Добавить вершину', command=self.add_vertex_mode, bg_color=btns_color) # <====================================================
        self.add_edge_btn = CTkButton(root, text='Добавить ребро', command=self.add_edge, bg_color=btns_color) # <====================================================
        self.del_comp_btn = CTkButton(root, text='Удалить компонент', command=self.delete_comp, bg_color=btns_color) # <====================================================
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
        self.default_mode()
    
    def __del__(self):
        del self.graph
        del self.edges
        del self.vertexes
        del self.selected_vertexes
        self.DEL()


    def update_from_adj(self, adj: list) -> None:
        self.graph = Graph(adj)
        self.canvas.delete('all')
        self.vertexes.clear()
        self.edges.clear()
        self.id_vert = 0
        for i in range(len(adj)):
            self.vertexes.append(Vertex(self.canvas, self.id_vert, randint(0, 1445-vertex_radius), randint(0, 875-vertex_radius), self.id_vert))
            self.id_vert += 1
        for i in range(len(adj)):
            for j in range(len(adj)):
                if adj[i][j] != 0:
                    self.edges.append(Edge(self.canvas, adj[i][j], self.vertexes[i], self.vertexes[j], adj[i][j] != adj[j][i]))
                    if adj[i][j] == adj[j][i]:
                        adj[j][i] = 0

    def default_mode(self):
        self.canvas.bind('<Button-1>', lambda event: None)
        self.canvas.bind('<B1-Motion>', self.move_vertex)
        self.canvas.bind('<Control-Button-1>', self.select_vertex)

    def add_vertex_mode(self):
        self.canvas.bind('<Button-1>', self.add_vertex_click)
        self.canvas.bind('<B1-Motion>', lambda event: None)

    def select_vertex(self, event):
        for vertex in self.vertexes:
            if (vertex.x - event.x)**2 + (vertex.y - event.y)**2 <= vertex.radius**2:
                if vertex not in self.selected_vertexes:
                    self.selected_vertexes.append(vertex)
                    vertex.select()
                else:
                    self.selected_vertexes.remove(vertex)
                    vertex.unselect()
                break

    def show_properties(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                vertex.show_properties(event)
                break
        else:
            for edge in self.edges:
                if sqrt((x - edge.x1)**2 + (y - edge.y1)**2) + sqrt((x - edge.x2)**2 + (y - edge.y2)**2) <= sqrt((edge.x2 - edge.x1)**2 + (edge.y2 - edge.y1)**2)+5:
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

    def add_vertex_click(self, event):
        x, y = event.x, event.y
        self.graph.add_vertex()
        self.vertexes.append(Vertex(self.canvas, name=self.id_vert, x=x, y=y, id_vert=self.id_vert))
        self.id_vert += 1

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
        props.geometry(f'300x200+{event.x_root}+{event.y_root}')
        props.title('Свойства ребра')
        props.resizable(False, False)
        props.bind('<Escape>', lambda event: props.destroy())
            

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

    def delete_selected_vertexes(self):
        for vertex in self.selected_vertexes:
            for _ in range(len(self.vertexes)):
                for edge in self.edges:
                    if vertex in (edge.vertex1, edge.vertex2):
                        vertex1 = edge.vertex1.id_vert
                        vertex2 = edge.vertex2.id_vert
                        self.edges.remove(edge)
                        self.graph.del_edge(vertex1, vertex2)
                        edge.delete()
            self.vertexes.remove(vertex)
            for vert in self.vertexes:
                if vert.id_vert > vertex.id_vert:  
                    vert.id_vert -= 1
                    self.id_vert -= 1
            self.graph.del_vertex(vertex.id_vert)
            vertex.delete()
        self.selected_vertexes.clear()

    def delete_comp(self):
        self.canvas.bind('<Button-1>', self.delete_comp_click)
        self.canvas.bind('<B1-Motion>', self.delete_comp_click)
    
    def delete_comp_click(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                vertex.delete()
                for _ in range(len(self.vertexes)):
                    for edge in self.edges:
                        if vertex in (edge.vertex1, edge.vertex2):
                            vertex1 = edge.vertex1.id_vert
                            vertex2 = edge.vertex2.id_vert
                            edge.delete()
                            self.edges.remove(edge)
                            self.graph.del_edge(vertex1, vertex2)
                self.vertexes.remove(vertex)
                for vert in self.vertexes:
                    if vert.id_vert > vertex.id_vert:  
                        vert.id_vert -= 1
                        self.id_vert -= 1
                self.graph.del_vertex(vertex.id_vert)
                break
        else:
            for edge in self.edges:
                if sqrt((x - edge.x1)**2 + (y - edge.y1)**2) + sqrt((x - edge.x2)**2 + (y - edge.y2)**2) <= sqrt((edge.x2 - edge.x1)**2 + (edge.y2 - edge.y1)**2)+5:
                    self.graph.del_edge(edge.vertex1.id_vert, edge.vertex2.id_vert)
                    edge.delete()
                    self.edges.remove(edge)
                    break

        
    def copy_to_clipboard(self):
        dict = {}
        dict['vertexes'] = []
        dict['edges'] = []

        for i, vertex1 in enumerate(self.selected_vertexes):
            dict['vertexes'].append((vertex1.name, vertex1.x, vertex1.y, vertex1.color))
            for j, vertex2 in enumerate(self.selected_vertexes):
                if vertex1 != vertex2:
                    for edge in self.edges:
                        if edge.vertex1 == vertex1 and edge.vertex2 == vertex2 or edge.vertex1 == vertex2 and edge.vertex2 == vertex1:
                            dict['edges'].append((i, j, edge.weight, edge.is_oriented, edge.color)) # i, j - индексы вершин в списке dict['vertexes']
                            break
        pyperclip.copy(json.dumps(dict))

    def paste_from_clipboard(self):
        dict = json.loads(pyperclip.paste())
        length = len(dict['vertexes'])
        for vertex in dict['vertexes']:
            self.vertexes.append(Vertex(self.canvas, vertex[0], vertex[1], vertex[2], self.id_vert, vertex[3]))
            self.graph.add_vertex()
            self.id_vert += 1
        for edge in dict['edges']:

            self.edges.append(Edge(self.canvas, edge[2], self.vertexes[-length + edge[0]], self.vertexes[-length + edge[1]], edge[3], edge[4]))
            if edge[3]:
                self.graph.add_orient_edge(self.edges[-1].vertex1.id_vert, self.edges[-1].vertex2.id_vert, edge[2])
            else:
                self.graph.add_unorient_edge(self.edges[-1].vertex1.id_vert, self.edges[-1].vertex2.id_vert, edge[2])


    def recovery_from_dict(self, dict):
        self.name = dict['graph_name']
        self.tab_btn.configure(text=self.name)
        self.id_vert = 0
        self.graph = Graph()
        for vertex in range(len(dict['name'])):
            self.graph.add_vertex()
            self.vertexes.append(Vertex(self.canvas, dict['name'][vertex], dict['coords'][vertex][0], dict['coords'][vertex][1], self.id_vert, dict['color'][vertex]))
            self.id_vert += 1
        for edge in dict['edges']:
            for vertex in self.vertexes:
                if vertex.x == edge[0][0] and vertex.y == edge[0][1]:
                    vertex1 = vertex
                elif vertex.x == edge[1][0] and vertex.y == edge[1][1]:
                    vertex2 = vertex
            
            if edge[3]:
                self.graph.add_orient_edge(vertex1.id_vert, vertex2.id_vert, edge[2])
            else:
                self.graph.add_unorient_edge(vertex1.id_vert, vertex2.id_vert, edge[2])
            self.edges.append(Edge(self.canvas, edge[2], vertex1, vertex2, edge[3], edge[4]))
        


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
                file.write(json.dumps(dict, indent=4))

    def export_to_text(self):
        pass

    def import_from_text(self):
        pass

    def vertexes_degree(self):
        degrees = []
        for vertex in self.vertexes:
            pass

    def HIDE(self):
        self.canvas.place_forget()
        self.tab_btn.configure(fg_color=default_btn_clr)

        self.add_vert_btn.place_forget()
        self.add_edge_btn.place_forget()
        self.del_comp_btn.place_forget()
        self.default_btn.place_forget()

    def SHOW(self):
        for workspace in workspaces:
            workspace.HIDE()
        self.canvas.place(anchor='nw')

        self.tab_btn.configure(fg_color=selected_tab_clr)
        
        self.add_vert_btn.place(anchor='ne', relx=0.997, rely=0.01)
        self.add_edge_btn.place(anchor='ne', relx=0.997, rely=0.05)
        self.del_comp_btn.place(anchor='ne', relx=0.997, rely=0.09)
        self.default_btn.place(anchor='ne', relx=0.997, rely=0.13)

    def DEL(self):
        try:
            self.canvas.destroy()
            self.tab_btn.destroy()
            self.close_tab_btn.destroy()
        except:
            pass
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
    root.geometry("1600x900+150+70")
    root.resizable(False, False)
    root.set_appearance_mode(main_theme)

    root.bind('<Delete>', delete_selected_vertexes)
    root.bind('<Control-c>', copy_selected_vertexes)
    root.bind('<Control-v>', paste_selected_vertexes)

    # Раздел меню
    mainmenu = Menu(root)
    root.config(menu=mainmenu)

    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Новый", command=add_new_tab)
    filemenu.add_command(label="Открыть", command=open_file)
    filemenu.add_command(label="Сохранить", command=save_file)
    filemenu.add_separator()
    filemenu.add_command(label="Экспорт в текст", command=lambda: print('Экспорт в текст')) # <====================================================
    filemenu.add_command(label="Импорт из текста", command=lambda: print('Импорт из текста')) # <====================================================

    algsmenu = Menu(mainmenu, tearoff=0)
    algsmenu.add_command(label="Кол-во вершин", command=vertexes_count) # <====================================================
    algsmenu.add_command(label="Кол-во ребер", command=edges_count) # <====================================================
    algsmenu.add_command(label="Степени вершин", command=vertexes_degree) # <====================================================
    algsmenu.add_command(label="Матрица смежности", command=get_adj_matrix) # <====================================================
    algsmenu.add_command(label="Матрица инцидентности", command=get_inc_matrix) # <====================================================
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


def activate_func(func):
    for workspace in workspaces:
        if workspace.is_tab_opened:
            exec(f'workspace.{func}()')

def save_file():
    activate_func('save_graph')

def delete_selected_vertexes(event):
    activate_func('delete_selected_vertexes')

def copy_selected_vertexes(event):
    activate_func('copy_to_clipboard')

def paste_selected_vertexes(event):
    activate_func('paste_from_clipboard')

def vertexes_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            print(len(workspace.vertexes), workspace.graph.vertexes_count)

def edges_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            print(len(workspace.edges), workspace.graph.edges_count)

def vertexes_degree():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.vertexes_degree()

def get_adj_matrix():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            string = workspace.graph.show_adj_matrix()

            win = CTk()
            win.title('Матрица смежности')
            win.geometry('500x500')
            win.bind('<Escape>', lambda event: win.destroy())

            text = Text(win)
            text.insert(1.0, string[0:-1])
            text.place(anchor='nw', relx=0, rely=0, relwidth=1, relheight=0.9)


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

def get_inc_matrix():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            sring = workspace.graph.show_inc_matrix()

            win = CTk()
            win.title('Матрица инцидентности')
            win.geometry('500x500')
            win.bind('<Escape>', lambda event: win.destroy())

            text = Text(win, width=30, height=15)
            text.insert(1.0, sring[0:-1])
            text.place(anchor='center', relx=0.5, rely=0.5)


            # считать матрицу инцидентности и построить граф
            def read_matrix():
                matrix = []
                string = text.get(1.0, END).replace(',', '')
                if string:
                    strings = string.split('\n')
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
                    adj_matrix = inc_to_adj(matrix)
                    workspace.update_from_adj(adj_matrix) 

            CTkButton(win, text='Построить граф', bg_color=btns_color, fg_color=add_tab_button,
                        corner_radius=5, command=read_matrix).place(anchor='center', relx=0.5, rely=0.9)

            win.mainloop()



workspaces = []
def ex(event):
    global root
    workspaces.clear()
    root.destroy()

main()
