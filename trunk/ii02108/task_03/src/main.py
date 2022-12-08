from tkinter import Menu, PhotoImage, filedialog, Text, messagebox, Label, END
from main_components import Vertex, Edge
from graphs import Graph, inc_to_adj
from config import main_theme, btns_color, add_tab_button, close_tab_button, unselected_btn_clr, selected_tab_clr
from config import unactive_mode_btn, active_mode_btn, path_to_img_create_new_tab, path_to_img_close_tab, vertex_radius, get_script_dir
from numpy.random import randint
from numpy import sqrt as sq
from _tkinter import TclError

import customtkinter as ctk
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

        self.edge_vertexes = []


        self.add_vert_btn = ctk.CTkButton(root, text='Добавить вершину', command=self.add_vertex_mode, bg_color=btns_color)
        self.add_edge_btn = ctk.CTkButton(root, text='Добавить ребро', command=self.add_edge_mode, bg_color=btns_color)
        self.del_comp_btn = ctk.CTkButton(root, text='Удалить компонент', command=self.delete_comp_mode, bg_color=btns_color)
        self.default_btn = ctk.CTkButton(root, text='По умолчанию', command=self.default_mode, bg_color=btns_color)


        self.is_tab_opened = True
        self.canvas = ctk.CTkCanvas(root, width=1445, height=875, bg='#D3D3D3')


        self.tab_btn = ctk.CTkButton(root, text=self.name[0:12], command=self.SHOW, bg_color=btns_color,
                                 fg_color='white')
        self.close_tab_btn = ctk.CTkButton(root, image=PhotoImage(file=path_to_img_close_tab),
                                    text='', bg_color=btns_color, fg_color=close_tab_button, hover_color='darkred',
                                    command=self.DEL)
        self.tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*len(workspaces), width=110)
        self.close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*len(workspaces), width=30)


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
        for i, _ in enumerate(adj):
            # self.graph
            self.vertexes.append(Vertex(self.canvas, self.id_vert, randint(0, 1445-vertex_radius), randint(0, 875-vertex_radius), self.id_vert))
            self.id_vert += 1
        for i, _ in enumerate(adj):
            for j, _ in enumerate(adj):
                if adj[i][j] != 0:
                    self.edges.append(Edge(self.canvas, adj[i][j], self.vertexes[i], self.vertexes[j], adj[i][j] != adj[j][i]))
                    if adj[i][j] == adj[j][i]:
                        adj[j][i] = 0

    def add_vertex_mode(self):
        self.add_vert_btn.configure(fg_color=active_mode_btn)
        self.add_edge_btn.configure(fg_color=unactive_mode_btn)
        self.del_comp_btn.configure(fg_color=unactive_mode_btn)
        self.default_btn.configure(fg_color=unactive_mode_btn)

        for vertex in self.vertexes:
            vertex.unselect()
        self.selected_vertexes.clear()

        self.canvas.bind('<Button-1>', self.add_vertex_click)
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<Button-3>', self.show_properties)

    def add_edge_mode(self):
        self.add_vert_btn.configure(fg_color=unactive_mode_btn)
        self.add_edge_btn.configure(fg_color=active_mode_btn)
        self.del_comp_btn.configure(fg_color=unactive_mode_btn)
        self.default_btn.configure(fg_color=unactive_mode_btn)

        for vertex in self.vertexes:
            vertex.unselect()
        self.edge_vertexes.clear()
        self.selected_vertexes.clear()

        self.canvas.bind('<Button-1>', self.add_edge_click)
        self.canvas.bind('<Button-3>', self.del_vert_from_edge)

    def delete_comp_mode(self):
        self.add_vert_btn.configure(fg_color=unactive_mode_btn)
        self.add_edge_btn.configure(fg_color=unactive_mode_btn)
        self.del_comp_btn.configure(fg_color=active_mode_btn)
        self.default_btn.configure(fg_color=unactive_mode_btn)

        for vertex in self.vertexes:
            vertex.unselect()
        self.selected_vertexes.clear()

        self.canvas.bind('<Button-1>', self.delete_comp_click)
        self.canvas.bind('<B1-Motion>', self.delete_comp_click)
        self.canvas.bind('<Button-3>', self.show_properties)

    def default_mode(self):
        self.add_vert_btn.configure(fg_color=unactive_mode_btn)
        self.add_edge_btn.configure(fg_color=unactive_mode_btn)
        self.del_comp_btn.configure(fg_color=unactive_mode_btn)
        self.default_btn.configure(fg_color=active_mode_btn)

        for vertex in self.vertexes:
            vertex.unselect()
        self.selected_vertexes.clear()

        self.canvas.bind('<Button-1>', lambda event: None)
        self.canvas.bind('<B1-Motion>', self.move_vertex)
        self.canvas.bind('<Control-Button-1>', self.select_vertex)
        self.canvas.bind('<Button-3>', self.show_properties)

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
                if sq((x - edge.x1)**2 + (y - edge.y1)**2) + sq((x - edge.x2)**2 + (y - edge.y2)**2) <= sq((edge.x2 - edge.x1)**2 + (edge.y2 - edge.y1)**2)+5:
                    edge.show_properties(event, self.graph)
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

    def add_edge_click(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                self.edge_vertexes.append(vertex)
                vertex.select()
                break
        if len(self.edge_vertexes) == 2:
            props = ctk.CTk()
            props.geometry(f'300x200+{event.x_root}+{event.y_root}')
            props.title('Свойства ребра')
            props.resizable(False, False)
            props.bind('<Escape>', lambda event: props.destroy())


            def create_edge(is_oriented: bool):
                try:
                    weight = int(entry.get())
                except ValueError:
                    messagebox.showerror('Ошибка', 'Вес должен быть целым числом')
                else:
                    if is_oriented:
                        self.graph.add_orient_edge(self.edge_vertexes[0].id_vert, self.edge_vertexes[1].id_vert, weight)
                    else:
                        self.graph.add_unorient_edge(self.edge_vertexes[0].id_vert, self.edge_vertexes[1].id_vert, weight)
                    self.edges.append(Edge(self.canvas, weight, self.edge_vertexes[0], self.edge_vertexes[1], is_oriented))
                    props.destroy()
                    self.del_vert_from_edge(None)


            entry = ctk.CTkEntry(props, text='Введите вес', justify='center')
            entry.place(anchor='n', relx=0.5, rely=0.1)
            entry.focus()

            btn_or = ctk.CTkButton(props, text='Ориентированное', command=lambda: create_edge(True))
            btn_unor = ctk.CTkButton(props, text='Неориентированное', command=lambda: create_edge(False))
            btn_or.place(anchor='n', relx=0.5, rely=0.5)
            btn_unor.place(anchor='n', relx=0.5, rely=0.7)

            props.mainloop()

    def del_vert_from_edge(self, event):
        if event is None:
            for vertex in self.edge_vertexes:
                vertex.unselect()
            self.edge_vertexes.clear()
        else:
            for vertex in self.edge_vertexes:
                if (vertex.x - event.x)**2 + (vertex.y - event.y)**2 <= vertex.radius**2:
                    self.edge_vertexes.remove(vertex)
                    vertex.unselect()
                    break

    def delete_selected_vertexes(self):
        for vertex in self.selected_vertexes:
            for _ in self.vertexes:
                for edge in self.edges:
                    if vertex in (edge.vertex1, edge.vertex2):
                        vertex1 = edge.vertex1.id_vert
                        vertex2 = edge.vertex2.id_vert
                        self.edges.remove(edge)
                        self.graph.del_edge(vertex1, vertex2)
                        edge.delete()
            self.vertexes.remove(vertex)
            self.id_vert -= 1
            for vert in self.vertexes:
                if vert.id_vert > vertex.id_vert:
                    vert.id_vert -= 1
            self.graph.del_vertex(vertex.id_vert)
            vertex.delete()
        self.selected_vertexes.clear()

    def delete_comp_click(self, event):
        x, y = event.x, event.y
        for vertex in self.vertexes:
            if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                vertex.delete()
                for _ in self.vertexes:
                    for edge in self.edges:
                        if vertex in (edge.vertex1, edge.vertex2):
                            vertex1 = edge.vertex1.id_vert
                            vertex2 = edge.vertex2.id_vert
                            edge.delete()
                            self.edges.remove(edge)
                            self.graph.del_edge(vertex1, vertex2)
                self.vertexes.remove(vertex)
                self.id_vert -= 1
                for vert in self.vertexes:
                    if vert.id_vert > vertex.id_vert:
                        vert.id_vert -= 1
                self.graph.del_vertex(vertex.id_vert)
                break
        else:
            for edge in self.edges:
                if sq((x - edge.x1)**2 + (y - edge.y1)**2) + sq((x - edge.x2)**2 + (y - edge.y2)**2) <= sq((edge.x2 - edge.x1)**2 + (edge.y2 - edge.y1)**2)+5:
                    self.graph.del_edge(edge.vertex1.id_vert, edge.vertex2.id_vert)
                    edge.delete()
                    self.edges.remove(edge)
                    break


    def cut_to_clipboard(self):
        self.copy_to_clipboard()
        self.delete_selected_vertexes()

    def copy_to_clipboard(self):
        dictionary = dict()
        dictionary['vertexes'] = []
        dictionary['edges'] = []

        for i, vertex1 in enumerate(self.selected_vertexes):
            dictionary['vertexes'].append((vertex1.name, vertex1.x, vertex1.y, vertex1.color))
            for j, vertex2 in enumerate(self.selected_vertexes):
                if vertex1 != vertex2:
                    for edge in self.edges:
                        if edge.vertex1 == vertex1 and edge.vertex2 == vertex2:
                            dictionary['edges'].append((i, j, edge.weight, edge.is_oriented, edge.color)) # i, j - индексы вершин в списке dict['vertexes']
                            break
        copy = json.dumps(dictionary)
        pyperclip.copy(copy)

    def paste_from_clipboard(self):
        try:
            paste = pyperclip.paste()
            dictionary = json.loads(paste)
        except json.decoder.JSONDecodeError:
            messagebox.showerror('Ошибка', 'В буфере обмена нет данных')
        else:
            if not ('vertexes' in dictionary and 'edges' in dictionary):
                messagebox.showerror('Ошибка', 'В буфере обмена нет данных')
            else:
                length = len(dictionary['vertexes'])
                for vertex in dictionary['vertexes']:
                    self.vertexes.append(Vertex(self.canvas, vertex[0], vertex[1], vertex[2], self.id_vert, vertex[3]))
                    self.graph.add_vertex()
                    self.id_vert += 1
                for edge in dictionary['edges']:

                    self.edges.append(Edge(self.canvas, edge[2], self.vertexes[-length + edge[0]], self.vertexes[-length + edge[1]], edge[3], edge[4]))
                    if edge[3]:
                        self.graph.add_orient_edge(self.edges[-1].vertex1.id_vert, self.edges[-1].vertex2.id_vert, edge[2])
                    else:
                        self.graph.add_unorient_edge(self.edges[-1].vertex1.id_vert, self.edges[-1].vertex2.id_vert, edge[2])


    def recovery_from_dict(self, dictionary: dict):
        self.name = dictionary['graph_name']
        self.tab_btn.configure(text=self.name)
        self.id_vert = 0
        self.graph = Graph()
        for vertex in range(len(dictionary['name'])):
            self.graph.add_vertex()
            self.vertexes.append(Vertex(self.canvas, dictionary['name'][vertex], dictionary['coords'][vertex][0],
                                dictionary['coords'][vertex][1], self.id_vert, dictionary['color'][vertex]))
            self.id_vert += 1
        for edge in dictionary['edges']:
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

            dictionary = dict()
            dictionary['graph_name'] = self.name
            dictionary['name'] = []
            dictionary['coords'] = []
            dictionary['color'] = []
            dictionary['edges'] = []

            for vertex in self.vertexes:
                dictionary['name'].append(vertex.name)
                dictionary['coords'].append((vertex.x, vertex.y))
                dictionary['color'].append(vertex.color)
            for edge in self.edges:
                dictionary['edges'].append(((edge.x1,edge.y1), (edge.x2, edge.y2), edge.weight, edge.is_oriented, edge.color))

            with open(path, 'w') as file:
                file.write(json.dumps(dictionary))

    def export_to_text(self):
        path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=(('Текстовые файлы', '*.txt'),
                                           ('Все файлы', '*.')), initialdir=get_script_dir())
        if path:
            string = self.name + '\n'
            for edge in self.edges:
                if edge.is_oriented:
                    string += 'ORIENT; '
                    is_orient = True
                    break
            else:
                string += 'UNORIENT\n'
                is_orient = False

            string += ''.join([str(i+1)+', ' for i in range(self.id_vert)])[:-2] + '\n'

            matrix = [i.copy() for i in self.graph.get_adj_matrix()]

            if is_orient:
                for i, _ in enumerate(matrix):
                    for j, _ in enumerate(matrix):
                        if matrix[i][j] != 0:
                            string += f'{i+1} -> {j+1} {matrix[i][j]}\n'
            else:
                for i, _ in enumerate(matrix):
                    for j, _ in enumerate(matrix):
                        if matrix[i][j] != 0:
                            string += f'{i+1} -- {j+1} {matrix[i][j]}\n'
                            matrix[j][i] = 0

            with open(path, 'w') as file:
                file.write(string)

    def import_from_text(self, text: str):
        strings = text.split('\n')
        self.name = strings[0]
        self.tab_btn.configure(text=self.name)

        length = int(strings[2].split(', ')[-1])
        matrix = [[0 for i in range(length)] for _ in range(length)]

        if strings[1] == 'ORIENT':
            for edge in strings[3:]:
                if edge:
                    string = edge.split(' ')
                    matrix[int(string[0])-1][int(string[2])-1] = int(string[3])
        else:
            for edge in strings[3:]:
                if edge:
                    string = edge.split(' ')
                    matrix[int(string[0])-1][int(string[2])-1] = int(string[3])
                    matrix[int(string[2])-1][int(string[0])-1] = int(string[3])
        self.update_from_adj(matrix)


    def vertexes_degree(self):
        degrees = {vertex.name : self.graph.get_degree(vertex.id_vert) for vertex in self.vertexes}
        show_info('Степени вершин', degrees)

    def find_shortest_path(self):
        self.selected_vertexes.clear()

        def get_vertex(event):
            x = event.x
            y = event.y
            for vertex in self.vertexes:
                vertex.unselect()
                if (vertex.x - x)**2 + (vertex.y - y)**2 <= vertex.radius**2:
                    vertex.select()
                    self.selected_vertexes.append(vertex)
            if len(self.selected_vertexes) == 2:
                path = self.graph.get_shortest_path(self.selected_vertexes[0].id_vert, self.selected_vertexes[1].id_vert)
                output = ['' for _ in path]
                for i, vertex in enumerate(path):
                    output[i] = self.vertexes[vertex].name
                if path is not None:
                    show_info('Кратчайший путь', output)
                else:
                    show_info('Кратчайший путь', 'Путь не найден')
                self.default_mode()
        self.canvas.bind('<Button-1>', get_vertex)

    def find_center(self):
        center = self.graph.get_center()
        if center:
            show_info('Центр графа', center)
        else:
            show_info('Центр графа', 'Центр не найден')

    def find_radius(self):
        radius = self.graph.get_radius()
        if radius != float('inf'):
            show_info('Радиус графа', radius)
        else:
            show_info('Радиус графа', 'Радиус не найден')

    def find_diameter(self):
        diameter = self.graph.get_diameter()
        if diameter != 0:
            show_info('Радиус графа', diameter)
        else:
            show_info('Радиус графа', 'Диаметр не найден')

    def eulerian_path(self):
        path = self.graph.get_eulerian_cycle()
        if path:
            output = ['' for _ in path]
            for i, vertex in enumerate(path):
                output[i] = self.vertexes[vertex].name
            show_info('Эйлеров путь', output)
        else:
            show_info('Эйлеров путь', 'Путь не найден')

    def hamiltonian_path(self):
        path = self.graph.get_hamiltonian_cycle()
        if path:
            output = ['' for _ in path]
            for i, vertex in enumerate(path):
                output[i] = self.vertexes[vertex].name
            show_info('Гамильтонов путь', output)
        else:
            show_info('Гамильтонов путь', 'Путь не найден')


    def HIDE(self):
        self.is_tab_opened = False
        self.canvas.place_forget()
        self.tab_btn.configure(fg_color=unselected_btn_clr)

        self.add_vert_btn.place_forget()
        self.add_edge_btn.place_forget()
        self.del_comp_btn.place_forget()
        self.default_btn.place_forget()

    def SHOW(self):
        for workspace in workspaces:
            workspace.HIDE()
        self.is_tab_opened = True
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
        except TclError:
            pass
        workspaces.remove(self)

        for i, _ in enumerate(workspaces):
            try:
                workspaces[i].tab_btn.place(anchor='w', relx = 0.9097, rely=0.34+0.04*i, width=110)
                workspaces[i].close_tab_btn.place(anchor='e', relx = 0.998, rely=0.34+0.04*i, width=30)
            except TclError:
                pass


