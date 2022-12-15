import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import networkx as nk
import csv
from random import SystemRandom
# Переменные
# Для всех элементов
NodeCount = 1
EdgeCounter, x1, y1, x2, y2 = 0, 0.0, 0.0, 0.0, 0.0
RgbNodes = {}
Nodes = {}
RgbNodesBord = {}
TextNodes = {}
TempItems = []
# Граф
Graph = 0
GraphName = ''

# Функции

def rgbtohex(r, g, b):
    if (r != '' and g != '' and b != '') and (0 <= int(r) <= 255) and (0 <= int(g) <= 255) and (0 <= int(b) <= 255):
        return f'#{int(r):02x}{int(g):02x}{int(b):02x}'
    else:
        return '#000000'
def reversergbtohex(r, g, b):
    if (r != '' and g != '' and b != '') and (0 <= int(r) <= 255) and (0 <= int(g) <= 255) and (0 <= int(b) <= 255):
        return f'#{abs(int(r) - 255):02x}{abs(int(g) - 255):02x}{abs(int(b) - 255):02x}'
    else:
        return '#000000'
def reversergb(r, g, b):
    if (r != '' and g != '' and b != '') and (0 <= int(r) <= 255) and (0 <= int(g) <= 255) and (0 <= int(b) <= 255):
        return abs(int(r) - 255), abs(int(g) - 255), abs(int(b) - 255)
    else:
        return 0, 0, 0
def reversehexrgb(hxlist):
    rgb = []
    for i in (1, 3, 5):
        decimal = int(hxlist[i:i + 2], 16)
        rgb.append(decimal)
    # print(rgb)
    return "#{:02X}{:02X}{:02X}".format(abs(rgb[0] - 255), abs(rgb[1] - 255), abs(rgb[2] - 255))


def TestConsole(event):
    print(f"Test Baby {event.x} {event.y}")
def RgbCanvasNodebg(event=0):
    CanvasNodeBord["bg"] = rgbtohex(EntryNodeBorderR.get(), EntryNodeBorderG.get(), EntryNodeBorderB.get())
    CanvasNode["bg"] = rgbtohex(EntryNodeR.get(), EntryNodeG.get(), EntryNodeB.get())
    CanvasNode.after(1, RgbCanvasNodebg)
def CanvasEdgebg(event=0):
    CanvasEdge["bg"] = rgbtohex(EntryEdgeR.get(), EntryEdgeG.get(), EntryEdgeB.get())
    CanvasEdge.after(1, CanvasEdgebg)
def EnterAndLeaveTextVericle(event=0):
    tags = Canvas.gettags("current")
    item = Canvas.find_withtag(f"Node&&{tags[1]}")
    # print(Canvas.itemcget(item,"fill"))
    Canvas.itemconfigure(item, fill=reversehexrgb(Canvas.itemcget(item, "fill")))


def InputNodesMode(event=0):
    app.config(menu='')
    Toplevel.deiconify()
    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши для создания вершины | Нажмите правую кнопку мыши для завершения (Не закрывайте меню цвета!!!)")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 1>", AddNodes)
    Canvas.bind("<Button 3>", StopInputModeNodes)
def AddNodes(event):
    global NodeCount, RgbNodes, RgbNodesBord, TextNodes

    RgbNodesBord[NodeCount] = [EntryNodeBorderR.get(), EntryNodeBorderG.get(), EntryNodeBorderB.get()]
    RgbNodes[NodeCount] = [EntryNodeR.get(), EntryNodeG.get(), EntryNodeB.get()]
    EntryNode = 0
    if EntryTextNode.get() == '':
        EntryNode = NodeCount
    else:
        EntryNode = EntryTextNode.get()

    Nodes[NodeCount] = Canvas.create_oval(event.x - 15, event.y - 15, event.x + 15, event.y + 15, width=1,
                                          outline=rgbtohex(EntryNodeBorderR.get(), EntryNodeBorderG.get(),
                                                           EntryNodeBorderB.get()),
                                          fill=rgbtohex(EntryNodeR.get(), EntryNodeG.get(), EntryNodeB.get()),
                                          tags=["Node", f"{EntryNode}"],
                                          activefill=reversergbtohex(EntryNodeR.get(), EntryNodeG.get(),
                                                                     EntryNodeB.get()))

    print(["Node", f"{EntryNode}"])
    TextNodes[NodeCount] = Canvas.create_text(event.x, event.y, text=f"{EntryNode}",
                                              fill=rgbtohex(EntryNodeBorderR.get(), EntryNodeBorderG.get(),
                                                            EntryNodeBorderB.get()),
                                              tags=["TextNode", f"{EntryNode}"])
    print(["TextNode", f"{EntryNode}"])
    Graph.add_node(f"{EntryNode}", text="SomeText")
    NodeCount += 1
def StopInputModeNodes(event=0):
    app.config(menu=main_menu)
    FrameEdge.pack_forget()
    Toplevel.withdraw()
    GraphAlgInfo.withdraw()
    ButtonChange.grid_forget()
    ButtonEdge.grid_forget()
    Canvas.tag_unbind("Node", "<Button 1>")
    Canvas.tag_unbind("TextNode", "<Button 1>")
    Canvas.tag_unbind("Edge", "<Button 1>")
    Canvas.tag_unbind("TextEdge", "<Button 1>")
    Canvas.unbind("<Button 1>")
    Canvas.unbind("<Button 3>")
    InfoLabel.pack_forget()
