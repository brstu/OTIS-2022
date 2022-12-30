from tkinter import Tk, Canvas, Button, Label, Entry, Checkbutton, BooleanVar
from tkinter import messagebox as mb
import numpy as np

tk = Tk()  # Создание окна
tk.title("Graph")  # Заголовок окна
tk.geometry("890x860+410+10")  # Размер окна и его расположение
tk.resizable(False, False)  # Запрет на изменение размера окна
# tk.state('zoomed') #Развернуть окно на весь экран
# tk.overrideredirect(True)  # убирает рамку окна и запрещает его изменять размер
tk.wm_attributes('-topmost', 1)  # Окно всегда сверху
# tk.update()

canvas = Canvas(tk, bg="#888", width=886, height=726)  # Создание холста

canvas.place(x=0, y=130)  # Расположение холста

label = Label(tk)  # Создание метки
label.place(x=370, y=100)  # Расположение метки
label["text"] = "Имя графа"  # Текст метки


# Класс создания вершины
class Vertex:
    def __init__(self, canvas, color):
        global x_click, y_click, vert_name, vertex_count
        self.vertex_count = vertex_count
        self.vert_name = vert_name[-1]
        self.canvas = canvas
        self.color = color
        self.x = x_click
        self.y = y_click
        self.id_vert = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=color, width=2)
        self.id_txt = self.canvas.create_text(self.x, self.y, anchor='center', text=self.vert_name,
                                              font="Arial 10", fill="white")
        canvas.unbind("<Button-1>")

    def get_info(self):
        return self.vertex_count, self.vert_name[self.vertex_count - 1]


class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex, weight: int = 0):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.x1, self.y1 = vertex1.x, vertex1.y
        self.x2, self.y2 = vertex2.x, vertex2.y

        self.weight = weight
        if var1.get():
            self.line = canvas.create_line(line_intersect_circle(self.x1, self.y1, self.x2, self.y2), width=2,
                                           arrow="last")
            if weight != "0":
                self.rect = canvas.create_rectangle((self.x1 + self.x2) / 2 - 5,
                                                    (self.y1 + self.y2) / 2 - 8,
                                                    (self.x1 + self.x2) / 2 + 5,
                                                    (self.y1 + self.y2) / 2 + 8,
                                                    fill='white', width=0)
                self.text = canvas.create_text((self.x1 + self.x2) / 2,
                                               (self.y1 + self.y2) / 2,
                                               text=self.weight,
                                               font=('Arial', 14), fill='black', )
            else:
                self.rect = None
                self.text = None
        else:
            self.line = canvas.create_line(line_intersect_circle(self.x1, self.y1, self.x2, self.y2), width=2)
            if weight != "0":
                self.rect = canvas.create_rectangle((self.x1 + self.x2) / 2 - 5,
                                                    (self.y1 + self.y2) / 2 - 8,
                                                    (self.x1 + self.x2) / 2 + 5,
                                                    (self.y1 + self.y2) / 2 + 8,
                                                    fill='white', width=0)
                self.text = canvas.create_text((self.x1 + self.x2) / 2,
                                               (self.y1 + self.y2) / 2,
                                               text=self.weight,
                                               font=('Arial', 14), fill='black', )
            else:
                self.rect = None
                self.text = None

    def delete(self):
        canvas.delete(self.line)
        canvas.delete(self.rect)
        canvas.delete(self.text)


# Отслеживание нажатия кнопки мыши и запись в глобальные переменные
def on_wasd(event):
    global x_click, y_click
    x_click = event.x
    y_click = event.y


# function create matrix adjacency from list of edges and print it in new window tkinter
def create_matrix_adjacency():
    global vert_name, edges
    matrix_adjacency = [[0 for i in range(vert_name.__len__())] for i in range(vert_name.__len__())]
    for edge in edges:
        matrix_adjacency[vert_name.index(edge.vertex1.vert_name)][vert_name.index(edge.vertex2.vert_name)] = 1
        matrix_adjacency[vert_name.index(edge.vertex2.vert_name)][vert_name.index(edge.vertex1.vert_name)] = 1
    window = Tk()
    window.title("Матрица смежности")
    window.geometry("400x400+0+0")
    for i in range(matrix_adjacency.__len__()):
        for j in range(len(matrix_adjacency[0])):
            Label(window, text=matrix_adjacency[i][j], font="Arial 10", width=5, height=2, borderwidth=1,
                  relief="solid").grid(
                row=i, column=j)
    window.mainloop()