def add_new_tab():
    global workspaces
    for workspace in workspaces:
        workspace.is_tab_opened = False
        workspace.tab_btn.configure(fg_color=unselected_btn_clr)
    graph = Workspace()
    workspaces.append(graph)
    return graph

def open_file():
    graph = add_new_tab()
    path = filedialog.askopenfilename(initialdir=get_script_dir(), filetypes=(('Графы', '*.graph'), ('Все файлы', '*.')), title='Открыть граф')
    if path:
        with open(path, 'r') as file:
            dictionary = json.load(file)
        graph.recovery_from_dict(dictionary)

def save_file():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.save_graph()

def export_to_text():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.export_to_text()

def import_from_text():
    graph = add_new_tab()
    path = filedialog.askopenfilename(initialdir=get_script_dir(), filetypes=(('Текстовые файлы', '*.txt'), ('Все файлы', '*.')), title='Открыть граф')
    if path:
        with open(path, 'r') as file:
            text = file.read()
        graph.import_from_text(text)

def delete_selected_vertexes(event):
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.delete_selected_vertexes()

def cut_selected_vertexes(event):
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.cut_to_clipboard()

def copy_selected_vertexes(event):
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.copy_to_clipboard()

def paste_selected_vertexes(event):
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.paste_from_clipboard()

