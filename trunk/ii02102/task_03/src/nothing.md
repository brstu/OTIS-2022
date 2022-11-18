```python
from tkinter import *
from pynput import mouse



tk = Tk()
tk.title("Graph")
tk.geometry(f"860x860")
tk.resizable(0, 0)
tk.overrideredirect(1)
tk.wm_attributes('-topmost', 1)
# tk.update()

canvas = Canvas(tk, bg="red", width=856, height=726)

canvas.place(x=0, y=130)

label = Label(tk)
label.place(x=370, y=100)
label["text"] = "Имя графа"



class Vertex:
    def __init__(self, canvas, color, posx, posy):
        self.canvas = canvas
        self.color = color
        self.posx = posx
        self.posy = posy
        self.id = canvas.create_oval(10, 10, 70, 70, fill=color, width=2)
        self.canvas.move(self.id, posx, posy)
        # self.btn.id=Button(canvas, )



# Создание шара и лини ведущей к нему
# canvas.create_polygon([135,210],[210,140], outline="black",width=2)
# ball = [Vertex(canvas, 'green', 100, 200, 1)]
#Vertex.append(Vertex(canvas, 'blue', 200, 100))


def mouseclick():
    mouse_x=tk.winfo_pointerx()-tk.winfo_rootx()
    mouse_y=tk.winfo_pointery()-tk.winfo_rooty()
    print(mouse_x, mouse_y)



def quitfunc(root):
    root.destroy()


def change_graf_name(name, root):
    label["text"] = name
    quitfunc(root)


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


vertex = []  # Глобальные переменные
color=""


def give_color(numb):
    global color
    if (numb == 1):
        color = "blue"
    elif (numb == 2):
        color = "red"
    else:
        color = "green"


def create_vertex(root):
    vertex.append(Vertex(canvas, color, 200, 200))
    root.destroy()

def menu_create_vetrex():
    new_window = Tk()
    new_window.geometry("600x400")
    new_window.title("Задайте имя графа")
    new_window.wm_attributes('-topmost', 1)
    new_window.resizable(0, 0)
    label = Label(new_window)
    label["text"] = "Введите имя вершины"
    entry = Entry(new_window)
    btnVertName = Button(new_window, text="Ввод", command=lambda: change_graf_name(entry.get(), new_window))
    btnColor1 = Button(new_window, text="Синий", command=lambda: give_color(1))
    btnColor2 = Button(new_window, text="Красный", command=lambda: give_color(2))
    btnColor3 = Button(new_window, text="Зелёный", command=lambda: give_color(3))
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


def delete_vertex():
    pass


def rename_vertex():
    pass


btn1 = Button(tk, text="Задать имя графа", command=graf_name)
btn2 = Button(tk, text="Сохранить Значения", command=save_data)
btn3 = Button(tk, text="Импортировать значения", command=import_data)
btn4 = Button(tk, text="Создать вершину", command=menu_create_vetrex)
btn5 = Button(tk, text="Удалить вершину", command=delete_vertex())
btn6 = Button(tk, text="Переименовать вершину", command=rename_vertex)
btn7 = Button(tk, text="7")
btn8 = Button(tk, text="quit",command= lambda : tk.destroy())

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