# function create matrix incendence from list of edges and print it in new window tkinter
def create_matrix_incidence_window():
    global vert_name, edges
    matrix = [[0 for i in range(len(edges))] for i in range(len(vert_name))]
    for i in range(edges.__len__()):
        matrix[vert_name.index(edges[i].vertex1.vert_name)][i] = 1
        matrix[vert_name.index(edges[i].vertex2.vert_name)][i] = 1
    window = Tk()
    window.title("Матрица инцидентности")
    window.geometry("400x400+0+0")
    for i in range(matrix.__len__()):
        for j in range(len(matrix[0])):
            Label(window, text=matrix[i][j], font="Arial 10", width=5, height=2, borderwidth=1, relief="solid").grid(
                row=i, column=j)
    window.mainloop()


# функция выхода из программы
def quitfunc(root):
    root.destroy()


# Законченная функция создания имени графа №1
def change_graf_name(name, root):
    label["text"] = name
    quitfunc(root)


# Законченная функция создания имени графа №2
def graf_name():
    new_window = Tk()
    new_window.title("Задайте имя графа")  # Заголовок окна
    new_window.wm_attributes('-topmost', 1)  # Окно всегда сверху
    new_window.resizable(False, False)  # Запрет на изменение размера окна
    labelGraph = Label(new_window)
    labelGraph["text"] = "Введите имя графа"
    labelGraph.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_window)
    entry.grid(row=1, column=0)
    btnGraf = Button(new_window, text="Ввод", command=lambda: change_graf_name(entry.get(), new_window))
    btnGraf.grid(row=2, column=0, sticky="ew")
    if entry.get == label["text"]:
        new_window.destroy()
    new_window.mainloop()


def move_vertex2():
    canvas.bind("<Button-1>", select_vertex)


# function select vertex with mouse click
def select_vertex(event):
    global x_click, y_click, sel_vert
    x_click = event.x
    y_click = event.y
    for vert in vertex:
        if vert.x - 20 <= x_click <= vert.x + 20 and vert.y - 20 <= y_click <= vert.y + 20:
            sel_vert = vert
            canvas.bind("<B1-Motion>", move_vertex)
            canvas.bind("<ButtonRelease-1>", unselect_vertex)
            print(sel_vert.vert_name, x_click, y_click)
            break


def move_vertex(event):
    global x_click, y_click, sel_vert, vertex
    x_click = event.x
    y_click = event.y
    sel_vert.x = x_click
    sel_vert.y = y_click
    canvas.coords(sel_vert.id_vert, x_click - 20, y_click - 20, x_click + 20, y_click + 20)
    canvas.coords(sel_vert.id_txt, x_click, y_click)
    for edge in edges:
        if edge.vertex1 == sel_vert:
            canvas.coords(edge.line, line_intersect_circle(x_click, y_click, edge.vertex2.x, edge.vertex2.y))
            canvas.coords(edge.rect, (x_click + edge.vertex2.x) / 2 - 5,
                          (y_click + edge.vertex2.y) / 2 - 8,
                          (x_click + edge.vertex2.x) / 2 + 5,
                          (y_click + edge.vertex2.y) / 2 + 8)
            canvas.coords(edge.text, (x_click + edge.vertex2.x) / 2, (y_click + edge.vertex2.y) / 2)

        elif edge.vertex2 == sel_vert:
            canvas.coords(edge.line, line_intersect_circle(edge.vertex1.x, edge.vertex1.y, x_click, y_click))
            canvas.coords(edge.rect, (x_click + edge.vertex1.x) / 2 - 5,
                          (y_click + edge.vertex1.y) / 2 - 8,
                          (x_click + edge.vertex1.x) / 2 + 5,
                          (y_click + edge.vertex1.y) / 2 + 8)
            canvas.coords(edge.text, (x_click + edge.vertex1.x) / 2, (y_click + edge.vertex1.y) / 2)


def unselect_vertex(event):
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")


def save_data():
    pass


# Законченная функция выбора цвета вершины
def give_color(numb):
    global color
    if (numb == 1):
        color = "blue"
    elif (numb == 2):
        color = "red"
    elif (numb == 3):
        color = "green"
    else:
        color = "white"


# Функция создания вершины
def create_vertex(root, entry):
    global call_count, vertex_count, color, vertex, vert_name
    if '' == entry.get():
        mb.showerror("Ошибка", "Вы не ввели имя вершины")
    elif entry.get() in [vert.vert_name for vert in vertex]:
        mb.showerror("Ошибка", "Такая вершина уже существует")
    elif entry.get() not in [vert.vert_name for vert in vertex]:
        vert_name[vertex_count] = entry.get()
        call_count += 1
    if call_count != 0:
        vertex_count += 1
        vertex.append(Vertex(canvas, color))
        call_count = 0
        root.destroy()


call_count = 0


