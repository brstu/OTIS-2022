```python
from tkinter import *
from tkinter import messagebox as mb

tk = Tk() # Создание окна
tk.title("Graph") # Заголовок окна
tk.geometry(f"860x860+310+0") # Размер окна и его расположение
tk.resizable(0, 0) #Запрет на изменение размера окна
# tk.state('zoomed') #Развернуть окно на весь экран
tk.overrideredirect(1)  # убирает рамку окна и запрещает его изменять размер
tk.wm_attributes('-topmost', 1) # Окно всегда сверху
# tk.update()

canvas = Canvas(tk, bg="#888", width=856, height=726) # Создание холста

canvas.place(x=0, y=130)    # Расположение холста

label = Label(tk) # Создание метки
label.place(x=370, y=100) # Расположение метки
label["text"] = "Имя графа" # Текст метки






# canvas.bind("<Motion> <B1-Motion>",movement) #отслеживание движения мыши

#Класс создания вершины
class Vertex:
    def __init__(self, canvas, color):
        global x_click, y_click, vert_name, vertex_count
        self.vertex_count = vertex_count
        self.vert_name = vert_name
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_oval(-12, -12, 40, 40, fill=color, width=2)
        self.canvas.move(self.id, x_click, y_click)
        # print(self.id)
        self.id = self.canvas.create_text(x_click + 14, y_click + 12, text=self.vert_name[self.vertex_count - 1],
                                          font="Arial 10", fill="white")
        print(self.id)
        # self.btn.id=Button(canvas, )
        canvas.unbind("<Button-1>")

    def get(self):
        return (self.canvas, self.color, self.posx, self.posy)


# Создание шара и лини ведущей к нему
# canvas.create_polygon([135,210],[210,140], outline="black",width=2)
# ball = [Vertex(canvas, 'green', 100, 200, 1)]
# Vertex.append(Vertex(canvas, 'blue', 200, 100))

#Отслеживание нажатия кнопки мыши и запись в глобальные переменные
def on_wasd(event):
    global x_click, y_click
    # if x_click != 0 and y_click != 0:
    x_click = event.x
    y_click = event.y
    print(f"x={event.x} y={event.y}", "asdsadas")
    # print(f"x={x_click} y={y_click}")



def movement(event):
    pass
    # print(f"x1={event.x} y1={event.y}")

#Отслеживание нажатия кнопки мыши и запись в глобальные переменные
# def mouseclick():
#     mouse_x = tk.winfo_pointerx() - tk.winfo_rootx()
#     mouse_y = tk.winfo_pointery() - tk.winfo_rooty()
#     print(mouse_x, mouse_y)

#функция выхода из программы
def quitfunc(root):
    root.destroy()


# Законченная функция создания имени графа №1
def change_graf_name(name, root):
    label["text"] = name
    quitfunc(root)


# Законченная функция создания имени графа №2
def graf_name():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(0, 0)
    label = Label(new_window)
    label["text"] = "Введите имя графа"
    label.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_window)
    entry.grid(row=1, column=0)
    btnGraf = Button(new_window, text="Ввод", command=lambda: change_graf_name(entry.get(), new_window))
    btnGraf.grid(row=2, column=0, sticky="ew")
    if entry.get == label["text"]:
        new_window.destroy()
    new_window.mainloop


def choose_opt_vert():
    pass


def save_data():
    pass


def import_data():
    pass



def color_for_vert(number):
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

#Функция создания вершины
def create_vertex(root):
    global call_count
    if call_count != 0:
        global vertex_count, x_click, y_click
        vertex_count += 1
        print(x_click, y_click)  # отслеживание нажатия кнопки мыш
        vertex.append(Vertex(canvas, color))
        root.destroy()
    else:
        mb.showerror("Ошибка", "Вы не ввели имя вершины")


call_count = 0


#Меню создания вершины
def menu_create_vetrex():
    global vert_name,call_count
    call_count = 0
    canvas.bind("<Button-1>", on_wasd)  # Событие нажатия кнопки мыши
    vert_name.append("")

    def create_name_vert(entry):
        global call_count
        call_count += 1
        for i in [vert_name]:
            if '' == entry.get():
                mb.showerror("Ошибка", "Вы не ввели имя вершины")
            elif entry.get() not in vert_name:
                vert_name[vertex_count] = entry.get()
                print(vert_name)
            else:
                mb.showerror("Ошибка", "Такая вершина уже существует")
    new_window = Tk()
    new_window.geometry("300x100+0+0")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(0, 0)
    label = Label(new_window)
    label["text"] = "Введите имя вершины"
    entry = Entry(new_window)
    btnVertName = Button(new_window, text="Ввод", command=lambda: create_name_vert(entry))
    btnColor1 = Button(new_window, text="Синий", command=lambda: give_color(1),bg="blue")
    btnColor2 = Button(new_window, text="Красный", command=lambda: give_color(2), bg="red")
    btnColor3 = Button(new_window, text="Зелёный", command=lambda: give_color(3), bg="green")
    btnCreate = Button(new_window, text="""Создать 
вершину""", command=lambda: create_vertex(new_window))
    label.grid(row=0, column=0, sticky="ew")
    entry.grid(row=1, column=0)
    btnVertName.grid(row=2, column=0, sticky="ew")
    btnColor1.grid(row=0, column=1, sticky="ew")
    btnColor2.grid(row=1, column=1, sticky="ew")
    btnColor3.grid(row=2, column=1, sticky="ew")
    btnCreate.grid(row=0, column=2, sticky="sn", rowspan=3)

    new_window.mainloop

#Меню удаления вершины
def find_delete_vertex(entry, root):
    global vert_name
    True_False = 0
    while 1:
        for i in range(len(vert_name)):
            if vert_name[i] == entry:
                print(vert_name[i])
                canvas.delete(i + 1)  # Удаление вершины по её id
                canvas.delete(i + 2)  # Удаление текста по id вершины
                root.destroy()
                True_False = 1
                break
        if True_False == 1:
            break
        else:
            mb.showerror("Ошибка", "Вы ввели неверное имя вершины")
            break

#Удаление вершины
def delete_vertex():
    new_window = Tk()
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(0, 0)
    label = Label(new_window)
    label["text"] = "Введите имя удаляемой вершины"
    label.grid(row=0, column=0, sticky="ew")
    entry = Entry(new_window)
    entry.grid(row=1, column=0)
    btnDel = Button(new_window, text="Ввод", command=lambda: find_delete_vertex(entry.get(), new_window))
    btnDel.grid(row=2, column=0, sticky="ew")
    if entry.get == label["text"]:
        new_window.destroy()
    # new_window.mainloop
    # canvas.delete(3)  # Удаление вершины по её id
    # canvas.delete(4)  # Удаление текста по id вершины

#Переназвание вершины
def rename_vertex():
    global vert_name
    for i in range(len(vert_name)):
        print(vert_name[i])
    pass


vert_name = [] #Список имен вершин
vertex = []  # Глобальные переменные
color = "red" #Цвет вершины
x_click = 0 #Глобальные переменные
x_move = [] #Список координат x
y_click = 0 #Глобальные переменные
y_move = [] #Список координат y
vertex_count = 0 #Счетчик вершин

btn1 = Button(tk, text="Задать имя графа", command=graf_name)
btn2 = Button(tk, text="Сохранить Значения", command=save_data)
btn3 = Button(tk, text="Импортировать значения", command=import_data)
btn4 = Button(tk, text="Создать вершину", command=menu_create_vetrex)
btn5 = Button(tk, text="Удалить вершину", command=delete_vertex)
btn6 = Button(tk, text="Переименовать вершину", command=rename_vertex)
btn7 = Button(tk, text="7")
btn8 = Button(tk, text="quit", command=lambda: tk.destroy())

btn1.grid(row=0, column=0, stick="ew")
btn2.grid(row=0, column=1, stick="ew")
btn3.grid(row=0, column=2, stick="ew")
btn4.grid(row=0, column=3, stick="ew")
btn5.grid(row=0, column=4, stick="ew")
btn6.grid(row=0, column=5, stick="ew")
btn7.grid(row=1, column=0, stick="ew")
btn8.grid(row=1, column=5, stick="ew")

tk.mainloop()
```