def DeleteNodeMode(event=0):
    app.config(menu='')
    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши для удаления вершины | Нажмите правую кнопку мыши для завершения")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 1>", DeleteNode)
    Canvas.bind("<Button 3>", StopInputModeNodes)
def DeleteNode(event=0):
    item = Canvas.gettags("current&&(Node||TextNode)")
    print(Canvas.gettags("Node||TextNode"))
    Canvas.delete(f"Node&&{item[1]}")
    Canvas.delete(f"TextNode&&{item[1]}")
    for i in Canvas.find_withtag("Node"):
        print(f"Edge&&{item[1]}-{Canvas.gettags(i)[1]}")
        Canvas.delete(f"Edge&&{item[1]}-{Canvas.gettags(i)[1]}")
        Canvas.delete(f"Edge&&{Canvas.gettags(i)[1]}-{item[1]}")
        Canvas.delete(f"TextEdge&&{item[1]}-{Canvas.gettags(i)[1]}")
        Canvas.delete(f"TextEdge&&{Canvas.gettags(i)[1]}-{item[1]}")
    Graph.remove_node(item[1])


NodeChange = 0
def ChangeNodeMode(event=0):
    app.config(menu='')
    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши для изменения вершины | Нажмите правую кнопку мыши для завершения")
    InfoLabel.pack(fill="x", expand=False, side="top")
    ButtonChange.grid(row=10, column=1, columnspan=2)
    Canvas.tag_bind("Node", "<Button 1>",ShowTLChange)
    Canvas.bind("<Button 3>", StopInputModeNodes)
def ShowTLChange(event=0):
    global NodeChange
    InfoLabel.configure(text="Нажмите правую кнопку мыши для отмены")
    Toplevel.deiconify()
    NodeChange = Canvas.find_withtag("current")
    Canvas.tag_unbind("Node", "<Button 1>")
def SumbitChangeNode(event=0):
    global NodeChange, Graph
    item = NodeChange
    Canvas.itemconfigure(item,
                         outline=rgbtohex(EntryNodeBorderR.get(), EntryNodeBorderG.get(), EntryNodeBorderB.get()),
                         fill=rgbtohex(EntryNodeR.get(), EntryNodeG.get(), EntryNodeB.get()),
                         activefill=reversergbtohex(EntryNodeR.get(), EntryNodeG.get(), EntryNodeB.get()))
    textitem = Canvas.find_withtag(f"TextNode&&{Canvas.gettags(item)[1]}")
    Canvas.itemconfigure(textitem,
                         fill=rgbtohex(EntryNodeBorderR.get(), EntryNodeBorderG.get(), EntryNodeBorderB.get()), )
    if EntryTextNode.get() != '':
        print("entryTextNode")
        text = Canvas.itemcget(textitem, "text")
        previosname=Canvas.gettags(item)[1]
        mapping = {text: EntryTextNode.get()}
        Graph = nk.relabel_nodes(Graph, mapping)
        Canvas.itemconfigure(textitem, text=f"{EntryTextNode.get()}", tags=['TextNode', f'{EntryTextNode.get()}'])
        Canvas.itemconfigure(item, tags=['Node', f'{EntryTextNode.get()}'])
        EdgesId=Canvas.find_withtag("Edge")
        for item in EdgesId:
            tags=Canvas.gettags(item)[1]
            if tags.find(previosname)!=-1:
                print('& ',tags.replace(previosname,f"{EntryTextNode.get()}"))
                tags2=tags.replace(previosname,f"{EntryTextNode.get()}")
                itemtext=Canvas.find_withtag(f"TextEdge&&{tags}")
                Canvas.itemconfigure(item,tags=['Edge',f'{tags2}'])
                Canvas.itemconfigure(itemtext,tags=['TextEdge',f'{tags2}'])
                print('*',Canvas.gettags(item))
                print('*',Canvas.gettags(itemtext))

    Toplevel.withdraw()
    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши для изменения вершины | Нажмите правую кнопку мыши для завершения")
    Canvas.tag_bind("Node", "<Button 1>", ChangeNodeMode)
def MoveNodeMode(event=0):
    app.config(menu='')
    InfoLabel.configure(text="Нажмите Левую кнопку мыши для удаления дуги | Нажмите правую кнопку мыши для завершения")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 1>", MoveNodeFirstPart)
    Canvas.bind("<Button 3>", StopInputModeNodes)


NodeOrText=0
def MoveNodeFirstPart(event=0):
    global NodeOrText
    NodeOrText=Canvas.find_withtag("current&&(Node||TextNode)")
    if not NodeOrText: return
    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши где она должна будет находится | Нажмите правую кнопку мыши для отмены")
    Canvas.bind("<Button 1>", MoveNodeSecondPart)
