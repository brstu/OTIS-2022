from tkinter import messagebox as mb
import tkinter as tk
from math import inf, sqrt
import networkx as nx
application = tk.Tk() # Создание окна
application.geometry("860x860+310+0") # Размер окна и его расположение
application.resizable(0, 0) #Запрет на изменение размера окна
application.wm_attributes('-topmost', 1) # Окно всегда сверху

canvas = tk.Canvas(application, bg="white", width=856, height=726) # Создание холста

canvas.place(x=0, y=120)
application.title("работа с графами")

label = tk.Label(application) # Создание метки
label.place(x=370, y=125) # Расположение метки
label["text"] = "Имя графа" # Текст метки

global color_vertices_line # для хранения цвета вершин и рёбер
color_vertices_line = 'white'
global name_vertex # имя вершины
name_vertex = ""
array_name_vertex = [] # массив имен вершин
all_name_garphs = [] # для имён графа
global rename_name
rename_name = ""



data_vertex_id_x_y = dict() # словарь для хранения ID рёбер их координат и имени
global ID # id вершин
ID = 0
# array_all_ID = []


global non_oriented_line # что-то типо счётчика
non_oriented_line = 0
global ID_none_oriented_line # ID для неоринтированных рёбер
ID_none_oriented_line = 0
data_id_unorient_line_x_y = dict() # словарь для хранения ID неориентированных рёбер и для имён и координат вершин с которыми они соединены
global count_unoriented_line # количесвто рёбер
count_unoriented_line = 0

global oriented_line # что-то типо счётчика
oriented_line = 0
global ID_oriented_line # ID для оринтированных рёбер
ID_oriented_line = 0
data_id_orient_line_x_y = dict() # словарь для хранения ID ориентированных рёбер и для имён и координат вершин с которыми они соединены


global weight
weight = 0
data_weight_line_x_y = dict() # массив для весов
global ID_weight
ID_weight = 0


temp_edges = [] # список ребёр
global max_node # максимальная степень вершины
max_node = 0
nodes = [] # список всех вершин
# weight = []
global UNORIN_ORIENT # булевая переменная для проверки на ориентированность графа
UNORIN_ORIENT = 0 # если = 0 то граф неориентированный


global result_adjancy_matrix,result_incidency_matrix # матрица смежности
result_adjancy_matrix = []
result_incidency_matrix = [] # матрица инцидентности


global x1, y1, x2, y2 # переменные используемые для хранения координат вершин в функицях
x1, y1, x2, y2 = 0, 0, 0, 0
application.update()



def line_intersect_circle(x1, y1, x2, y2):# функция для нахождения точек пересечения прямой и окружности
    '''Возвращает координаты точек пересечения прямой и двух окружностей'''
    main_gipotenusa = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenusa - 15) * main_dx / main_gipotenusa
    dy = (main_gipotenusa - 15) * main_dy / main_gipotenusa
    return x2 - dx, y2 - dy, x1 + dx, y1 + dy



def draw_vertixes(): # рисование вершин
    canvas.bind_all("<Button-1>", draw_vertex_on_click)
def draw_vertex_on_click(event):
    global name_vertex
    global color_vertices_line
    r=15
    global ID
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    if mouse_y > 0:
        canvas.create_oval(mouse_x - r, mouse_y - r, mouse_x + r, mouse_y+ r,fill=color_vertices_line, outline="black", width=2)
        print(mouse_x, mouse_y)
        ID+=1
        # array_all_ID.append(ID)
        data_vertex_id_x_y[ID] = [mouse_x, mouse_y, name_vertex,color_vertices_line]
        print("data_vertex_id_x_y\t",data_vertex_id_x_y)
        canvas.create_text(mouse_x, mouse_y, text=name_vertex, font="Arial 14")

def change_color_vertex(): # изменение цвета вершин
    canvas.bind_all("<Button-1>", change_color_vertex_on_click)
def change_color_vertex_on_click(event):
    global color_vertices_line
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and \
            mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            data_vertex_id_x_y[i][3] = color_vertices_line
            canvas.create_oval(data_vertex_id_x_y[i][0] - 15,data_vertex_id_x_y[i][1] - 15, data_vertex_id_x_y[i][0] + 15, \
                 data_vertex_id_x_y[i][1] + 15,fill=color_vertices_line, outline="black", width=2)
            canvas.create_text(data_vertex_id_x_y[i][0], data_vertex_id_x_y[i][1], text=data_vertex_id_x_y[i][2], font="Arial 14")
            print("data_vertex_id_x_y\t",data_vertex_id_x_y)


def draw_unoriented_line_between_vertex(): # рисование неориентированного ребра
    canvas.bind_all("<Button-1>",draw_line_between_vertex_on_click)