def vertexes_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            show_info('Количество вершин', str(len(workspace.vertexes)))

def edges_count():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            show_info('Количество ребер', str(len(workspace.edges)))

def vertexes_degree():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.vertexes_degree()

def is_tree():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            if workspace.graph.is_tree():
                show_info('Дерево', 'Да')
            else:
                show_info('Дерево', 'Нет')

def is_connected():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            if workspace.graph.is_connected():
                show_info('Связность', 'Да')
            else:
                show_info('Связность', 'Нет')

def is_full():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            if workspace.graph.is_full():
                show_info('Полнота', 'Да')
            else:
                show_info('Полнота', 'Нет')

def is_eulerian():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            if workspace.graph.is_eulerian():
                show_info('Эйлеровость', 'Да')
            else:
                show_info('Эйлеровость', 'Нет')

def is_hamiltonian():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            if workspace.graph.is_hamiltonian():
                show_info('Гамильтоновость', 'Да')
            else:
                show_info('Гамильтоновость', 'Нет')


def find_shortest_path():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.find_shortest_path()

def find_center():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.find_center()

def find_radius():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.find_radius()

def find_diameter():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.find_diameter()

def eulerian_path():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.eulerian_path()

def hamiltonian_path():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            workspace.hamiltonian_path()

def get_adj_matrix():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            string = workspace.graph.show_adj_matrix()

            win = ctk.CTk()
            win.title('Матрица смежности')
            win.geometry('500x500')
            win.bind('<Escape>', lambda event: win.destroy())

            text = Text(win)
            text.insert(1.0, string[0:-1])
            text.place(anchor='nw', relx=0, rely=0, relwidth=1, relheight=0.9)
            text.focus()


            def read_matrix():
                matrix = []
                strings = text.get(1.0, END).split('\n')
                for i, _ in enumerate(strings):
                    matrix.append(strings[i].split(' '))
                for i in matrix:
                    if i == ['']:
                        matrix.remove(i)
                    for j in i:
                        if j == '':
                            i.remove(j)
                for i, _ in enumerate(matrix):
                    for j, _ in enumerate(matrix[i]):
                        matrix[i][j] = int(matrix[i][j])
                win.destroy()
                workspace.update_from_adj(matrix)

            ctk.CTkButton(win, text='Построить граф', command=read_matrix).place(anchor='center', relx=0.5, rely=0.95)

            win.mainloop()

