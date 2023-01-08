from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import numpy as np
from idlelib.tooltip import Hovertip
import colour
# Граф — математическая абстракция реальной системы любой природы,
# объекты которой обладают парными связями. 
# Граф как математический объект есть совокупность двух множеств — множества самих объектов,
# называемого множеством вершин,
# и множества их парных связей, называемого множеством рёбер. Элемент множества рёбер есть пара элементов множества вершин.
c_w = 1280
c_h = 800
brush_size = 3
color = "blue"
sel_vert = None
vert_n = []  
edges = []
vertex = []  
x_click = 300 
x_move = []  
y_click = 300 
y_move = []  
vertex_count = 0  
edge_count = 0

Edges=[]
edge_x1=0 
edge_x2=0
edge_y1=0
edge_y2=0
ver_edge_1=None
ver_edge_2=None

window = Tk()
window.geometry('1280x800+300+100')
window.title('OTIS-3')
window. resizable(False, False)

class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.arcs = []
        self.d = {'': []}
        self.oval = None
        self.text = None
        self.canvases = []

    def __str__(self):
        return f"Кол-во вершин: {len(self.nodes)}\n" \
               f"Кол-во дуг: {len(self.arcs)}\n" \
               f"Матрица инцидентности: {self.count_incidence_matrix()}\n" \
               f"Матрица смежности: {self.count_adjacency_matrix()}"

class Plt:
    entry_color = Entry()
    label_color = Label()
    color = clr

class Vertex:
    def __init__(self, canvas, color,n):
        global x_click, y_click,  vertex_count
        self.vertex_count = vertex_count
        self.vert_n = n
        self.canvas = canvas
        self.color = color
        self.x = x_click
        self.y = y_click
        self.id_vert = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=color, width=2)
        self.id_txt = self.canvas.create_text(self.x, self.y, anchor='center', text=self.vert_n,fill="white")
        canvas.unbind("<Button-1>")

##  хранить именна и поим менять координаты 
class Edge:
    def __init__(self, canvas,x1,y1,x2,y2):
        global ver_edge_1,ver_edge_2
        self.edge_x1=x1
        self.edge_x2=x2
        self.edge_y1=y1
        self.edge_y2=y2
        self.ver_edge_1=ver_edge_1
        self.ver_edge_2=ver_edge_2
        self.width=5
        self.canvas = canvas
        self.color = 'black'
        self.id_line=self.canvas.create_line(line_intersect_circle(self.edge_x1,self.edge_y1 ,self.edge_x2,self.edge_y2),width=self.width,fill="black")



def add_vert(window,n):
    global  vertex_count, color, vertex
    if n == '': showerror("Ошибка" ,message=' Введите имя ')
    elif  n in vert_n: showerror("Ошибка" ,message=' Такое имя уже существует ')
    else:
        print("до цикла создания",vertex)
        vertex_count+=1
        print("до создания",vertex)
        vertex.append(Vertex(canvas, color,n))
        print("после создания",vertex)

def menu_add_vert():
    new=Toplevel()
    new["bg"]="black"
    new.title("Создание вершины")
    new.geometry('200x100+600+300')
    entry = Entry(new, bg='white')  ##  строка ввода
    button1 = Button(new,text='Ввод', bg='white',width=15, comman=lambda:add_vert(new,entry.get()))
    entry.pack()
    button1.pack()

def exit():
    window.destroy()

 #     position   point move_vertex Перемещение вершин
def position(event):
    global y_click, x_click
    y_click=event.y
    x_click=event.x
    print("x -",x_click, " y -",y_click)

def point(event):
    global sel_vert
    y_click=event.y
    x_click=event.x
    for vert in vertex:
        if y_click+20>=vert.y >= y_click-20 and x_click+20 >= vert.x >= x_click-20:
            sel_vert = vert
            canvas.bind("<B1-Motion>", move_vertex)
            move_label.config(text="Перемещается вершина : "+str(sel_vert.vert_n))
            print(sel_vert.vert_n, x_click, y_click )

def move_vertex(event):
    global edges
    y_click=event.y
    x_click=event.x
    sel_vert.x = x_click
    sel_vert.y = y_click
    canvas.coords(sel_vert.id_vert, event.x - 20, event.y - 20, event.x + 20, event.y + 20)# перемещение вершины
    canvas.coords(sel_vert.id_txt, event.x, event.y)# перемещение имени вершины
    for edg in edges:
        if sel_vert.vert_n == edg.ver_edge_1:
            edg.edge_x1=sel_vert.x
            edg.edge_y1=sel_vert.y
            canvas.coords(edg.id_line,line_intersect_circle( edg.edge_x1, edg.edge_y1,edg.edge_x2,edg.edge_y2))
        else :
            if sel_vert.vert_n == edg.ver_edge_2:
                edg.edge_x2=sel_vert.x
                edg.edge_y2=sel_vert.y
                canvas.coords(edg.id_line,line_intersect_circle( edg.edge_x1, edg.edge_y1,edg.edge_x2,edg.edge_y2))