def draw_line_between_vertex_on_click(event):
    global x1, y1, x2, y2, non_oriented_line, ID_none_oriented_line, name1, name2,color
    global count_unoriented_line
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    color = color_vertices_line
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and \
            mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            if non_oriented_line == 0:
                name1 = data_vertex_id_x_y[i][2]
                x1 = data_vertex_id_x_y[i][0]
                y1 = data_vertex_id_x_y[i][1]
                non_oriented_line += 1
                break
            elif non_oriented_line == 1:
                ID_none_oriented_line+=1
                name2 = data_vertex_id_x_y[i][2]
                x2 = data_vertex_id_x_y[i][0]
                y2 = data_vertex_id_x_y[i][1]
                count_unoriented_line+=1
                data_id_unorient_line_x_y[ID_none_oriented_line] = [[x1,y1,name1,color],[x2,y2,name2,color]]
                print("data_id_unorient_line_x_y\t",data_id_unorient_line_x_y)
                canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill=color, width=2)
                non_oriented_line = 0
                break
def delete_unoriented_line(): # удаление неориентированного ребра
    canvas.bind_all("<Button-1>",delete_unoriented_line_on_click)
def delete_unoriented_line_on_click(event):
    global x1, y1, x2, y2, non_oriented_line, ID_none_oriented_line, name1, name2,color
    global count_unoriented_line
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            if non_oriented_line == 0:
                name1 = data_vertex_id_x_y[i][2]
                x1 = data_vertex_id_x_y[i][0]
                y1 = data_vertex_id_x_y[i][1]
                non_oriented_line += 1
                print("nam1,x1,y1   ",name1,x1,y1)
                break
            elif non_oriented_line == 1:
                name2 = data_vertex_id_x_y[i][2]
                x2 = data_vertex_id_x_y[i][0]
                y2 = data_vertex_id_x_y[i][1]
                print("nam2,x2,y2   ",name2,x2,y2)
                count_unoriented_line-=1
                for key in data_id_unorient_line_x_y:
                    if data_id_unorient_line_x_y[key][0][0] == x1 and data_id_unorient_line_x_y[key][0][1] == y1 and\
                         data_id_unorient_line_x_y[key][1][0] == x2 and data_id_unorient_line_x_y[key][1][1] == y2:
                        print("data_id_unorient_line_x_y in delete\t",data_id_unorient_line_x_y)
                        canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill="white", width=3)
                        del data_id_unorient_line_x_y[key]
                        break
                    elif data_id_unorient_line_x_y[key][0][0] == x2 and data_id_unorient_line_x_y[key][0][1] == y2 and\
                         data_id_unorient_line_x_y[key][1][0] == x1 and data_id_unorient_line_x_y[key][1][1] == y1:
                        print("data_id_unorient_line_x_y in delete\t",data_id_unorient_line_x_y)
                        canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill="white", width=3)
                        del data_id_unorient_line_x_y[key]
                        break
                print("data_id_unorient_line_x_y in delete\t",data_id_unorient_line_x_y)
                canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill="white", width=3)
                non_oriented_line = 0
                break


def draw_oriented_line_between_vertex(): # рисование ориентированного ребра
    canvas.bind_all("<Button-1>",draw_oriented_line_between_vertex_on_click)
def draw_oriented_line_between_vertex_on_click(event):
    global x1, y1, x2, y2, oriented_line, ID_oriented_line, name1, name2,color1
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    color1 = color_vertices_line
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            if oriented_line == 0:
                name1 = data_vertex_id_x_y[i][2]
                x1 = data_vertex_id_x_y[i][0]
                y1 = data_vertex_id_x_y[i][1]
                oriented_line += 1
                break
            elif oriented_line == 1:
                ID_oriented_line+=1
                name2 = data_vertex_id_x_y[i][2]
                x2 = data_vertex_id_x_y[i][0]
                y2 = data_vertex_id_x_y[i][1]
                data_id_orient_line_x_y[ID_oriented_line] = [[x1,y1,name1,color1],[x2,y2,name2,color1]]
                print("data_id_orient_line_x_y\t",data_id_orient_line_x_y)
                canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill=color1, width=2, arrow=tk.LAST)
                oriented_line = 0
                break
def delete_oriented_line(): # удаление ориентированного ребра
    canvas.bind_all("<Button-1>",delete_oriented_line_on_click)
def delete_oriented_line_on_click(event):
    global x1, y1, x2, y2, oriented_line, ID_oriented_line, name1, name2
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            if oriented_line == 0:
                name1 = data_vertex_id_x_y[i][2]
                x1 = data_vertex_id_x_y[i][0]
                y1 = data_vertex_id_x_y[i][1]
                oriented_line += 1
                print("nam1,x1,y1   ",name1,x1,y1)
                break
            elif oriented_line == 1:
                name2 = data_vertex_id_x_y[i][2]
                x2 = data_vertex_id_x_y[i][0]
                y2 = data_vertex_id_x_y[i][1]
                print("nam2,x2,y2   ",name2,x2,y2)
                for key in data_id_orient_line_x_y:
                    if data_id_orient_line_x_y[key][0][0] == x1 and data_id_orient_line_x_y[key][0][1] == y1 and\
                         data_id_orient_line_x_y[key][1][0] == x2 and data_id_orient_line_x_y[key][1][1] == y2:
                        del data_id_orient_line_x_y[key]
                        break
                    elif data_id_orient_line_x_y[key][0][0] == x2 and data_id_orient_line_x_y[key][0][1] == y2 and\
                         data_id_orient_line_x_y[key][1][0] == x1 and data_id_orient_line_x_y[key][1][1] == y1:
                        del data_id_orient_line_x_y[key]
                        break
                print("data_id_orient_line_x_y in delete\t",data_id_orient_line_x_y)
                canvas.create_line(*line_intersect_circle(x1, y1, x2, y2), fill="white", width=3, arrow=tk.LAST)
                oriented_line = 0
                break