def MoveNodeSecondPart(event):
    global NodeOrText
    tagNOT=Canvas.gettags(NodeOrText)[1]
    print(Canvas.gettags(NodeOrText))
    Node=Canvas.find_withtag(f"Node&&{Canvas.gettags(NodeOrText)[1]}")
    Text=Canvas.find_withtag(f"TextNode&&{Canvas.gettags(NodeOrText)[1]}")
    Canvas.coords(Node,event.x-15,event.y-15,event.x+15,event.y+15)
    Canvas.coords(Text,event.x,event.y)
    Edgelist=Canvas.find_withtag("Edge")
    EdgeId=[Canvas.gettags(i)[1] for i in Edgelist]
    for i in EdgeId:
        if i.find(tagNOT)!=-1:
            x1=0
            y1=0
            x2=0
            y2=0
            if i.find(tagNOT)==0:
                x1,y1=Canvas.coords(Text)
                x2,y2=Canvas.coords(f"TextNode&&{i.split('-')[1]}")
            else:
                x2,y2=Canvas.coords(Text)
                x1,y1=Canvas.coords(f"TextNode&&{i.split('-')[0]}")
            if abs(y1 - y2) > abs(x1 - x2):
                if y1 < y2:
                    y1 += 15
                    y2 -= 15
                else:
                    y1 -= 15
                    y2 += 15
            else:
                if x1 < x2:
                    x1 += 15
                    x2 -= 15
                else:
                    x1 -= 15
                    x2 += 15
            Canvas.coords(f"Edge&&{i}",x1,y1,x2,y2)
            Canvas.coords(f"TextEdge&&{i}",(x1+x2)/2,(y1+y2)/2)

    InfoLabel.configure(
        text="Нажмите Левую кнопку мыши для выбора вершины | Нажмите правую кнопку мыши для отмены")
    Canvas.bind("<Button 1>", MoveNodeFirstPart)

def DeleteEdgeMode(event=0):
    app.config(menu='')
    InfoLabel.configure(text="Нажмите Левую кнопку мыши для удаления дуги | Нажмите правую кнопку мыши для завершения")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 1>", DeleteEdge)
    Canvas.bind("<Button 3>", StopInputModeNodes)
def DeleteEdge(event=0):
    item = Canvas.gettags("current&&(Edge||TextEdge)")
    Canvas.delete(f"TextEdge&&{item[1]}")
    Canvas.delete(f"Edge&&{item[1]}")
    Graph.remove_edge(item[1][0], item[1][2])
def AddEdgeFirstPart(event=0):
    global x1, y1, TempItems
    TempItems.clear()
    item = Canvas.gettags('current')
    coords = Canvas.coords('current')
    if item[0] == "Node":
        x1, y1 = coords[0] + 15, coords[1] + 15
    else:
        x1, y1 = coords[0], coords[1]
    TempItems.append(Canvas.find_withtag(f"Node&&{item[1]}"))
    TempItems.append(Canvas.find_withtag(f"TextNode&&{item[1]}"))
    InfoLabel.configure(text="Выберите Вторую Вершину: | Правая кнопкам мыши для отмены")
    Canvas.bind("<Button 1>", AddEdgeSecondPart)
def AddEdgeSecondPart(event=0):
    global x1, y1, x2, y2, TempItems
    item = Canvas.gettags('current')
    coords = Canvas.coords('current')
    TempItems.append(Canvas.find_withtag(f"Node&&{item[1]}"))
    TempItems.append(Canvas.find_withtag(f"TextNode&&{item[1]}"))
    if item[0] == "Node":
        x2, y2 = coords[0] + 15, coords[1] + 15
    else:
        x2, y2 = coords[0], coords[1]
    if abs(y1 - y2) > abs(x1 - x2):
        if y1 < y2:
            y1 += 15
            y2 -= 15
        else:
            y1 -= 15
            y2 += 15
    else:
        if x1 < x2:
            x1 += 15
            x2 -= 15
        else:
            x1 -= 15
            x2 += 15

    ves = 0
    try:
        ves = int(float(EntryEdge.get()))
    except ValueError:
        ves = 0
    anchor = ''
    if Canvas.find_withtag(
        f"{Canvas.gettags(TempItems[3])[1]}-{Canvas.gettags(TempItems[0])[1]}||{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}"):
        print("Попытка создания такой-же дуги")
    else:
        if RadioVar.get() == 0:
            Canvas.create_line(x1, y1, x2, y2, width=2, fill=rgbtohex(EntryEdgeR.get(),EntryEdgeG.get(),EntryEdgeB.get()),
                               tags=["Edge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}"], activewidth=5)
            print(["Edge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}", "Unorient"])
        elif RadioVar.get() == 1:
            Canvas.create_line(x1, y1, x2, y2, width=2, fill=rgbtohex(EntryEdgeR.get(),EntryEdgeG.get(),EntryEdgeB.get()),
                               tags=["Edge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}"], activewidth=5, arrow=ctk.LAST)
            print(["Edge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}", "Orient"])
        if abs(y1 - y2) > abs(x1 - x2):
            anchor = "ne"
        else:
            anchor = "sw"
        Canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{ves}", fill="Red", font='Helvetica 15 bold',
                           anchor=anchor, activefill="Green", \
                           tags=["TextEdge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}"])
        print(["TextEdge", f"{Canvas.gettags(TempItems[0])[1]}-{Canvas.gettags(TempItems[3])[1]}"])
        Graph.add_weighted_edges_from([(Canvas.gettags(TempItems[0])[1], Canvas.gettags(TempItems[3])[1], ves)])
    InfoLabel.configure(text="Выберите Первую Вершину:")
    Canvas.bind("<Button 1>", AddEdgeFirstPart)
def InputEdgeMode(event=0):
    app.config(menu='')
    FrameEdge.pack(fill="x", expand=False)
    InfoLabel.configure(text="Выберите Первую Вершину: | Правая кнопкам мыши для отмены")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 1>", AddEdgeFirstPart)
    Canvas.bind("<Button 3>", StopInputModeNodes)