# Меню создания вершины
def menu_create_vetrex():
    global vert_name, call_count
    call_count = 0
    canvas.bind("<Button-1>", on_wasd)  # Событие нажатия кнопки мыши
    vert_name.append("")
    new_window = Tk()
    new_window.geometry("230x100+0+0")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label = Label(new_window)
    label["text"] = "Введите имя вершины"
    entry = Entry(new_window)
    btnColor1 = Button(new_window, text="Синий", command=lambda: give_color(1), bg="blue")
    btnColor2 = Button(new_window, text="Красный", command=lambda: give_color(2), bg="red")
    btnColor3 = Button(new_window, text="Зелёный", command=lambda: give_color(3), bg="green")
    btnCreate = Button(new_window, text="Создать\nвершину", command=lambda: create_vertex(new_window, entry))
    label.grid(row=0, column=0, sticky="ew")
    entry.grid(row=1, column=0, sticky="ewns")
    btnColor1.grid(row=0, column=1, sticky="ew")
    btnColor2.grid(row=1, column=1, sticky="ew")
    btnColor3.grid(row=2, column=1, sticky="ewn")
    btnCreate.grid(row=2, column=0, sticky="ew")

    new_window.mainloop()


# Меню удаления вершины
def find_delete_vertex(entry, root):
    global vert_name, vertex, vertex_count, edge_count
    vertex_count -= 1
    flag = 1
    while flag:
        for j, edge in enumerate(edges):
            if edge.vertex1.vert_name == entry or edge.vertex2.vert_name == entry:
                canvas.delete(edge.line)
                canvas.delete(edge.text)
                canvas.delete(edge.rect)
                edges.pop(j)
                edge_count -= 1
        for i, vert in enumerate(vertex):
            if vert.vert_name == entry:
                canvas.delete(vert.id_vert)  # Удаление вершины по её id
                canvas.delete(vert.id_txt)  # Удаление текста по id вершины
                vertex.pop(i)
                vert_name.pop(i)
                root.destroy()
                flag = 0
                break
        else:
            mb.showerror("Ошибка", "Вы ввели неверное имя вершины")
            break
    if edge_count == 0:
        c2["state"] = "normal"


# Удаление вершины
def delete_vertex():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label = Label(new_window)
    label["text"] = "Введите имя удаляемой вершины"
    label.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_window)
    entry.grid(row=1, column=0)
    btnDel = Button(new_window, text="Ввод", command=lambda: find_delete_vertex(entry.get(), new_window))
    btnDel.grid(row=2, column=0, sticky="ew")
    if entry.get == label["text"]:
        new_window.destroy()


def find_delete_edge(en1, en2, root):
    global vertex, vert_name, edge_count, edges
    for i, edge in enumerate(edges):
        if edge.vertex1.vert_name == en1 and edge.vertex2.vert_name == en2:
            canvas.delete(edge.line)
            canvas.delete(edge.text)
            canvas.delete(edge.rect)
            edges.pop(i)
            edge_count -= 1
            root.destroy()
            break
    else:
        mb.showerror("Ошибка", "Такого ребра не существует")
    if edge_count == 0:
        c2["state"] = "normal"


def menu_delete_edge():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label = Label(new_window)
    label["text"] = "Введите имя вершин, между которыми \nудаляется ребро\nПервая вершина"
    label.grid(row=0, column=0, sticky="ew")
    label2 = Label(new_window)
    label2["text"] = "Вторая вершина"
    entry = Entry(new_window)
    entry2 = Entry(new_window)
    entry.grid(row=1, column=0, sticky="ew")
    label2.grid(row=2, column=0, sticky="ew")
    entry2.grid(row=3, column=0, sticky="ew")
    btnDel = Button(new_window, text="Ввод", command=lambda: find_delete_edge(entry.get(), entry2.get(), new_window))
    btnDel.grid(row=4, column=0, sticky="ew")


# Переназвание вершины
def rename_vertex(en1, en2, root):
    global vert_name, vertex
    for vert in vertex:
        if vert.vert_name == en1 and en2 not in vert_name:
            vert.vert_name = en1
            canvas.itemconfigure(vert.id_txt, text=en2)
            vert_name[vert_name.index(en1)] = en2
            root.destroy()
            break
    else:
        mb.showerror("Ошибка", "Вы ввели неверное имя вершины")