def draw_weight_line(): # рисование веса
    canvas.bind_all("<Button-1>",draw_weight_on_click)
def draw_weight_on_click(event):
    global weight,ID_weight
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    if mouse_y > 0:
        ID_weight+=1
        data_weight_line_x_y[ID_weight]=[mouse_x,mouse_y,weight]
        print("data_weight_line_x_y\t",data_weight_line_x_y)
        canvas.create_text(mouse_x, mouse_y, text=weight, fill = "black", font=("Purisa", 12))


def delete_weight_line(): # удаление веса
    canvas.bind_all("<Button-1>",delete_weight_on_click)
def delete_weight_on_click(event):
    global weight,ID_weight
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    if mouse_y > 0:
        for key in data_weight_line_x_y:
            if data_weight_line_x_y[key][0] == mouse_x and data_weight_line_x_y[key][1] == mouse_y:
                del data_weight_line_x_y[key]
                break
    canvas.create_oval(mouse_x-10, mouse_y-10, mouse_x+10, mouse_y+10, fill="white", outline="white")

def input_weight(): # рисование веса
    new_application1 = tk.Tk()
    new_application1.title("Задайте вес ребра")
    new_application1.resizable(15, 15)
    label1 = tk.Label(new_application1, text="Введите вес ребра")
    label1.grid(row=0, column=0, sticky="ew")
    entry1 = tk.Entry(new_application1)
    entry1.grid(row=1, column=0,sticky="ew")
    button1 = tk.Button(new_application1, text="OK", command=lambda: input_weight_on_click(entry1.get(),new_application1))
    button1.grid(row=2, column=0, sticky="ew")
    new_application1.mainloop()
def input_weight_on_click(weight_line,root):
    global weight
    if weight_line == "":
        mb.showerror("","Вы не вес ребра")
    else:
        weight = weight_line
        root.destroy()


def NAME_VERTEX(): # функция для задания имени вершины
    new_application = tk.Tk()
    new_application.title("Задайте имя вершины")
    new_application.resizable(15, 15)
    label = tk.Label(new_application)
    label["text"] = "Введите имя вершины"
    label.grid(row=0, column=0, sticky="ew")
    entry = tk.Entry(new_application)
    entry.grid(row=1, column=0)
    btnGraf = tk.Button(new_application, text="Ввод вершины", command=lambda: vertex_name(entry.get(), new_application))
    btnGraf.grid(row=2, column=0, sticky="ew")
    new_application.mainloop()
def vertex_name(name, root): # проверка на существование вершины
    global name_vertex
    if name == "":
        mb.showerror(" ","Вы не ввели имя вершины")
    elif name not in array_name_vertex:
        array_name_vertex.append(name)
        print(array_name_vertex)
        name_vertex = name
        root.destroy()
    else:
        mb.showerror(" ","Такая вершина уже существует")

def stop_add_vertex(): # для остановки действия
    canvas.unbind_all("<Button-1>")
def color_vertex(color): # для изменения цвета вершины
    global color_vertices_line
    color_vertices_line = color
    print(color_vertices_line)
 

def graph_name(): # изменение имени графа
    new_application = tk.Tk()
    new_application.title("Задайте имя графа")
    new_application.wm_attributes('-topmost', 1)
    new_application.resizable(0, 0)
    label = tk.Label(new_application)
    label["text"] = "Введите имя графа"
    label.grid(row=0, column=0, sticky="ew")
    entry = tk.Entry(new_application)
    entry.grid(row=1, column=0)
    btnGraf = tk.Button(new_application, text="Ввод", command=lambda: change_graf_name(entry.get(), new_application))
    btnGraf.grid(row=2, column=0, sticky="ew")
    new_application.mainloop()
def change_graf_name(name, root): # изменение имени графа
    if name in all_name_garphs:
        mb.showerror(" ","Такое имя графа уже существует")
    elif name == "":
        mb.showerror(" ","Вы не ввели имя графа")
    else:
        label["text"] = name
        all_name_garphs.append(name)
        print(all_name_garphs)
        root.destroy()
    

def delete_vertex():# удаление вершины
    canvas.bind_all("<Button-1>", delete_vertex_on_click)