def get_inc_matrix():
    for workspace in workspaces:
        if workspace.is_tab_opened:
            sring = workspace.graph.show_inc_matrix()

            win = ctk.CTk()
            win.title('Матрица инцидентности')
            win.geometry('500x500')
            win.bind('<Escape>', lambda event: win.destroy())

            text = Text(win, width=30, height=15)
            text.insert(1.0, sring[0:-1])
            text.place(anchor='nw', relx=0, rely=0, relwidth=1, relheight=0.9)
            text.focus()


            def read_matrix():
                matrix = []
                string = text.get(1.0, END).replace(',', '')
                if string:
                    strings = string.split('\n')
                    for i, _ in enumerate(strings):
                        matrix.append(strings[i].split(' '))
                    for i in matrix:
                        if i == ['']:
                            matrix.remove(i)
                        for j in i:
                            if j == '':
                                i.remove(j)

                    for i, _ in enumerate(matrix):
                        for j, _ in enumerate(matrix[i]):
                            matrix[i][j] = int(matrix[i][j])
                    win.destroy()
                    adj_matrix = inc_to_adj(matrix)
                    workspace.update_from_adj(adj_matrix)

            ctk.CTkButton(win, text='Построить граф', command=read_matrix).place(anchor='center', relx=0.5, rely=0.95)

            win.mainloop()