def ChangeEdgeMode(event=0):
    app.config(menu='')
    ButtonEdge.grid(row=2, column=3, columnspan=3)
    InfoLabel.configure(text="Выберите Дугу: | Правая кнопкам мыши для отмены")
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.tag_bind("Edge","<Button 1>", ShowEdgeChange)
    Canvas.bind("<Button 3>", StopInputModeNodes)


EdgeChange=0
def ShowEdgeChange(event=0):
    global EdgeChange
    FrameEdge.pack(fill="x", expand=False)
    InfoLabel.configure(text="Нажмите правую кнопку мыши для отмены")
    EdgeChange = Canvas.find_withtag("current")
    Canvas.tag_unbind("Edge", "<Button 1>")
def SumbitChangeEdge(event=0):
    global EdgeChange
    uvtext=Canvas.gettags(EdgeChange)[1]
    Canvas.itemconfigure(EdgeChange,fill=rgbtohex(EntryEdgeR.get(),EntryEdgeG.get(),EntryEdgeB.get()))
    Canvas.itemconfigure(Canvas.find_withtag(f"TextEdge&&{uvtext}"),text=f'{EntryEdge.get()}')
    uv=uvtext.split('-')
    try:
        Graph[uv[0]][uv[1]]['weight'] =int(EntryEdge.get())
    except Exception:
        print("Проблемы с изменением дуги")
    Canvas.tag_bind("Edge","<Button 1>", ShowEdgeChange)

def Elier_Circiut(event=0):
    app.config(menu='')
    result=''
    if nk.is_eulerian(Graph):
        try:
            result=list(nk.eulerian_circuit(Graph))
        except Exception:
            result="Невозможно"
    else:
        result="Граф не удовлетворяет условию"
    InfoLabel["text"]=f"Эйлеровый цикл Графа:{result} | Нажмите правую кнопку мыши в месте рисования для завершения"
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 3>", StopInputModeNodes)
def Dijkstra(event=0):
    app.config(menu='')
    result=''
    try:
        result=dict(nk.all_pairs_dijkstra_path(Graph))
    except nk.exception:
        result="Невозможно"
    InfoLabel["text"]=f"Матрица Дейкстры Для Графа:\n {result} \n Нажмите правую кнопку мыши в месте рисования для завершения"
    InfoLabel.pack(fill="both", expand=False, side="top")
    Canvas.bind("<Button 3>", StopInputModeNodes)
def Radius(event=0):
    app.config(menu='')
    result=''
    try:
        result=nk.radius(Graph)
    except Exception:
        result="Невозможно"
    InfoLabel["text"]=f"Радиус Графа: {result} | Нажмите правую кнопку мыши в месте рисования для завершения"
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 3>", StopInputModeNodes)
def Diameter(event=0):
    app.config(menu='')
    result=''
    try:
        result=nk.diameter(Graph)
    except Exception:
        result="Невозможно"
    InfoLabel["text"]=f"Диаметр Графа: {result} | Нажмите правую кнопку мыши в месте рисования для завершения"
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 3>", StopInputModeNodes)
def Center(event=0):
    app.config(menu='')
    result=''
    try:
        result=nk.center(Graph)
    except Exception:
        result="Невозможно"
    InfoLabel["text"]=f"Центр Графа: {result} | Нажмите правую кнопку мыши в месте рисования для завершения"
    InfoLabel.pack(fill="x", expand=False, side="top")
    Canvas.bind("<Button 3>", StopInputModeNodes)

def SaveGraphtxt(event=0):
    global GraphName
    with open(f"{filedialog.asksaveasfilename(filetypes=[['TXT-files', '*.txt']])}.txt",mode='w') as w_file:
        file_writer=csv.writer(w_file, delimiter=';',lineterminator='\r')
        NodesID=Canvas.find_withtag("Node")
        EdgesID=Canvas.find_withtag("Edge")
        TextEdgesID=Canvas.find_withtag("TextEdge")
        Nodes=[Canvas.gettags(item)[1] for item in NodesID]
        Edges=[Canvas.gettags(item)[1] for item in EdgesID]
        count=0
        for item in TextEdgesID:
            Edges[count]+=f" {Canvas.itemcget(item,'text')}"
            count+=1
        file_writer.writerow([GraphName,Graph.is_directed(),list(Nodes),list(Edges)])