def delete_vertex_on_click(event):
    name_delete_vertex = ''
    global ID_none_oriented_line,ID_oriented_line
    all_delete_name1 = []
    all_delete_name2 = []
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            # canvas.delete(data_vertex_id_x_y[i][2])
            canvas.create_oval(data_vertex_id_x_y[i][0] - 15, data_vertex_id_x_y[i][1] - 15, data_vertex_id_x_y[i][0] + 15,\
                 data_vertex_id_x_y[i][1] + 15,fill="white", outline="white", width=2)
            name_delete_vertex = data_vertex_id_x_y[i][2]
            
            print("словарь вершин:\t",data_vertex_id_x_y[i][2])
            if ID_none_oriented_line !=0:
                for name in data_id_unorient_line_x_y:
                    if data_id_unorient_line_x_y[name][0][2] == name_delete_vertex or data_id_unorient_line_x_y[name][1][2] == name_delete_vertex:
                        canvas.create_line(*line_intersect_circle(data_id_unorient_line_x_y[name][0][0], data_id_unorient_line_x_y[name][0][1],\
                             data_id_unorient_line_x_y[name][1][0], data_id_unorient_line_x_y[name][1][1]), fill="white", width=3)
                        canvas.delete(data_id_unorient_line_x_y[name])
                        
                        all_delete_name1.append(name)
                for j in all_delete_name1:
                    del data_id_unorient_line_x_y[j]
                print("data_id_unorient_line_x_y:\t",data_id_unorient_line_x_y)
            if ID_oriented_line !=0:
                for name in data_id_orient_line_x_y:
                    if data_id_orient_line_x_y[name][0][2] == name_delete_vertex or data_id_orient_line_x_y[name][1][2] == name_delete_vertex:
                        canvas.create_line(*line_intersect_circle(data_id_orient_line_x_y[name][0][0], data_id_orient_line_x_y[name][0][1],\
                            data_id_orient_line_x_y[name][1][0], data_id_orient_line_x_y[name][1][1]), fill="white", width=3, arrow=tk.LAST)
                        canvas.delete(data_id_orient_line_x_y[name])
                        all_delete_name2.append(name)
                for j in all_delete_name2:
                    del data_id_orient_line_x_y[j]
                print("data_id_orient_line_x_y:\t",data_id_orient_line_x_y)
            del data_vertex_id_x_y[i]
            array_name_vertex.remove(name_delete_vertex)
            print("array_name_vertex:\t",array_name_vertex)
            print("словарь вершин:\t",data_vertex_id_x_y)
            break


global name_vanish_vertex
name_vanish_vertex = ''
global ID_vanish_vertex
ID_vanish_vertex = 0
all_vanish_nonorline_id = []
all_vanish_orline_id = []
def move_vertex_and_line():
    canvas.bind_all("<Button-1>", vanish_vertex_on_click)
def vanish_vertex_on_click(event):
    print("event",event)
    global ID_none_oriented_line,ID_oriented_line, name_vanish_vertex, ID_vanish_vertex
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y: # delete vertex and line with this vertex
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            canvas.create_oval(data_vertex_id_x_y[i][0] - 15, data_vertex_id_x_y[i][1] - 15, data_vertex_id_x_y[i][0] + 15,\
                 data_vertex_id_x_y[i][1] + 15,fill="white", outline="white", width=2)
            name_vanish_vertex = data_vertex_id_x_y[i][2]
            ID_vanish_vertex = i
            print("имена вершин:\t",array_name_vertex)
            print("словарь вершин:\t",data_vertex_id_x_y[i][2])
            if ID_none_oriented_line !=0:
                for tid in data_id_unorient_line_x_y:
                    if data_id_unorient_line_x_y[tid][0][2] == name_vanish_vertex or data_id_unorient_line_x_y[tid][1][2] == name_vanish_vertex:
                        canvas.create_line(*line_intersect_circle(data_id_unorient_line_x_y[tid][0][0], data_id_unorient_line_x_y[tid][0][1],\
                             data_id_unorient_line_x_y[tid][1][0], data_id_unorient_line_x_y[tid][1][1]), fill="white", width=2)
                        all_vanish_nonorline_id.append(tid)
                print("data_id_unorient_line_x_y:\t",data_id_unorient_line_x_y)
            if ID_oriented_line !=0:
                for tid in data_id_orient_line_x_y:
                    if data_id_orient_line_x_y[tid][0][2] == name_vanish_vertex or data_id_orient_line_x_y[tid][1][2] == name_vanish_vertex:
                        canvas.create_line(*line_intersect_circle(data_id_orient_line_x_y[tid][0][0], data_id_orient_line_x_y[tid][0][1],\
                             data_id_orient_line_x_y[tid][1][0], data_id_orient_line_x_y[tid][1][1]), fill="white", width=2, arrow=tk.LAST)
                        all_vanish_orline_id.append(tid)
                print("data_id_orient_line_x_y:\t",data_id_orient_line_x_y)
                
            break
    canvas.bind_all("<Button-1>", appearance_vertex_on_move)