# функция  изменения цвета
def color_change(new_color):
    global color
    color = new_color 
    Cur_color.config( text='Текущий цвет: '+ str(color)) #config  для изменение элемента
    Cur_color_block.config(bg=color)

def n_g():
    new = Toplevel() 
    new.title("Change n graf")
    new.geometry('250x150+600+300')
    title=Label(new,text='Выберите имя')
    title.pack()
    nInput = Entry(new, bg='white',font=30)
    nInput.pack()
    btn =Button(new, text="Ввод",width =30,command= lambda:[n_graf.config(text='Граф: '+str(nInput.get())),new.destroy()])
    btn.pack()



def Choose_color():
    global color
    new=Toplevel()
    new.title("Change color")
    new.geometry('250x50+600+300')
    new['bg']='black'
    red_btn = Button(new, text= "Красный ", width=10,bg="red",fg="white", command=lambda:color_change("red"))
    black_btn = Button(new, text= "Черный", width=10,bg="black",fg="white", command=lambda:color_change("black"))
    blue_btn = Button(new, text= "Синий", width=10,bg="blue",fg="white", command=lambda:color_change("blue"))
    green_btn = Button(new, text= "Зеленый", width=10,bg="green",fg="white", command=lambda:color_change("green"))
    red_btn.grid(row=0, column=1)
    black_btn.grid(row=0, column=2)
    blue_btn.grid(row=0, column=3)
    green_btn.grid(row=1, column=1)


def ren():
    new = Toplevel() 
    new.title("Change n vertex")
    new.geometry('250x150+600+300')
    title=Label(new,text='Имя вершины')
    title.pack()
    nInput = Entry(new, bg='white',font=30)
    nInput.pack()
    title2=Label(new,text='Переименовать')
    title2.pack()
    n2Input = Entry(new, bg='white',font=30)
    n2Input.pack()
    btn =Button(new, text="Ввод",width =30,command= lambda:check_n(nInput.get(),n2Input.get(),new))
    btn.pack()

def check_n(n, n2,window):
    global new,vertex,edges
    count=0
    if n == n2:showerror("Неверное имя","Новое имя не должно совпадать со старым") 
    for vert in vertex:
        if vert.vert_n == n:
            count+=1
            vert.vert_n=n2
            canvas.itemconfigure(vert.id_txt, text=n2)
            for edg in edges:
                if edg.ver_edge_1==n: edg.ver_edge_1=n2;break
                if edg.ver_edge_2==n: edg.ver_edge_2=n2;break

#Создание ребер

def check_n_peaks(n1, n2,window):
    global ver_edge_1,ver_edge_2,edge_count,edges
    count=0
    count2=0
    if n1=='' or n2 == '':
        showerror("error","enter name") 
        return
    if n1 == n2:showerror("vet not exist") 
    for vert in vertex:
        if vert.vert_n == n1:
            count+=1
            ver_edge_1=vert.vert_n
            id1=vert
    for vert in vertex:
        if vert.vert_n == n2:
            count2+=1
            ver_edge_2=vert.vert_n
            id2=vert

def line_intersect_circle(x1, y1, x2, y2):
    main_gipotenuza = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenuza - 20) * main_dx / main_gipotenuza
    dy = (main_gipotenuza - 20) * main_dy / main_gipotenuza

    return x2 - dx, y2 - dy, x1 + dx, y1 + dy

def menu_edge():
    new = Toplevel() 
    new.title("Menu edge")
    new.geometry('250x150+600+300')
    title = Label(new,text = 'Выберите какие вершины соединить')
    title.pack()
    title1 = Label(new,text = ' Первая вершина ')
    title1.pack()
    Input_1 =Entry(new, bg='white',font=30)
    Input_1.pack()
    title2 = Label(new,text = ' Вторая вершина ')
    title2.pack()
    Input_2 =Entry(new, bg='white',font=30)
    Input_2.pack()
    btn=Button(new,text='Ввод',command=lambda:check_n_peaks(Input_1.get(),Input_2.get(),new))
    btn.pack()

def menu_delete_vert():
    new=Toplevel()
    new.title("Menu delete vert")
    new.geometry('250x150+600+300')
    title = Label(new,text = 'Выберите какую вершину удалить')
    title.pack()
    entry = Entry(new, bg="white")
    entry.pack()
    btn = Button (new, text="Ввод",width=15, command=lambda:cheak_delete_ver(entry.get(),new))
    btn.pack()

def cheak_delete_ver(n,window):
    global vertex,sel_vert,vertex_count,edge_count,edges
    count=0
    del_list=[]
    if n == '':
        showerror("Ошибка","Введите имя") 
        return        
    for ver in vertex:
        if ver.vert_n == n:
            for edg in edges:
                if edg.ver_edge_1  == n or edg.ver_edge_2 == n :
                    canvas.delete(edg.id_line)
                    del_list.append(edg)
                    edge_count-=1 
            for list in del_list:
                edges.remove(list)
            del_list.clear()
            count+=1
            sel_vert= ver
            canvas.delete(sel_vert.id_vert)
            canvas.delete(sel_vert.id_txt)
            vertex.remove(ver)
            vertex_count-=1
            print(vertex)

