from customtkinter import CTk, CTkEntry, CTkButton, CTkToplevel, CTkCanvas
from tkinter import messagebox
from config import vertex_radius
from math import sqrt


class Vertex:
    def __init__(self, canvas, name: int | str, x: int, y: int, id_vert: int, color: str = 'black') -> None:
        self.name = str(name)
        self.id_vert = id_vert
        self.x = x
        self.y = y
        self.radius = vertex_radius
        self.color = color

        self.canvas = canvas

        self.is_selected = False

        self.circle = create_circle(self.canvas, self.x, self.y, self.radius, fill=self.color)
        self.text = self.canvas.create_text(self.x, self.y, text=self.name, font=f'Arial {self.radius-5}', fill='white')

    def delete(self):
        self.canvas.delete(self.circle)
        self.canvas.delete(self.text)
        if self.is_selected:
            self.canvas.delete(self.selection)

    def select(self):
        self.is_selected = True
        self.selection = create_circle(self.canvas, self.x, self.y, self.radius+3, outline='red', width=3)

    def unselect(self):
        self.is_selected = False
        try:
            self.canvas.delete(self.selection)
        except AttributeError:
            pass

    def show_properties(self, event):
        props_vert = CTk()
        props_vert.wm_attributes('-topmost', '1')
        props_vert.title(f'Vertex: {self.name} properties')
        props_vert.geometry(f'300x300+{event.x+250}+{event.y}')
        props_vert.bind('<Escape>', lambda event: props_vert.destroy())

        name_entry = CTkEntry(props_vert, text='Введите имя', justify='center')
        name_entry.insert(0, self.name)
        name_entry.place(anchor='n', relx=0.5, rely=0.1)
        name_entry.bind('<Return>', lambda event: self.rename(name_entry.get()))
        name_entry.focus()


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

        clrbtn_1.place(anchor='nw', relx=0, rely=0.28, relwidth=0.333, relheight=0.2)
        clrbtn_2.place(anchor='nw', relx=0.33, rely=0.28, relwidth=0.333, relheight=0.2)
        clrbtn_3.place(anchor='nw', relx=0.66, rely=0.28, relwidth=0.35, relheight=0.2)
        clrbtn_4.place(anchor='nw', relx=0, rely=0.48, relwidth=0.333, relheight=0.2)
        clrbtn_5.place(anchor='nw', relx=0.33, rely=0.48, relwidth=0.333, relheight=0.2)
        clrbtn_6.place(anchor='nw', relx=0.66, rely=0.48, relwidth=0.35, relheight=0.2)
        clrbtn_7.place(anchor='nw', relx=0, rely=0.68, relwidth=0.333, relheight=0.2)
        clrbtn_8.place(anchor='nw', relx=0.33, rely=0.68, relwidth=0.333, relheight=0.2)
        clrbtn_9.place(anchor='nw', relx=0.66, rely=0.68, relwidth=0.35, relheight=0.2)
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
        if self.is_selected:
            self.canvas.coords(self.selection, self.x-self.radius-3, self.y-self.radius-3, self.x+self.radius+3, self.y+self.radius+3)