def appearance_vertex_on_move(event):
    global ID_none_oriented_line,ID_oriented_line, name_vanish_vertex, ID_vanish_vertex
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    if mouse_y>0:
        temp_color_vertex = data_vertex_id_x_y[ID_vanish_vertex][3]
        data_vertex_id_x_y[ID_vanish_vertex] = [mouse_x, mouse_y, name_vanish_vertex,temp_color_vertex]
        canvas.create_oval(mouse_x - 15, mouse_y - 15, mouse_x + 15, mouse_y + 15,fill=temp_color_vertex, outline="black", width=2)
        canvas.create_text(mouse_x, mouse_y, text=name_vanish_vertex, font="Arial 14")
        print("data_vertex_id_x_y:\t",data_vertex_id_x_y)
        if ID_none_oriented_line !=0:
            for idi in all_vanish_nonorline_id:
                if name_vanish_vertex == data_id_unorient_line_x_y[idi][0][2]:
                    data_id_unorient_line_x_y[idi][0] = [mouse_x, mouse_y, name_vanish_vertex,data_id_unorient_line_x_y[idi][0][3]]
                    canvas.create_line(*line_intersect_circle(data_id_unorient_line_x_y[idi][0][0], data_id_unorient_line_x_y[idi][0][1],\
                         data_id_unorient_line_x_y[idi][1][0], data_id_unorient_line_x_y[idi][1][1]), fill=data_id_unorient_line_x_y[idi][0][3], width=2)
                elif name_vanish_vertex == data_id_unorient_line_x_y[idi][1][2]:
                    data_id_unorient_line_x_y[idi][1] = [mouse_x, mouse_y, name_vanish_vertex,data_id_unorient_line_x_y[idi][1][3]]
                    canvas.create_line(*line_intersect_circle(data_id_unorient_line_x_y[idi][0][0], data_id_unorient_line_x_y[idi][0][1],\
                         data_id_unorient_line_x_y[idi][1][0], data_id_unorient_line_x_y[idi][1][1]), fill=data_id_unorient_line_x_y[idi][1][3], width=2)
            print("data_id_unorient_line_x_y:\t",data_id_unorient_line_x_y)
        if ID_oriented_line !=0:
            for idj in all_vanish_orline_id:
                if name_vanish_vertex == data_id_orient_line_x_y[idj][0][2]:
                    data_id_orient_line_x_y[idj][0] = [mouse_x, mouse_y, name_vanish_vertex,data_id_orient_line_x_y[idj][0][3]]
                    canvas.create_line(*line_intersect_circle(data_id_orient_line_x_y[idj][0][0], data_id_orient_line_x_y[idj][0][1],\
                         data_id_orient_line_x_y[idj][1][0], data_id_orient_line_x_y[idj][1][1]), \
                             fill=data_id_orient_line_x_y[idj][0][3], width=2, arrow=tk.LAST)
                elif name_vanish_vertex == data_id_orient_line_x_y[idj][1][2]:
                    data_id_orient_line_x_y[idj][1] = [mouse_x, mouse_y, name_vanish_vertex,data_id_orient_line_x_y[idj][1][3]]
                    canvas.create_line(*line_intersect_circle(data_id_orient_line_x_y[idj][0][0], data_id_orient_line_x_y[idj][0][1],\
                         data_id_orient_line_x_y[idj][1][0], data_id_orient_line_x_y[idj][1][1]), \
                             fill=data_id_orient_line_x_y[idj][1][3], width=2, arrow=tk.LAST)
            print("data_id_orient_line_x_y:\t",data_id_orient_line_x_y)
                
        
def rename_vertex(): # переименование вершины
    canvas.bind_all("<Button-1>", rename_vertex_on_click)
def rename_vertex_on_click(event):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    print(mouse_x, mouse_y)
    for i in data_vertex_id_x_y:
        if mouse_x > data_vertex_id_x_y[i][0] - 15 and mouse_x < data_vertex_id_x_y[i][0] + 15 and\
             mouse_y > data_vertex_id_x_y[i][1] - 15 and mouse_y < data_vertex_id_x_y[i][1] + 15:
            new_application = tk.Tk()
            new_application.title("Задайте имя вершины")
            new_application.resizable(15, 15)
            label = tk.Label(new_application)
            label["text"] = "Введите имя вершины"
            label.grid(row=0, column=0, sticky="ew")
            entry = tk.Entry(new_application)
            entry.grid(row=1, column=0)
            print("имена вершин: ",array_name_vertex)
            # print("словарь вершин: ",data_vertex_id_x_y[i][2])
            print("оставшийся словарь вершин",data_vertex_id_x_y)
            btnGraf = tk.Button(new_application, text="Ввод вершины", command=lambda: rename_vertex_name(entry.get(), new_application, i))
            btnGraf.grid(row=2, column=0, sticky="ew")
            new_application.mainloop()
            break