# Меню переназвания вершины
def menu_rename_vertex():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label1 = Label(new_window)
    label1["text"] = "Введите имя изменяемой вершины"
    label1.grid(row=0, column=0, sticky="ew")
    entry1 = Entry(new_window)
    entry1.grid(row=1, column=0, sticky="ew")
    label2 = Label(new_window)
    label2["text"] = "Введите новое имя вершины"
    label2.grid(row=2, column=0, sticky="ew")
    entry2 = Entry(new_window)
    entry2.grid(row=3, column=0, sticky="ew")
    btnRen = Button(new_window, text="Изменить имя",
                    command=lambda: rename_vertex(entry1.get(), entry2.get(), new_window))
    btnRen.grid(row=4, column=0, sticky="ew")


def line_intersect_circle(x1, y1, x2, y2):
    main_gipotenuza = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenuza - 20) * main_dx / main_gipotenuza
    dy = (main_gipotenuza - 20) * main_dy / main_gipotenuza

    return x2 - dx, y2 - dy, x1 + dx, y1 + dy


def create_edge(en1, en2, weight, root):
    global vertex, vert_name, edge_count
    vert1, vert2 = 0, 0
    for vert in vertex:
        if vert.vert_name == en1:
            vert1 = vert
            break
    else:
        mb.showerror("Ошибка", "Вы ввели неверное имя вершины")
    for vert in vertex:
        if vert.vert_name == en2:
            vert2 = vert
            break
    else:
        mb.showerror("Ошибка", "Вы ввели неверное имя вершины")
    edges.append(Edge(vert1, vert2, weight))
    c2["state"] = "disable"
    edge_count += 1
    root.destroy()


def menu_create_edge():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(False, False)
    label1 = Label(new_window)
    label1["text"] = "Введите имя 1-ой вершины"
    entry1 = Entry(new_window)
    entry2 = Entry(new_window)
    entry3 = Entry(new_window)
    entry3.insert(0, "0")
    label2 = Label(new_window)
    label3 = Label(new_window)
    label3["text"] = "Введите вес вершины"
    label2["text"] = "Введите имя 2-ой вершины"
    label1.grid(row=0, column=0, sticky="ew")
    btnVertName = Button(new_window, text="Ввод",
                         command=lambda: create_edge(entry1.get(), entry2.get(), entry3.get(), new_window))
    entry1.grid(row=1, column=0, sticky="ew")
    label2.grid(row=2, column=0, sticky="ew")
    entry2.grid(row=3, column=0, sticky="ew")
    label3.grid(row=4, column=0, sticky="ew")
    entry3.grid(row=5, column=0, sticky="ew")
    btnVertName.grid(row=0, column=1, rowspan=6, sticky="ns")


sel_vert = None
vert_name = []  # Список имен вершин
edges = []
vertex = []  # Глобальные переменные
color = "red"  # Цвет вершины
x_click = 0  # Глобальные переменные
x_move = []  # Список координат x
y_click = 0  # Глобальные переменные
y_move = []  # Список координат y
vertex_count = 0  # Счетчик вершин
edge_count = 0
var1 = BooleanVar()
var1.set(False)
var2 = BooleanVar()
var2.set(False)

btn1 = Button(tk, text="Задать имя графа", command=graf_name)
btn2 = Button(tk, text="Сохранить Значения", command=save_data)
# btn3 = Button(tk, text="Импортировать значения", command=import_data)
btn4 = Button(tk, text="Создать вершину", command=menu_create_vetrex)
btn5 = Button(tk, text="Удалить вершину", command=delete_vertex)
btn6 = Button(tk, text="Переименовать вершину", command=menu_rename_vertex)
btn7 = Button(tk, text="Создать ребро", command=menu_create_edge)
btn8 = Button(tk, text="quit", command=exit)
btn9 = Button(tk, text="Удалить ребро", command=menu_delete_edge)
c2 = Checkbutton(tk, text="Ориентированность", onvalue=1, offvalue=0, variable=var1, bg="gray")
c1 = Button(tk, text="Передвижение вершин", command=move_vertex2)
btn11 = Button(tk, text="Матрица инцендентности", command=create_matrix_incidence_window)
btn12 = Button(tk, text="Матрица смежности", command=create_matrix_adjacency)

btn1.grid(row=0, column=0, stick="ew")
btn2.grid(row=0, column=4, stick="ew")
# btn3.grid(row=1, column=4, stick="ew")
btn4.grid(row=0, column=1, stick="ew")
btn5.grid(row=1, column=1, stick="ew")
btn6.grid(row=2, column=1, stick="ew")
btn7.grid(row=0, column=2, stick="ew")
btn8.grid(row=1, column=5, stick="ew")
btn9.grid(row=1, column=2, stick="ew")
c1.grid(row=1, column=0, stick="ew")
c2.grid(row=2, column=2, stick="ew")
btn11.grid(row=1, column=3, stick="ew")
btn12.grid(row=0, column=3, stick="ew")

tk.mainloop()