def OpenGraphtxt(event=0):
    global Graph,NodeCount,GraphName

    with open(filedialog.askopenfilename(filetypes=[['TXT-files', '*.txt']]),mode='r') as r_file:
        file_reader = csv.reader(r_file,delimiter=';')
        listreader=next(file_reader)
        GraphName=listreader[0]
        NodeCount=1
        try:
            Graph.clear()
        except AttributeError:
            print("Попытка стирания пустого графа")
        try:
            Canvas.delete("all")
        except Exception:
            print("Попытка стирания пустого канваса")
        arrow=None
        if listreader[1]=="True":
            Graph = nk.DiGraph()
            arrow=ctk.LAST
        else:
            Graph = nk.Graph()
        Nodes=listreader[2][1:-1].replace('\'','').split(", ")
        Edges=listreader[3][1:-1].replace('\'','').replace('-',' ').split(", ")
        rand=SystemRandom()
        rand_x=rand.randrange(700)+50
        rand_y=rand.randrange(500)+50
        randlistx={}
        randlisty={}
        for index in Nodes:
            randlistx[index]=rand_x
            randlisty[index]=rand_y
            Canvas.create_oval(rand_x - 15, rand_y - 15, rand_x + 15, rand_y + 15, width=1,
                                          outline='#ffcc3d',
                                          fill='#c2334f',
                                          tags=["Node", f"{index}"],
                                          activefill='#3dccb0')
            Canvas.create_text(rand_x, rand_y, text=f"{index}",
                                              fill='#ffcc3d',
                                              tags=["TextNode", f"{index}"])
            NodeCount+=1
            Graph.add_node(index)
            rand_x=rand.randrange(700)+50
            rand_y=rand.randrange(500)+50
        anchor=None
        for index in Edges:
            indexlist=index.split(' ')
            x1=randlistx[indexlist[0]]
            x2=randlistx[indexlist[1]]
            y1=randlisty[indexlist[0]]
            y2=randlisty[indexlist[1]]
            if abs(y1 - y2) > abs(x1 - x2):
                anchor = "ne"
            else:
                anchor = "sw"
            if abs(y1 - y2) > abs(x1 - x2):
                if y1 < y2:
                    y1 += 15
                    y2 -= 15
                else:
                    y1 -= 15
                    y2 += 15
            else:
                if x1 < x2:
                    x1 += 15
                    x2 -= 15
                else:
                    x1 -= 15
                    x2 += 15
            Canvas.create_line(x1,y1,x2,y2, width=2, fill='#ffcc3d',
                               tags=["Edge",f"{indexlist[0]}-{indexlist[1]}" ,
                                     "Orient"], activewidth=5, arrow=arrow)
            Canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{int(indexlist[2])}", fill="Red", font='Helvetica 15 bold',
                           anchor=anchor, activefill="Green", \
                           tags=["TextEdge", f"{indexlist[0]}-{indexlist[1]}"])
            Graph.add_edge(indexlist[0],indexlist[1],weight=int(indexlist[2]))
        print(Nodes)
        print(Edges)
        main_menu.entryconfig(3, state=tk.NORMAL)
        main_menu.entryconfig(5, state=tk.NORMAL)

def OpenGraph(even=0):
    global Graph,NodeCount,GraphName
    try:
        Canvas.clear()
    except AttributeError:
        print("Попытка очитски пустого Канваса")
    Canvas.delete("all")
    NodeCount=1
    with open(filedialog.askopenfilename(filetypes=[['CSV-files', '*.csv']]),mode='r') as r_file:
        file_reader = csv.reader(r_file,delimiter=';')#,quoting=csv.QUOTE_NONNUMERIC )
        GraphName=next(file_reader)[0]
        print(GraphName)
        if next(file_reader)=="True":
            Graph = nk.DiGraph()
        else:
            Graph = nk.Graph()
        #Graph.add_weighted_edges_from(next(file_reader))
        edges=next(file_reader)#[1:-1]#.split(", ")
        print(edges)
        for i in edges:
            edge=i[1:-1].split(", ")
            print(edge[0:])
            Graph.add_edge(edge[0][1:-1],edge[1][1:-1],weight=int(edge[2]))
        for item in file_reader:
            print(item)
            coords=item[1][1:-1].split(", ")
            print(coords[1])
            print(item[4][1:-1].replace('\"', '').replace('\'','').split(', '))
            if item[0]=="Node":
                NodeCount+=1
                tags=item[4][1:-1].replace('\"', '').replace('\'','').split(', ')
                print(Canvas.gettags(Canvas.create_oval(coords[0],coords[1],coords[2],coords[3],width=1,\
                                                        outline=item[2],fill=item[3],tags=tags,activefill=item[5])))
            elif item[0]=="TextNode":
                Graph.add_node(item[2])
                tags=item[4][1:-1].replace('\"', '').replace('\'','').split(', ')
                print(Canvas.gettags(Canvas.create_text(coords[0],coords[1],text=item[2],fill=item[3],tags=tags)))
            elif item[0]=="Edge":
                tags=item[3][1:-1].replace('\"', '').replace('\'','').split(', ')
                print(Canvas.gettags(Canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=2,\
                                                        fill=item[2],tags=tags,arrow=item[4],activewidth=5)))
            elif item[0]=="TextEdge":
                tags=item[4][1:-1].replace('\"', '').replace('\'','').split(', ')
                print(Canvas.gettags(Canvas.create_text(coords[0],coords[1],text=item[2],anchor=item[3],\
                                                        tags=tags,fill="Red", font='Helvetica 15 bold',activefill="Green")))
    Canvas.gettags("all")
    main_menu.entryconfig(3, state=tk.NORMAL)
    main_menu.entryconfig(5, state=tk.NORMAL)
def SaveGraph(event=0):
    #nk.write_gexf(Graph, "new.gexf")
    global GraphName
    Nodes=Canvas.find_withtag("Node")
    TextNodes=Canvas.find_withtag("TextNode")
    Edges=Canvas.find_withtag("Edge")
    TextEdges=Canvas.find_withtag("TextEdge")
    with open(f"{GraphName}.csv",mode='w') as w_file:
        file_writer= csv.writer(w_file, delimiter=';',lineterminator='\r')
        file_writer.writerow([GraphName])
        file_writer.writerow([Graph.is_directed()])
        file_writer.writerow(list(Graph.edges.data("weight", default=1)))
        for item in Nodes:
            file_writer.writerow(["Node",Canvas.coords(item),Canvas.itemcget(item,'outline'),\
                                  Canvas.itemcget(item,'fill'),Canvas.gettags(item),Canvas.itemcget(item,'activefill')])
        for item in TextNodes:
            file_writer.writerow(["TextNode",Canvas.coords(item),Canvas.itemcget(item,'text'),\
                                  Canvas.itemcget(item,'fill'),Canvas.gettags(item)])
        for item in Edges:
            file_writer.writerow(["Edge",Canvas.coords(item),Canvas.itemcget(item,'fill'),\
                                  Canvas.gettags(item),Canvas.itemcget(item,'arrow')])
        for item in TextEdges:
            file_writer.writerow(["TextEdge",Canvas.coords(item),Canvas.itemcget(item,'text'),\
                                  Canvas.itemcget(item,'anchor'),Canvas.gettags(item)])
