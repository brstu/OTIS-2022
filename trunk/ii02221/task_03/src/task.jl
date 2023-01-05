from tkinter import *
import random
from tkinter.messagebox import showerror, showwarning, showinfo
import numpy as np
from idlelib.tooltip import Hovertip
import time

canvas_width = 1280
canvas_height = 800
brush_size = 3
color = "blue"
sel_vert = None
vert_name = []  # List of vertex names
edges = []
vertex = []  # Global variables
x_click = 300  # Global variables
x_move = []  # List of x coordinates
y_click = 300  # Global variables
y_move = []  # List of y coordinates
vertex_count = 0  # Vertex counter
edge_count = 0

Edges=[]
edge_x1=0 
edge_x2=0
edge_y1=0
edge_y2=0
ver_edge_1=None
ver_edge_2=None

root = Tk()
root.geometry('1280x800+300+100')
root.title('OTIS-3')
#root.after(20000, root.destroy)## remove

class Vertex:
    def __init__(self, canvas, color,name):
        global x_click, y_click,  vertex_count
        self.vertex_count = vertex_count
        self.vert_name = name
        self.canvas = canvas
        self.color = color
        self.x = x_click
        self.y = y_click
        self.id_vert = canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=color, width=2)
        self.id_txt = self.canvas.create_text(self.x, self.y, anchor='center', text=self.vert_name,fill="green")
        canvas.unbind("<Button-1>")

##  store names and change coordinates based on them 
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
        

# Creating vertices
def create_vertex(root,name):
    global  vertex_count, color, vertex
    if name == '': showerror("error" ,message=' Enter a name ')
    elif  name in vert_name: showerror("error" ,message=' Such a name already exists ')
    else:
        print("before the creation cycle",vertex)
        vertex_count+=1
        print("before creation",vertex)
        vertex.append(Vertex(canvas, color,name))
        print("after creation",vertex)
        root.destroy()

def menu_create_vertex():
    new_window=Toplevel()
    new_window["bg"]="black"
    new_window.title("Creating a vertex")
    new_window.geometry('200x100+600+300')
    entry = Entry(new_window, bg='green')  ##  input line
    btn1 = Button(new_window,text='Input', bg='green',width=15, comman=lambda:create_vertex(new_window,entry.get()))
    entry.pack()
    btn1.pack()

def exit():
    showerror( message=' Рофлан ')##about the infa error
    root.destroy()

 #     position   point move_vertex Moving vertices
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
            move_label.config(text="The vertex is being moved : "+str(sel_vert.vert_name))
            print(sel_vert.vert_name, x_click, y_click )

def move_vertex(event):
    global edges
    y_click=event.y
    x_click=event.x
    sel_vert.x = x_click
    sel_vert.y = y_click
    canvas.coords(sel_vert.id_vert, event.x - 20, event.y - 20, event.x + 20, event.y + 20)# moving a vertex
    canvas.coords(sel_vert.id_txt, event.x, event.y)# moving the vertex name
    for edg in edges:
        if sel_vert.vert_name == edg.ver_edge_1:
            edg.edge_x1=sel_vert.x
            edg.edge_y1=sel_vert.y
            canvas.coords(edg.id_line,line_intersect_circle( edg.edge_x1, edg.edge_y1,edg.edge_x2,edg.edge_y2))
        else :
            if sel_vert.vert_name == edg.ver_edge_2:
                edg.edge_x2=sel_vert.x
                edg.edge_y2=sel_vert.y
                canvas.coords(edg.id_line,line_intersect_circle( edg.edge_x1, edg.edge_y1,edg.edge_x2,edg.edge_y2))

# color changing function
def color_change(new_color):
    global color
    color = new_color 
    Cur_color.config( text='Current color: '+ str(color)) #config  to change an element
    Cur_color_block.config(bg=color)

def nameGraf():
    new_window = Toplevel() 
    new_window.title("Change Name graf")
    new_window.geometry('250x150+600+300')
    title=Label(new_window,text='Choose a name')
    title.pack()
    NameInput = Entry(new_window, bg='green',font=30)
    NameInput.pack()
    btn =Button(new_window, text="Input",width =30,command= lambda:[Name_graf.config(text='Graph: '+str(NameInput.get())),new_window.destroy()])
    btn.pack()
    
    

def Choose_color():
    global color
    new_window=Toplevel()
    new_window.title("Change color")
    new_window.geometry('250x50+600+300')
    new_window['bg']='black'
    red_btn = Button(new_window, text= "Красный ", width=10,bg="red",fg="white", command=lambda:color_change("red"))
    pink_btn = Button(new_window, text= "Розовый", width=10,bg="pink",fg="white", command=lambda:color_change("pink"))
    blue_btn = Button(new_window, text= "Синий", width=10,bg="blue",fg="white", command=lambda:color_change("blue"))
    violet_btn = Button(new_window, text= "Фиолетовый", width=10,bg="violet",fg="white", command=lambda:color_change("violet"))
    red_btn.grid(row=0, column=1)
    pink_btn.grid(row=0, column=2)
    blue_btn.grid(row=0, column=3)
    violet_btn.grid(row=1, column=1)
    