def rename_vertex_name(name, root, i):
    global color_vertices_line,rename_name
    if name == "":
        mb.showerror(" ","Вы не ввели имя вершины")
    elif name in array_name_vertex:
        mb.showerror(" ","Такое имя вершины уже существует")
    else:
        canvas.delete(data_vertex_id_x_y[i][2])
        canvas.create_oval(data_vertex_id_x_y[i][0] - 15, data_vertex_id_x_y[i][1] - 15, data_vertex_id_x_y[i][0] + 15,\
             data_vertex_id_x_y[i][1] + 15,fill=color_vertices_line, outline="black", width=2)
        canvas.create_text(data_vertex_id_x_y[i][0], data_vertex_id_x_y[i][1], text=name, font="Arial 14", fill="black")
        array_name_vertex.remove(data_vertex_id_x_y[i][2])
        rename_name=data_vertex_id_x_y[i][2]
        print("rename_name\t",rename_name)
        data_vertex_id_x_y[i][2] = name
        data_vertex_id_x_y[i][3] = color_vertices_line
        if ID_none_oriented_line != 0: # при изменнии имени вершины, делаем проверку на нахождение переименованной вершины в словаре неориентированных ребер
            for i in data_id_unorient_line_x_y: # и если находим, то меняем имя вершины в списке ребер на новое имя
                if data_id_unorient_line_x_y[i][0][2] == rename_name:
                    data_id_unorient_line_x_y[i][0][2] = name

                if data_id_unorient_line_x_y[i][1][2] == rename_name:
                    data_id_unorient_line_x_y[i][1][2] = name
            print("data_id_orient_line_x_y\t",data_id_unorient_line_x_y)
        elif ID_oriented_line != 0: # при изменнии имени вершины, делаем проверку на нахождение переименованной вершины в словаре ориентированных ребер
            for i in data_id_orient_line_x_y: # и если находим, то меняем имя вершины в списке ребер на новое имя
                if data_id_orient_line_x_y[i][0][2] == rename_name:
                    data_id_orient_line_x_y[i][0][2] = name
                if data_id_orient_line_x_y[i][1][2] == rename_name:
                    data_id_orient_line_x_y[i][1][2] = name
            print("data_id_orient_line_x_y\t",data_id_orient_line_x_y)
        array_name_vertex.append(name)
        root.destroy()


def algorithm(): # функция для создания окна с алгоритмами
    global max_node, UNORIN_ORIENT,result_adjancy_matrix,result_incidency_matrix
    new_application = tk.Tk() # Создание окна
    new_application.geometry("432x470+195+0") # Размер окна и его расположение
    new_application.resizable(0, 0) # Запрет на изменение размера окна
    new_application.wm_attributes('-topmost', 1) # Окно всегда сверху
    new_application.title("запишите свой граф и выберите алгоритм") # Заголовок окна
    entry = tk.Entry(new_application, width=20, font="Arial 16")
    
    
    button_dejkstra = tk.Button(new_application, text="Алгоритм\nДейкстры", command=lambda: deikstra(temp_edges,weight,max_node),width=12, height=2)
    input_value = tk.Button(new_application, text="Ввод графа", command=lambda: graph_info(entry.get(), new_application),width=12, height=2)
    button_reading_file = tk.Button(new_application, text="Чтение из файла", command=lambda: reading_file(new_application),width=12, height=2)

    if UNORIN_ORIENT ==0:
        button_diametr_graph = tk.Button(new_application, text="Диаметр графа", command=lambda: diameterGraph(nodes,temp_edges),width=12, height=2)
        button_radius_graph = tk.Button(new_application, text="Радиус графа", command=lambda: radiusGraph(nodes,temp_edges),width=12, height=2)
        button_center_graph = tk.Button(new_application, text="Центр графа", command=lambda: centerGraph(nodes,temp_edges),width=12, height=2)
    else:
        button_diametr_graph = tk.Button(new_application, text="Диаметр графа",\
             command=lambda: diameterGraph(nodes,temp_edges),width=12, height=2, state=tk.DISABLED)
        button_radius_graph = tk.Button(new_application, text="Радиус графа",\
             command=lambda: radiusGraph(nodes,temp_edges),width=12, height=2, state=tk.DISABLED)
        button_center_graph = tk.Button(new_application, text="Центр графа",\
             command=lambda: centerGraph(nodes,temp_edges),width=12, height=2, state=tk.DISABLED)

    entry.grid(row=0, column=1)
    input_value.grid(row=1, column=1, sticky="ew")
    button_reading_file.grid(row=2, column=1, sticky="ew")
    button_adjancy_matrix = tk.Button(new_application, text="Матрица\nсмежности", command=lambda: adjancy_matrix(temp_edges,max_node),width=12, height=2)
    button_incidency_matrix = tk.Button(new_application, text="Матрица\nинцидентности",\
         command=lambda: incidency_matrix(temp_edges,max_node, UNORIN_ORIENT,new_application),width=12, height=2)
    button_euleran_circle = tk.Button(new_application, text="Эйлеров\nцикл", command=lambda: euleran_circle(result_adjancy_matrix),width=12, height=2)
    button_quit = tk.Button(new_application, text="Выход", command=new_application.destroy,width=12, height=2)

    print("result_ajancy_matrix\t",result_adjancy_matrix)
    print("result_incidency_matrix\t",result_incidency_matrix)
    print("max_node=\t", max_node)
    print("nodes=\t", nodes)
    print("edges=\t", weight)
    button_adjancy_matrix.grid(row=1, column=0, sticky="ew")
    button_incidency_matrix.grid(row=0, column=0, sticky="ew")
    button_euleran_circle.grid(row=2, column=0, sticky="ew")
    button_diametr_graph.grid(row=0, column=2, sticky="ew")
    button_radius_graph.grid(row=1, column=2, sticky="ew")
    button_center_graph.grid(row=2, column=2, sticky="ew")
    button_dejkstra.grid(row=3, column=0, sticky="ew")
    button_quit.grid(row=8, column=0, sticky="ew")
    new_application.mainloop()