class Edge:
    def __init__(self, canvas, weight: int, vertex1: Vertex, vertex2: Vertex, oriented: bool, color='black') -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2

        self.weight = weight
        self.x1, self.y1 = vertex1.x, vertex1.y
        self.x2, self.y2 = vertex2.x, vertex2.y

        self.is_oriented = oriented
        self.is_loop = self.vertex1 == self.vertex2

        self.color = color
        self.thickness = vertex_radius // 5

        self.canvas = canvas


        if self.is_oriented:
            if self.is_loop:
                pass
            else:
                self.line = self.canvas.create_line(*line_intersect_circle(self.x1, self.y1, self.x2, self.y2), fill=self.color,
                                                    width=self.thickness, arrow='last', arrowshape=(25, 25, 5))
                self.rect = self.canvas.create_rectangle((self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13,
                                                        (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13, fill='white', width=0)
                self.text = self.canvas.create_text((self.x1+self.x2)/2, (self.y1+self.y2)/2, text=self.weight, font=('Arial', 18), fill='black', )
        else:
            if self.is_loop:
                pass
            else:
                self.line = self.canvas.create_line(*line_intersect_circle(self.x1, self.y1, self.x2, self.y2), fill=self.color, width=self.thickness)
                self.rect = self.canvas.create_rectangle((self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13,
                                                        (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13, fill='white', width=0)
                self.text = self.canvas.create_text((self.x1+self.x2)/2, (self.y1+self.y2)/2, text=self.weight, font=('Arial', 18), fill='black')

    def delete(self):
        self.canvas.delete(self.line)
        self.canvas.delete(self.rect)
        self.canvas.delete(self.text)
        del self.vertex1
        del self.vertex2

    def change_weight(self, weight, graph):
        try:
            self.weight = int(weight)
        except ValueError:
            messagebox.showerror('Ошибка', 'Вес должен быть числом')
        else:
            self.canvas.coords(self.rect, (self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13,
                              (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13)
            self.canvas.itemconfig(self.text, text=self.weight)
            graph.adjacency_matrix[self.vertex1.id_vert][self.vertex2.id_vert] = self.weight
            if not self.is_oriented:
                graph.adjacency_matrix[self.vertex2.id_vert][self.vertex1.id_vert] = self.weight

    def change_color(self, color):
        self.color = color
        self.canvas.itemconfig(self.line, fill=self.color)


    def move(self):
        self.x1, self.y1 = self.vertex1.x, self.vertex1.y
        self.x2, self.y2 = self.vertex2.x, self.vertex2.y
        self.canvas.coords(self.line, line_intersect_circle(self.x1, self.y1, self.x2, self.y2))
        self.canvas.coords(self.rect, (self.x1+self.x2)/2-len(str(self.weight))*8, (self.y1+self.y2)/2-13,
                          (self.x1+self.x2)/2+len(str(self.weight))*8, (self.y1+self.y2)/2+13)
        self.canvas.coords(self.text, (self.x1+self.x2)/2, (self.y1+self.y2)/2)

    def show_properties(self, event, graph):
        props_edge = CTkToplevel()
        props_edge.wm_attributes('-topmost', '1')
        props_edge.title('Edge properties')
        props_edge.geometry(f'300x300+{event.x+250}+{event.y}')
        props_edge.bind('<Escape>', lambda event: props_edge.destroy())

        name_entry = CTkEntry(props_edge, text='Введите вес', justify='center')
        name_entry.delete(0, 'end')
        name_entry.insert(0, str(self.weight))
        name_entry.place(anchor='n', relx=0.5, rely=0.1)
        name_entry.bind('<Return>', lambda event: self.change_weight(name_entry.get(), graph))
        name_entry.focus()

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

        clrbtn_1.place(anchor='nw', relx=0, rely=0.28, relwidth=0.333, relheight=0.2)
        clrbtn_2.place(anchor='nw', relx=0.33, rely=0.28, relwidth=0.333, relheight=0.2)
        clrbtn_3.place(anchor='nw', relx=0.66, rely=0.28, relwidth=0.35, relheight=0.2)
        clrbtn_4.place(anchor='nw', relx=0, rely=0.48, relwidth=0.333, relheight=0.2)
        clrbtn_5.place(anchor='nw', relx=0.33, rely=0.48, relwidth=0.333, relheight=0.2)
        clrbtn_6.place(anchor='nw', relx=0.66, rely=0.48, relwidth=0.35, relheight=0.2)
        clrbtn_7.place(anchor='nw', relx=0, rely=0.68, relwidth=0.333, relheight=0.2)
        clrbtn_8.place(anchor='nw', relx=0.33, rely=0.68, relwidth=0.333, relheight=0.2)
        clrbtn_9.place(anchor='nw', relx=0.66, rely=0.68, relwidth=0.35, relheight=0.2)
        clrbtn_10.place(anchor='nw', relx=0, rely=0.88, relwidth=1, relheight=0.2)

        props_edge.mainloop()


def create_circle(canvas: CTkCanvas, x, y, r, **kwargs):
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def line_intersect_circle(x1, y1, x2, y2):
    '''Returns the coordinates of the intersection points of a line and two circles'''
    main_gipotenusa = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    main_dx = x2 - x1
    main_dy = y2 - y1
    dx = (main_gipotenusa - vertex_radius) * main_dx / main_gipotenusa
    dy = (main_gipotenusa - vertex_radius) * main_dy / main_gipotenusa

    return x2 - dx, y2 - dy, x1 + dx, y1 + dy