def rename():
    new_window = Toplevel() 
    new_window.title("Change Name vertex")
    new_window.geometry('250x150+600+300')
    title=Label(new_window,text='Vertex name')
    title.pack()
    NameInput = Entry(new_window, bg='green',font=30)
    NameInput.pack()
    title2=Label(new_window,text='Rename')
    title2.pack()
    Name2Input = Entry(new_window, bg='green',font=30)
    Name2Input.pack()
    btn =Button(new_window, text="Input",width =30,command= lambda:check_name(NameInput.get(),Name2Input.get(),new_window))
    btn.pack()

def check_name(name, name2,root):
    global new_window,vertex,edges
    count=0
    if name == name2:showerror("Invalid name","The new name must not match the old one") 
    for vert in vertex:
        if vert.vert_name == name:
            count+=1
            vert.vert_name=name2
            canvas.itemconfigure(vert.id_txt, text=name2)
            for edg in edges:
                if edg.ver_edge_1==name: edg.ver_edge_1=name2;break
                if edg.ver_edge_2==name: edg.ver_edge_2=name2;break
    if count==0:showerror("error", " There is no such vertex")
    root.destroy()

#Creating edges

def check_name_peaks(name1, name2,root):
    global ver_edge_1,ver_edge_2,edge_count,edges
    count=0
    count2=0
    if name1=='' or name2 == '':
        showerror("error","Enter a name") 
        return
    if name1 == name2:showerror("Invalid name","The vertices must not match") 
    for vert in vertex:
        if vert.vert_name == name1:
            count+=1
            ver_edge_1=vert.vert_name
            id1=vert
    for vert in vertex:
        if vert.vert_name == name2:
            count2+=1
            ver_edge_2=vert.vert_name
            id2=vert
    if count2==0 or count==0:showerror("error", " The entered vertex does not exist"); root.destroy()
    
    if count!=0 and count2!=0:
        for edg in edges:
            if (edg.ver_edge_1 == ver_edge_2 or  edg.ver_edge_1 == ver_edge_1) and  (edg.ver_edge_2 == ver_edge_2 or  edg.ver_edge_2 == ver_edge_1):
                showerror("error", " Such an edge already exists ")
                return
        edge_count +=1
        edges.append(Edge(canvas,id1.x,id1.y,id2.x,id2.y))
    root.destroy()

def line_intersect_circle(x1, y1, x2, y2):
    main_gipotenuza = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenuza - 20) * main_dx / main_gipotenuza
    dy = (main_gipotenuza - 20) * main_dy / main_gipotenuza

    return x2 - dx, y2 - dy, x1 + dx, y1 + dy

def menu_edge():
    new_window = Toplevel() 
    new_window.title("Menu edge")
    new_window.geometry('250x150+600+300')
    title = Label(new_window,text = 'Choose which vertices to connect')
    title.pack()
    title1 = Label(new_window,text = ' The first vertex ')
    title1.pack()
    Input_1 =Entry(new_window, bg='green',font=30)
    Input_1.pack()
    title2 = Label(new_window,text = ' The second vertex ')
    title2.pack()
    Input_2 =Entry(new_window, bg='green',font=30)
    Input_2.pack()
    btn=Button(new_window,text='Input',command=lambda:check_name_peaks(Input_1.get(),Input_2.get(),new_window))
    btn.pack()

def menu_delete_vert():
    new_window=Toplevel()
    new_window.title("Menu delete vert")
    new_window.geometry('250x150+600+300')
    title = Label(new_window,text = 'Choose which vertex to delete')
    title.pack()
    entry = Entry(new_window, bg="green")
    entry.pack()
    btn = Button (new_window, text="Input",width=15, command=lambda:cheak_delete_ver(entry.get(),new_window))
    btn.pack()

def cheak_delete_ver(name,root):
    global vertex,sel_vert,vertex_count,edge_count,edges
    count=0
    del_list=[]
    if name == '':
        showerror("error","Enter a name") 
        return        
    for ver in vertex:
        if ver.vert_name == name:
            for edg in edges:
                if edg.ver_edge_1  == name or edg.ver_edge_2 == name :
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
    if count == 0: showerror(" error "," There is no such vertex ")
    root.destroy()

def menu_delete_peaks():
    new_window = Toplevel() 
    new_window.title("Menu Delete of Peaks")
    new_window.geometry('250x150+600+300')
    title = Label(new_window,text = 'Choose between which vertices to remove an edge from')
    title.pack()
    title1 = Label(new_window,text = ' The first vertex ')
    title1.pack()
    Input_1 =Entry(new_window, bg='green',font=30)
    Input_1.pack()
    title2 = Label(new_window,text = ' The second vertex ')
    title2.pack()
    Input_2 =Entry(new_window, bg='green',font=30)
    Input_2.pack()
    btn=Button(new_window,text='Ввод',command=lambda:check_delete_name_peaks(Input_1.get(),Input_2.get(),new_window))
    btn.pack()