def graph_info(information, root): # функция для ввода графа
    file = open("info.txt","w")
    file.write(information)
    file.close()
def reading_file(root): # считывание записанного в файл графа
    global max_node, UNORIN_ORIENT, temp_edges, nodes,weight
    file = open("info.txt ","r")
    temp = file.readline()
    information = temp.split(";")
    name_type_graph = information[0]
    temp_nodes = information[1]
    edges_graph = information[2]
    temp_weight = information[3]
    
    UNORIN_ORIENT = 0
    if "UNORIENT" in name_type_graph:
        UNORIN_ORIENT = 0
    elif "ORIENT" in name_type_graph:
        UNORIN_ORIENT = 1

    nodes = temp_nodes.split(",")
    for i ,val in enumerate(nodes):
        nodes[i] = int(val)

    temp = edges_graph.split(",")
    temp_edges = []
    for i,val in enumerate(temp):
        temp_edges.append(temp[i].split("->"))
    for i,vali in enumerate(temp_edges):
        for j,valj in enumerate(vali):
            temp_edges[i][j] = int(valj)
    print("temp edges\t", temp_edges)
    n = len(temp_edges)
    max_node = 0
    for i,val in enumerate(temp_edges):
        for j,valj in enumerate(val):
            if max_node < valj:
                max_node = valj

    weight = temp_weight.split(",")
    for i,val in enumerate(weight):
        weight[i] = int(val)
    print("max_node=\t", max_node)
    print("n=\t", n)
    print("nodes=\t", nodes)
    print("weight=\t", weight)
    file.close()

def adjancy_matrix(nodes,max_node): # функция для матрицы смежности
    global result_adjancy_matrix
    print("Матрица смежности")
    adj = [[0 for i in range(max_node)] for j in range(max_node)]
    for i,val in enumerate(nodes):
        adj[val[0]-1][val[1]-1]=1
        if UNORIN_ORIENT == 0:
            adj[val[1]-1][val[0]-1]=1
    for i in range(max_node):
        print(adj[i])
    print()
    result_adjancy_matrix = adj
def incidency_matrix(nodes,max_nodes, UNORIN_ORIENT,root):
    global result_incidency_matrix
    print("Матрица инцидентности")
    if UNORIN_ORIENT == 0:
        inc = [[0 for i in range(len(nodes))] for j in range(max_nodes)]
        for i,val in enumerate(nodes):
            inc[val[0]-1][i] = 1
            inc[val[1]-1][i] = 1
    else:
        inc = [[0 for i in range(len(nodes))] for j in range(max_nodes)]
        for i,val in enumerate(nodes):
            inc[val[0]-1][i] = 1
            inc[val[1]-1][i] = -1
    for i in range(max_nodes):
        print(inc[i])
    print()
    result_incidency_matrix = inc


def adjancy_for_deikstra(nodes, weight, max_node):
    n = len(nodes)
    m = 2
    array_edge = [[0 for i in range(m)] for j in range(n)]
    array_edjancy = [[0 for i in range(max_node)] for j in range(max_node)]
    for i in range(n):
        for j in range(m):
            array_edge[i][j] = nodes[i][j]
    for i in range(max_node):
        for j in range(max_node):
            array_edjancy[i][j] = 0
    for i in range(n):
        x = array_edge[i][0]
        y = array_edge[i][1]
        array_edjancy[x-1][y-1] = weight[i]
        array_edjancy[y-1][x-1] = weight[i]
    return array_edjancy
def deikstra(nodes,weight,max_node):
    adjacencyMatrix = adjancy_for_deikstra(nodes, weight, max_node)
    for start in range(max_node):
        distance = [inf for i in range(max_node)]
        visited = [0 for i in range(max_node)]
        distance[start] = 0
        for i in range(max_node):
            v = -1
            for j in range(max_node):
                if visited[j] == 0 and (v == -1 or distance[j] < distance[v]):
                    v = j
            if distance[v] == inf:
                break
            visited[v] = 1
            for j in range(max_node):
                if adjacencyMatrix[v][j] != 0:
                    to = j
                    size = adjacencyMatrix[v][j]
                    if distance[v] + size < distance[to]:
                        distance[to] = distance[v] + size
        print("vertex\tdistance")
        for i in range(max_node):
            print(i+1,"\t",distance[i])


def connected_components(adjacency_matrix):
    visited = [False] * len(adjacency_matrix)
    count = 0
    for i in range(len(adjacency_matrix)):
        if not visited[i]:
            dfs(adjacency_matrix, i, visited)
            count += 1
    return count
def dfs(adjacency_matrix, i, visited):
    visited[i] = True
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1 and not visited[j]:
            dfs(adjacency_matrix, j, visited)