def menu_delete_peaks():
    new = Toplevel() 
    new.title("Menu Delete of Peaks")
    new.geometry('250x150+600+300')
    title = Label(new,text = 'Выберите между какими вершины удалить ребро')
    title.pack()
    title1 = Label(new,text = ' Первая вершина ')
    title1.pack()
    Input_1 =Entry(new, bg='white',font=30)
    Input_1.pack()
    title2 = Label(new,text = ' Вторая вершина ')
    title2.pack()
    Input_2 =Entry(new, bg='white',font=30)
    Input_2.pack()
    btn=Button(new,text='Ввод',command=lambda:check_n(Input_1.get(),Input_2.get(),new))
    btn.pack()

def check_n(n1, n2,window):
    global ver_edge_1,ver_edge_2,edge_count,edges
    count=0
    count2=0
    count3=0
    if n1=='' or n2 == '':
        showerror("Ошибка","Введите имя") 
        return
    if n1 == n2:showerror("Неверное имя","Вершины не должны совпадать") 
    for vert in vertex:
        if vert.vert_n == n1:
            count+=1
            ver_edge_1=vert.vert_n
            break
    for vert in vertex:
        if vert.vert_n == n2:
            count2+=1
            ver_edge_2=vert.vert_n
            break
def create_matrix_adjacency():
    # Матрица смежности — один из способов 
    # представления графа в виде матрицы.
    global  edges,vertex_count,vertex
    matrix_adjacency = [[0 for i in range(vertex_count)]for i in range(vertex_count)]

    for edge in edges:
        index1=0
        index2=0       
        for ver in vertex:
            if ver.vert_n == edge.ver_edge_1:index1=vertex.index(ver)
            if ver.vert_n == edge.ver_edge_2:index2=vertex.index(ver)
            if index2!=0 and index1!=0: continue
        matrix_adjacency [index1] [index2]=1
        matrix_adjacency [index2] [index1]=1

    window = Tk()
    window.title("Матрица смежности")
    window.geometry("400x400+0+0")
    for i in range(vertex_count):
        for j in range(vertex_count):
            Label(window, text=matrix_adjacency[i][j], font="Arial 10", width=5, height=2,
                  borderwidth=1,relief="solid").grid(row=i, column=j)
    window.mainloop()
#   РАБОТА С ЛЕВОЙ ЧАСТЬЮ 


canvas=Canvas(window ,width =1000,height=800 , bg='#00ffff')

canvas.place(x=350)

frame = Frame(window, bg='red')
frame.place( width=350 , relheight=1)

title = Label(frame, text='Menu', bg='#00ffff', font=40)
title.pack()

n_graf = Label(frame, text='Имя графа', bg='#00ffff', font=40)
n_graf.pack()

Cur_color=Label(frame, text='Текущий цвет: '+ str(color), bg='white', font=40)
Cur_color.place(x=45,y=50,height=30,width=250)
outline=Label(frame, bg='#CCFFCC')
outline.place(x=8,y=48,height=34,width=34)
Cur_color_block=Label(frame, bg=color)
Cur_color_block.place(x=10,y=50,height=30,width=30)


canvas.bind('<2>', position)
canvas.bind('<3>', point)

move_label= Label(frame, text = "Перемещается вершина : ")
move_label.place(x=34,y=100,height=20)
outline2=Label(frame, bg='#CCFFCC')
outline2.place(x=8,y=98,height=24,width=24)
info_move= Label(frame, text = "?", bg="#006699")
info_move.place(x=10,y=100,width=20,height=20)
Hovertip(info_move, "Что бы выбрать вершину для перемещения нажмите ПКМ, затем для ее перемещения зажмите ЛКМ", hover_delay=100)

button1  = Button(frame,text='Имя графа', width=20, command=n_g)
button2  = Button(frame,text='Выбор цвета', width=20, command=Choose_color)
button3  = Button(frame,text='Создание Вершину', width=20, command=menu_add_vert)
button4  = Button(frame,text='Создание Ребро', width=20, command=menu_edge)
button5  = Button(frame,text='Переименовать вершину', width=20, command=ren)
button6  = Button(frame,text='Удалить вершину', width=20, command=menu_delete_vert)
button7  = Button(frame,text='Удалить ребро', width=20, command=menu_delete_peaks)
button8  = Button(frame,text='Матрица Смежности', width=20, command=create_matrix_adjacency)
button9 = Button(frame, text=' Выход ', command=exit)

button1.place(x=10,y=140)
button2.place(x=10,y=170)
button3.place(x=10,y=200)
button4.place(x=10,y=230)
button5.place(x=10,y=260)
button6.place(x=10,y=290)
button7.place(x=10,y=320)
button8.place(x=10,y=350)
button9.place(x=10,y=380)

window.mainloop()