def SaveasGraph(event=0):
    global GraphName
    Nodes=Canvas.find_withtag("Node")
    TextNodes=Canvas.find_withtag("TextNode")
    Edges=Canvas.find_withtag("Edge")
    TextEdges=Canvas.find_withtag("TextEdge")
    with open(f"{filedialog.asksaveasfilename(filetypes=[['CSV-files', '*.csv']])}.csv",mode='w') as w_file:
        file_writer= csv.writer(w_file, delimiter=';',lineterminator='\r')
        file_writer.writerow([GraphName])
        file_writer.writerow([Graph.is_directed()])
        file_writer.writerow(list(Graph.edges.data("weight", default=1)))
        for item in Nodes:
            file_writer.writerow(["Node",Canvas.coords(item),Canvas.itemcget(item,'outline'),\
                                  Canvas.itemcget(item,'fill'),Canvas.gettags(item),Canvas.itemcget(item,'activefill')])
        for item in TextNodes:
            file_writer.writerow(["TextNode",Canvas.coords(item),Canvas.itemcget(item,'text'),\
                                  Canvas.itemcget(item,'fill'),Canvas.gettags(item)])
        for item in Edges:
            file_writer.writerow(["Edge",Canvas.coords(item),Canvas.itemcget(item,'fill'),\
                                  Canvas.gettags(item),Canvas.itemcget(item,'arrow')])
        for item in TextEdges:
            file_writer.writerow(["TextEdge",Canvas.coords(item),Canvas.itemcget(item,'text'),\
                                  Canvas.itemcget(item,'anchor'),Canvas.gettags(item)])


LabelText=''
def GraphInfo(event=0):
    global GraphAlgLabel,GraphName,LabelText
    app.config(menu='')
    InfoLabel["text"]="Нажмите правую кнопку мыши в месте рисования для закрытия меню"
    InfoLabel.pack(fill="x", expand=False, side="top")
    LabelText=f"Имя графа: {GraphName}"
    #LabelText+='*' * 20

    LabelText+=f"\nКол-во узлов: {Graph.number_of_nodes()}"
    LabelText+=f"\nКол-во дуг: {Graph.number_of_edges()}"
    LabelText+=f"\nУзлы: {Graph.nodes()}"
    LabelText+=f"\nДуги: {list(Graph.edges(data=True))}"
    LabelText+="\nСтепени вершин: "
    for node in Graph.nodes():
       LabelText+=f"\n{node} - {Graph.degree(node)}"
    LabelText+="\nМатрица Индидентности: "
    try:
        LabelText+=f"\n{nk.incidence_matrix(Graph).todense()}"
    except nk.exception:
        LabelText+="Невозможно"
    LabelText+="\nМатрица Смежности: "
    try:
        LabelText+=f"\n{nk.adjacency_matrix(Graph,weight=None).todense()}"
    except nk.exception:
        LabelText+="Невозможно"
    GraphInfoSecond()

def GraphInfoSecond(event=0):
    global LabelText
    LabelText+="\nЯвляется ли деревом: "
    try:
        LabelText+=f"{nk.is_tree(Graph)}"
    except nk.exception:
        LabelText+="Невозможно"
    LabelText+="\nЯвляется ли полным: "
    try:
        LabelText+=f"{nk.is_clique(Graph)}"
    except nk.exception:
        LabelText+="Невозможно"
    LabelText+="\nЯвляется ли связным: "
    try:
        LabelText+=f"{nk.is_connected(Graph)}"
    except nk.exception:
        LabelText+="Невозможно"
    LabelText+="\nЯвляется ли Эйлеровым: "
    try:
        LabelText+=f"{nk.is_eulerian(Graph)}"
    except nk.exception:
        LabelText+="Невозможно"
    LabelText+="\nЯвляется ли планарным: "
    try:
        LabelText+=f"{nk.is_planar(Graph)}\n"
    except nk.exception:
        LabelText+="Невозможно\n"
    #LabelText+='*' * 20
    print(LabelText)
    GraphAlgLabel.configure(text=LabelText)
    GraphAlgInfo.deiconify()
    Canvas.bind("<Button 3>", StopInputModeNodes)

def NewGraph(event=0):
    app.config(menu='')
    GraphFrame.pack(fill="x", expand=False)
    GraphButton.configure(command=NewGraphSumbit)
def NewGraphSumbit(event=0):
    global Graph, GraphName
    if RadioVar.get() == 0:
        Graph = nk.Graph()
    elif RadioVar.get() == 1:
        Graph = nk.DiGraph()
    if GraphEntry.get() != '':
        GraphName = GraphEntry.get()
    else:
        GraphName = 'DefaultName'
    GraphFrame.pack_forget()
    main_menu.entryconfig(3, state=tk.NORMAL)
    main_menu.entryconfig(5, state=tk.NORMAL)
    app.config(menu=main_menu)