def euleran_circle(adjacencyMatrix):
    max_node = len(adjacencyMatrix)
    print("conCompDFS(adjacencyMatrix)", connected_components(adjacencyMatrix))
    if (connected_components(adjacencyMatrix) != 1):
        print("граф не является Эйлеровым")
        mb.showerror(" ","граф не является Эйлеровым")
    degrees = [0] * max_node
    for i in range(max_node):
        for j in range(max_node):
            if (adjacencyMatrix[i][j]):
                degrees[i] += 1
    for i in range(max_node):
        if (degrees[i] % 2 != 0):
            print("граф не является Эйлеровым")
            mb.showerror(" ","граф не является Эйлеровым")
    path = []
    s = []
    poz = 0
    s.append(poz)
    while s:
        poz = s[-1]
        temp = False
        for i in range(max_node):
            if (adjacencyMatrix[poz][i]):
                adjacencyMatrix[poz][i] = 0
                adjacencyMatrix[i][poz] = 0
                s.append(i)
                temp = True
                break
        if not temp:
            path.append((poz+1))
            s.pop()
    print("Euleran circle:\t",path)


def radiusGraph(nodes,edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print("радиус графа\t",nx.radius(G))
def diameterGraph(nodes,edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print("диаметр графа\t",nx.diameter(G))
def centerGraph(nodes,edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    print("центр графа\t",nx.center(G))



def main():
    button_vertex = tk.Button(application, text="add vertex", command=draw_vertixes,width=15, height=2)
    button_stop_add_vertex = tk.Button(application, text="stop add and\n delete vertex", command=stop_add_vertex,width=15, height=2)
    button_green = tk.Button(application, text="green", command=lambda: color_vertex("green"),width=15, height=2, bg="green")
    button_blue = tk.Button(application, text="blue", command=lambda: color_vertex("blue"),width=15, height=2, bg="blue")
    button_yellow = tk.Button(application, text="yellow", command=lambda: color_vertex("yellow"),width=15, height=2, bg="yellow")

    button_name_graph = tk.Button(application, text="name graph", command=graph_name,width=15, height=2)
    button_name_vertex = tk.Button(application, text="name vertex", command=NAME_VERTEX,width=15, height=2)
    button_delete_vertex = tk.Button(application, text="delete vertex", command=delete_vertex,width=15, height=2)
    button_rename_vertex = tk.Button(application, text="rename vertex", command=rename_vertex,width=15, height=2)
    button_draw_line_between_vertex = tk.Button(application, text="draw unoriented_line\n between vertex",\
         command=draw_unoriented_line_between_vertex,width=15, height=2)
    button_draw_oriented_line_between_vertex = tk.Button(application, text="draw oriented\n  between vertex",\
         command=draw_oriented_line_between_vertex,width=15, height=2)
    button_move_vertex_with_line = tk.Button(application, text="move vertex \nwith line", command=move_vertex_and_line,width=15, height=2)
    button_delete_unoriented_line= tk.Button(application, text="delete unoriented\n line", command=delete_unoriented_line,width=15, height=2)
    button_delete_oriented_line= tk.Button(application, text="delete oriented\n line", command=delete_oriented_line,width=15, height=2)
    button_algorithm= tk.Button(application, text="algorithm", command=algorithm,width=15, height=2)
    button_quit2 = tk.Button(application, text="quit", command=application.destroy,width=15, height=2)
    button_weight_line = tk.Button(application, text="input weight\n line", command=input_weight,width=15, height=2)
    button_draw_weight_line = tk.Button(application, text="draw weight\n line", command=draw_weight_line,width=15, height=2)
    button_delete_weight_line = tk.Button(application, text="delete weight\n line", command=delete_weight_line,width=15, height=2)
    button_change_color_vertex = tk.Button(application, text="change color\n vertex", command=change_color_vertex,width=15, height=2)

    button_name_vertex.grid(row=0, column=0)
    button_stop_add_vertex.grid(row=1, column=0)
    button_green.grid(row=0, column=1)
    button_blue.grid(row=0, column=2)
    button_yellow.grid(row=0, column=3)
    button_vertex.grid(row=0, column=4)
    button_draw_line_between_vertex.grid(row=1, column=4)
    button_delete_unoriented_line.grid(row=1,column=5)
    button_delete_oriented_line.grid(row=2,column=5)
    button_draw_oriented_line_between_vertex.grid(row=2, column=4)
    button_delete_vertex.grid(row=0, column=5)
    button_rename_vertex.grid(row=0, column=6)
    button_move_vertex_with_line.grid(row=1, column=6)
    button_name_graph.grid(row=2, column=0)
    button_algorithm.grid(row=2, column=1)
    button_weight_line.grid(row=1, column=1)
    button_draw_weight_line.grid(row=1, column=2)
    button_delete_weight_line.grid(row=1, column=3)
    button_quit2.grid(row=2, column=6)
    button_change_color_vertex.grid(row=2, column=2)
    application.mainloop()


if __name__ == "__main__":
    main()