def show_info(title: str, info: any):
    info = str(info)

    win = ctk.CTk()
    win.title(title)
    win.geometry('500x500')
    win.bind('<Escape>', lambda event: win.destroy())

    for i in range(0, len(info), 32):
        Label(win, font='Consolas 20', text=info[i:i+32]).pack()


    win.mainloop()

def close_program(event):
    workspaces.clear()
    root.destroy()


workspaces = []

root = ctk.CTk()
root.title('Graph Editor')
root.geometry("1600x900+150+70")
root.resizable(False, False)
root.set_appearance_mode(main_theme)

root.bind('<Delete>', delete_selected_vertexes)
root.bind('<Control-x>', cut_selected_vertexes)
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
filemenu.add_command(label="Экспорт в текст", command=export_to_text)
filemenu.add_command(label="Импорт из текста", command=import_from_text)

algsmenu = Menu(mainmenu, tearoff=0)
algsmenu.add_command(label="Кол-во вершин", command=vertexes_count)
algsmenu.add_command(label="Кол-во ребер", command=edges_count)
algsmenu.add_command(label="Степени вершин", command=vertexes_degree)
algsmenu.add_command(label="Матрица смежности", command=get_adj_matrix)
algsmenu.add_command(label="Матрица инцидентности", command=get_inc_matrix)
algsmenu.add_command(label="Граф - дерево?", command=is_tree)
algsmenu.add_command(label="Граф полный?", command=is_full)
algsmenu.add_command(label="Граф эйлеров?", command=is_eulerian)
algsmenu.add_command(label="Граф гамильтонов?", command=is_hamiltonian)
algsmenu.add_separator()
algsmenu.add_command(label="Поиск кратчайшего пути", command=find_shortest_path)
algsmenu.add_command(label="Нахождение наименьшего расстояния", command=find_shortest_path)
algsmenu.add_command(label="Нахождние центра", command=find_center)
algsmenu.add_command(label="Нахождние радиуса", command=find_radius)
algsmenu.add_command(label="Нахождние диаметра", command=find_diameter)
algsmenu.add_command(label="Поиск эйлерова цикла", command=eulerian_path)
algsmenu.add_command(label="Поиск гамильтонова цикла", command=hamiltonian_path)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Алгоритмы", menu=algsmenu)


# Раздел редактора
create_new_graph_btn = ctk.CTkButton(root, text='', bg_color=btns_color, fg_color=add_tab_button,
                                image=PhotoImage(file=path_to_img_create_new_tab),
                                corner_radius=5, command=add_new_tab)
create_new_graph_btn.place(anchor='w', relx=0.9097, rely=0.3)

root.bind('q', close_program)
root.mainloop()