def ChangeGraphName(event=0):
    app.config(menu='')
    GraphFrame.pack(fill="x", expand=False)
    GraphRadioButton1.grid_forget()
    GraphRadioButton2.grid_forget()
    GraphButton.configure(command=ChangeGraphNameSumbit)
def ChangeGraphNameSumbit(event=0):
    global GraphName
    if GraphEntry.get() != '':
        GraphName = GraphEntry.get()
    else:
        GraphName = 'DefaultName'
    GraphRadioButton1.grid(row=0, column=0, pady=5)
    GraphRadioButton2.grid(row=0, column=1, pady=5)
    GraphFrame.pack_forget()
    app.config(menu=main_menu)


# Базовые значения окна
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600+580+250")
app.minsize(width=800, height=600)
app.title("Karagodin Graph")
#app.iconphoto(False, tk.PhotoImage(file='winIcon.png'))

# Каркас Рисовки
Canvas = tk.Canvas(app, bg="#1f2024", borderwidth=0, highlightthickness=0)
Canvas.pack(fill="both", expand=True, side="bottom")
Canvas.tag_bind("TextNode", "<Enter>", EnterAndLeaveTextVericle)
Canvas.tag_bind("TextNode", "<Leave>", EnterAndLeaveTextVericle)
#Canvas.delete("all")
# Окно Создания вершины
Toplevel = ctk.CTkToplevel(app)
Toplevel.title("Создание Вершины и границы")
Toplevel.geometry('300x400+800+20')
Toplevel.resizable(0, 0)
Toplevel.attributes('-topmost', True)
# Toplevel.overrideredirect(True)
LabelNode = ctk.CTkLabel(Toplevel, text="Цвета Вершины")
LabelNode.grid(row=1, column=1, padx=5)
LabelNodeR = ctk.CTkLabel(Toplevel, text="R:")
LabelNodeR.grid(row=2, column=1)
EntryNodeR = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeR.grid(row=3, column=1)
LabelNodeG = ctk.CTkLabel(Toplevel, text="G:")
LabelNodeG.grid(row=4, column=1)
EntryNodeG = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeG.grid(row=5, column=1)
LabelNodeB = ctk.CTkLabel(Toplevel, text="B:")
LabelNodeB.grid(row=6, column=1)
EntryNodeB = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeB.grid(row=7, column=1)
LabelNodeBorder = ctk.CTkLabel(Toplevel, text="Цвета Границы")
LabelNodeBorder.grid(row=1, column=2, padx=5)
LabelNodeBorderR = ctk.CTkLabel(Toplevel, text="R:")
LabelNodeBorderR.grid(row=2, column=2)
EntryNodeBorderR = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeBorderR.grid(row=3, column=2)
LabelNodeBorderG = ctk.CTkLabel(Toplevel, text="G:")
LabelNodeBorderG.grid(row=4, column=2)
EntryNodeBorderG = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeBorderG.grid(row=5, column=2)
LabelNodeBorderB = ctk.CTkLabel(Toplevel, text="B:")
LabelNodeBorderB.grid(row=6, column=2)
EntryNodeBorderB = ctk.CTkEntry(Toplevel, placeholder_text="0-255")
EntryNodeBorderB.grid(row=7, column=2)
CanvasNode = ctk.CTkCanvas(Toplevel, width=50, height=50, borderwidth=0, highlightthickness=0)
CanvasNode.grid(row=8, column=1, pady=5)
CanvasNodeBord = ctk.CTkCanvas(Toplevel, width=50, height=50, borderwidth=0, highlightthickness=0)
CanvasNodeBord.grid(row=8, column=2, pady=5)
CanvasNode.after(1, RgbCanvasNodebg)
LabelTextNode = ctk.CTkLabel(Toplevel, text="Текст вершины")
EntryTextNode = ctk.CTkEntry(Toplevel, placeholder_text="Пучинский")
ButtonChange = ctk.CTkButton(Toplevel, text="Подвердить", command=SumbitChangeNode)
LabelTextNode.grid(row=9, column=1, pady=5)
EntryTextNode.grid(row=9, column=2, pady=5)
# ButtonChange.grid(row=10,column=1,columnspan=2)
Toplevel.withdraw()

# Инфо-Строка
InfoLabel = tk.Label(text="lorem50", height=4, bg="#000d44", fg="white")
#InfoLabel.pack(fill="x", expand=False)
#InfoLabel.pack_forget()

#Граф-Алгоритмы Окно-строка
GraphAlgInfo=ctk.CTkToplevel(app)
GraphAlgInfo.geometry('500x440+800+20')
GraphAlgLabel=ctk.CTkLabel(GraphAlgInfo,text="standart")
GraphAlgLabel.pack(fill="both", expand=True)
GraphAlgInfo.withdraw()
# Окно для Дуг
FrameEdge = ctk.CTkFrame(app, bg='white', height=30)
FrameEdge.pack(fill="x", expand=False)
LabelEdge = ctk.CTkLabel(FrameEdge, text="Вес:", width=50)
EntryEdge = ctk.CTkEntry(FrameEdge, placeholder_text="Догадайтесь что", width=115)
LabelEdgeR = ctk.CTkLabel(FrameEdge, text="R:", width=10)
EntryEdgeR = ctk.CTkEntry(FrameEdge, placeholder_text="0-255")
LabelEdgeG = ctk.CTkLabel(FrameEdge, text="G:", width=10)
EntryEdgeG = ctk.CTkEntry(FrameEdge, placeholder_text="0-255")
LabelEdgeB = ctk.CTkLabel(FrameEdge, text="B:", width=10)
EntryEdgeB = ctk.CTkEntry(FrameEdge, placeholder_text="0-255")
CanvasEdge = ctk.CTkCanvas(FrameEdge, width=30, height=30, borderwidth=0, highlightthickness=0)
CanvasEdge.after(1, CanvasEdgebg)
ButtonEdge= ctk.CTkButton(FrameEdge,text='Подвердить',command=SumbitChangeEdge)
for i in range(1, 9):
    FrameEdge.grid_columnconfigure(index=i, weight=1)