def check_delete_name_peaks(name1, name2,root):
    global ver_edge_1,ver_edge_2,edge_count,edges
    count=0
    count2=0
    count3=0
    if name1=='' or name2 == '':
        showerror("error","Enter a name") 
        return
    if name1 == name2:showerror("Invalid name","The vertices must not match") 
    for vert in vertex:
        if vert.vert_name == name1:
            count+=1
            ver_edge_1=vert.vert_name
            break
    for vert in vertex:
        if vert.vert_name == name2:
            count2+=1
            ver_edge_2=vert.vert_name
            break
    if count2==0 or count==0:showerror("error", " The entered vertex does not exist"); root.destroy()
    
    if count!=0 and count2!=0:
        for edg in edges:
            if (edg.ver_edge_1 == ver_edge_2 or  edg.ver_edge_1 == ver_edge_1) and  (edg.ver_edge_2 == ver_edge_2 or  edg.ver_edge_2 == ver_edge_1):
                canvas.delete(edg.id_line)
                edges.remove(edg)
                edge_count-=1
                count3=1
    if count3==0: showerror("error", " There was no edge between the vertices ")
    root.destroy()    

def create_matrix_adjacency():
    global  edges,vertex_count,vertex
    matrix_adjacency = [[0 for i in range(vertex_count)]for i in range(vertex_count)]

    for edge in edges:
        index1=0
        index2=0       
        for ver in vertex:
            if ver.vert_name == edge.ver_edge_1:index1=vertex.index(ver)
            if ver.vert_name == edge.ver_edge_2:index2=vertex.index(ver)
            if index2!=0 and index1!=0: continue
        matrix_adjacency [index1] [index2]=1
        matrix_adjacency [index2] [index1]=1
 
    window = Tk()
    window.title("Adjacency matrix")
    window.geometry("400x400+0+0")
    for i in range(vertex_count):
        for j in range(vertex_count):
            Label(window, text=matrix_adjacency[i][j], font="Arial 10", width=5, height=2,
                  borderwidth=1,relief="solid").grid(row=i, column=j)
    window.mainloop()
#   WORKING WITH THE LEFT SIDE 


canvas=Canvas(root ,width =1000,height=800 , bg='#0056ff')

canvas.place(x=350)

frame = Frame(root, bg='red')
frame.place( width=350 , relheight=1)

title = Label(frame, text='Menu', bg='#00ffff', font=40)
title.pack()

Name_graf = Label(frame, text='Name of the graph', bg='#00ffff', font=40)
Name_graf.pack()

Cur_color=Label(frame, text='Current color: '+ str(color), bg='green', font=40)
Cur_color.place(x=45,y=50,height=30,width=250)
outline=Label(frame, bg='#CCFFCC')
outline.place(x=8,y=48,height=34,width=34)
Cur_color_block=Label(frame, bg=color)
Cur_color_block.place(x=10,y=50,height=30,width=30)


canvas.bind('<2>', position)
canvas.bind('<3>', point)

move_label= Label(frame, text = "The vertex is being moved : ")
move_label.place(x=34,y=100,height=20)
outline2=Label(frame, bg='#CCFFCC')
outline2.place(x=8,y=98,height=24,width=24)
info_move= Label(frame, text = "?", bg="#006699")
info_move.place(x=10,y=100,width=20,height=20)
Hovertip(info_move, "To select a vertex to move, press the PCM, then to move it, hold the LMB", hover_delay=100)

btn1  = Button(frame,text='Name of the graph', width=20, command=nameGraf)
btn2  = Button(frame,text='Color selection', width=20, command=Choose_color)
btn3  = Button(frame,text='Creating a Vertex', width=20, command=menu_create_vertex)
btn4  = Button(frame,text='Creating an Edge', width=20, command=menu_edge)
btn5  = Button(frame,text='Rename a vertex', width=20, command=rename)
btn6  = Button(frame,text='Delete a vertex', width=20, command=menu_delete_vert)
btn7  = Button(frame,text='Remove an edge', width=20, command=menu_delete_peaks)
btn8  = Button(frame,text='Adjacency Matrix', width=20, command=create_matrix_adjacency)
btn9  = Button(frame,text='The incidence matrix', width=20)
btn10 = Button(frame, text=' Exit ', command=exit)

# canvas.create_line(15, 25, 200, 25,width=5,fill="black")

btn1.place(x=10,y=140)
btn2.place(x=10,y=170)
btn3.place(x=10,y=200)
btn4.place(x=10,y=230)
btn5.place(x=10,y=260)
btn6.place(x=10,y=290)
btn7.place(x=10,y=320)
btn8.place(x=10,y=350)
btn9.place(x=10,y=380)
btn10.place(x=10,y=410)

root.mainloop()