LabelEdge.grid(row=1, column=0, sticky="e")
EntryEdge.grid(row=1, column=1, sticky="w")
LabelEdgeR.grid(row=1, column=2, sticky="e")
EntryEdgeR.grid(row=1, column=3, sticky="w")
LabelEdgeG.grid(row=1, column=4, sticky="e")
EntryEdgeG.grid(row=1, column=5, sticky="w")
LabelEdgeB.grid(row=1, column=6, sticky="e")
EntryEdgeB.grid(row=1, column=7, sticky="w")
CanvasEdge.grid(row=1, column=8)
#ButtonEdge.grid(row=2, column=3, columnspan=3)
FrameEdge.pack_forget()

# Окно начальной настройки графа
GraphFrame = ctk.CTkFrame(app, bg='white', height=30)
RadioVar = ctk.IntVar()
GraphRadioButton1 = ctk.CTkRadioButton(GraphFrame, text="Неориентированный", variable=RadioVar, value=0)
GraphRadioButton2 = ctk.CTkRadioButton(GraphFrame, text="Ориентированный", variable=RadioVar, value=1)
GraphLabel = ctk.CTkLabel(GraphFrame, text="Название графа:", width=50)
GraphEntry = ctk.CTkEntry(GraphFrame, placeholder_text="Название", width=110)
GraphFrame.grid_rowconfigure(index=0, weight=1)
GraphFrame.grid_rowconfigure(index=1, weight=1)
GraphFrame.grid_columnconfigure(index=0, weight=1)
GraphFrame.grid_columnconfigure(index=1, weight=1)
GraphRadioButton1.grid(row=0, column=0, pady=5)
GraphRadioButton2.grid(row=0, column=1, pady=5)
GraphLabel.grid(row=1, column=0, sticky="s")
GraphEntry.grid(row=1, column=0, sticky="e")
GraphButton = ctk.CTkButton(GraphFrame, text="Подвердить")
GraphButton.bind("<Button 1>", NewGraphSumbit)
GraphButton.grid(row=1, column=1, sticky="s")

# Меню
main_menu = tk.Menu(app)
GraphMenu = tk.Menu(main_menu, tearoff=0)
GraphMenu.add_command(label="Новый граф", command=NewGraph)
GraphMenu.add_command(label="Открыть...", command=OpenGraph)
GraphMenu.add_command(label="Открыть граф(текст)",command=OpenGraphtxt)
GraphMenu.add_command(label="Сохранить", command=SaveGraph)
GraphMenu.add_command(label="Сохранить как...", command=SaveasGraph)
GraphMenu.add_command(label="Сохранить граф(текст)",command=SaveGraphtxt)
GraphMenu.add_separator()
GraphMenu.add_command(label="Вывод информации о графе", command=GraphInfo)
GraphMenu.add_command(label="Поменять имя графа", command=ChangeGraphName)
GraphMenu.add_separator()
GraphMenu.add_command(label='Выйти', command=exit)

NodesEdges = tk.Menu(main_menu, tearoff=0)
NodesEdges.add_command(label="Добавить узлы", command=InputNodesMode)
NodesEdges.add_command(label="Удалить узлы", command=DeleteNodeMode)
NodesEdges.add_command(label="Изменение узлов", command=ChangeNodeMode)
NodesEdges.add_command(label="Перемещение узлов", command=MoveNodeMode)
NodesEdges.add_separator()
NodesEdges.add_command(label="Добавить дуги", command=InputEdgeMode)
NodesEdges.add_command(label="Удалить дуги", command=DeleteEdgeMode)
NodesEdges.add_command(label="Изменение дуг", command=ChangeEdgeMode)

Algorithms = tk.Menu(main_menu, tearoff=0)
Algorithms.add_command(label="Алгоритм Дейсктры", command=Dijkstra)
Algorithms.add_separator()
Algorithms.add_command(label="Диаметр графа",command=Diameter)
Algorithms.add_command(label="Радиус графа",command=Radius)
Algorithms.add_command(label="Центр графа",command=Center)
Algorithms.add_separator()
Algorithms.add_command(label="Эйлеровый Цикл",command=Elier_Circiut)

main_menu.add_cascade(label="Граф", menu=GraphMenu)
main_menu.add_separator()
main_menu.add_cascade(label="Дуги и Узлы", menu=NodesEdges)
main_menu.add_separator()
main_menu.add_cascade(label="Алгоритмы и Вычисления", menu=Algorithms)
# main_menu.entryconfig(1,state=tk.DISABLED)
main_menu.entryconfig(3, state=tk.DISABLED)
main_menu.entryconfig(5, state=tk.DISABLED)

# Запуск основного цикла
app.config(menu=main_menu)
app.mainloop()
