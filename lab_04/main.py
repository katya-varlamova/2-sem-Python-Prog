from tkinter import *
from tkinter import messagebox as mb
class Point():
     def __init__(self, x, y, pointer):
         self.x = x
         self.y = y
         self.pointer = pointer
class Triangle():
    def __init__(self,  x1, y1, x2, y2, x3, y3):
         self.x1 = x1
         self.y1 = y1
         self.x2 = x2
         self.y2 = y2
         self.x3 = x3
         self.y3 = y3
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.solve_line = None
        self.parent = parent
        self.points = []
        self.triangles = []
        self.point_color = "black"
        self.triangle_color = 'red'
        self.brush_size = 2
        self.line = None
        self.array_of_points = []
        self.mode = 0
        self.canv = Canvas(self, bg="white")
        self.x_e = Entry(self)
        self.y_e = Entry(self)
        self.xlab = Label(self, text="x: ")
        self.ylab = Label(self, text="y: ")
        self.point_but = Button(self, text="Point", width=25,
                         command=lambda: self.set_drawing_mode(0),
                                activebackground = "#555",
                                background="#105",
                                foreground="#ccc",
                                padx="15",
                                pady="5",
                                font="16")
        self.point_but["state"] = ACTIVE
        self.triangle_but = Button(self, text="Triangle", width=25,
                         command=lambda: self.set_drawing_mode(1),
                                activebackground = "#555",
                                background="#105",
                                foreground="#ccc",
                                padx="15",
                                pady="5",
                                font="16")
        
        self.setUI()
        
    def set_color(self, new_color):
        self.color = new_color

    def set_drawing_mode(self, mode):
        if self.mode == mode:
            return
        if self.mode == 1:
            self.point_but["state"] = ACTIVE
            self.triangle_but["state"] = NORMAL
            if len(self.array_of_points) == 1:
                self.canv.delete(self.array_of_points[0].pointer)
                self.array_of_points = []
            elif len(self.array_of_points) == 2:
                self.canv.delete(self.line)
                self.canv.delete(self.array_of_points[0].pointer)
                self.canv.delete(self.array_of_points[1].pointer)
                self.line = None
                self.array_of_points = []
            else:
                self.mode = mode
            self.mode = mode
            self.set_color('black')
        else:
            self.point_but["state"] = NORMAL
            self.triangle_but["state"] = ACTIVE
            self.set_color('red')
            self.mode = mode

    def enter(self):
        try:
            x = float(self.x_e.get())
            y = float(self.y_e.get())
        except:
            show_error("x and y are numbers")
            self.x_e.delete(0,  END)
            self.y_e.delete(0,  END)
            return
        self.x_e.delete(0,  END)
        self.y_e.delete(0,  END)
        self.draw(x, y)
    def draw_handler(self, event):
        self.draw(event.x, event.y)

    def draw(self, x, y):
        if self.mode == 0:
            self.canv.create_oval(x - self.brush_size,
                                  y - self.brush_size,
                                  x + self.brush_size,
                                  y + self.brush_size,
                                  fill=self.point_color, outline=self.point_color)
            self.points.append(Point(x, y, None))
            self.find_line()
        else:
           
            if len(self.array_of_points) == 0:
                point = self.canv.create_oval(x - self.brush_size,
                                              y - self.brush_size,
                                              x + self.brush_size,
                                              y + self.brush_size,
                                              fill=self.triangle_color, outline=self.triangle_color)                
                self.array_of_points.append(Point(x, y, point))
            elif len(self.array_of_points) == 1:
                if self.array_of_points[0].x == x and self.array_of_points[0].y == y:
                    show_error("points must not match")
                    return
                point = self.canv.create_oval(x - self.brush_size,
                                              y - self.brush_size,
                                              x + self.brush_size,
                                              y + self.brush_size,
                                              fill=self.triangle_color, outline=self.triangle_color)
                self.array_of_points.append(Point(x, y, point))
                self.line = self.canv.create_line(self.array_of_points[0].x,
                                                  self.array_of_points[0].y,
                                                  self.array_of_points[1].x,
                                                  self.array_of_points[1].y,
                                                  fill=self.triangle_color)
            else:
                if self.array_of_points[0].x == x and self.array_of_points[0].y == y or\
                   self.array_of_points[1].x == x and self.array_of_points[1].y == y:
                    show_error("points must not match")
                    return             
                if self.belongs_to_line(self.array_of_points[0].x,
                                   self.array_of_points[0].y,
                                   self.array_of_points[1].x,
                                   self.array_of_points[1].y,
                                   x, y):
                    show_error("point must not belong to line")
                    return
                point = self.canv.create_oval(x - self.brush_size,
                                              y - self.brush_size,
                                              x + self.brush_size,
                                              y + self.brush_size,
                                              fill=self.triangle_color, outline=self.triangle_color)   
                self.canv.create_line(self.array_of_points[0].x,
                                      self.array_of_points[0].y,
                                      x,
                                      y,
                                      fill=self.triangle_color)
                self.canv.create_line(self.array_of_points[1].x,
                                      self.array_of_points[1].y,
                                      x,
                                      y,
                                      fill=self.triangle_color)
                self.triangles.append(Triangle(self.array_of_points[0].x,
                                          self.array_of_points[0].y,
                                          self.array_of_points[1].x,
                                          self.array_of_points[1].y,
                                          x, y))
                self.line = None
                self.array_of_points = []
                self.find_line()
    def find_line(self):
         if len(self.points) < 2 or len(self.triangles) == 0:
              return
         maxk = -1
         point1 = None
         point2 = None
         for i in range(0, len(self.points)):
             for j in range(i +  1, len(self.points)):
                 fx = self.points[i].x
                 fy = self.points[i].y
                 sx = self.points[j].x
                 sy = self.points[j].y
                 k = 0
                 for p in range(0, len(self.triangles)):    
                     if self.cross(fx, fy, sx, sy, p):
                         k += 1
                 if k > maxk:
                      maxk = k
                      point1 = self.points[i]
                      point2 = self.points[j]
         if maxk == 0:
              return
         if self.solve_line != None:
              self.canv.delete(self.solve_line)
         self.solve_line = self.canv.create_line(point1.x,
                                                 point1.y,
                                                 point2.x,
                                                 point2.y,
                                                 fill='green')
         
    def cross(self, x1, y1, x2, y2, p):
        t = self.triangles[p]
        return self.cross_lines(x1, y1, x2, y2, t.x1, t.y1, t.x2, t.y2) or\
               self.cross_lines(x1, y1, x2, y2, t.x1, t.y1, t.x3, t.y3) or\
               self.cross_lines(x1, y1, x2, y2, t.x3, t.y3, t.x2, t.y2)

    def multy(self,ax,ay,bx,by):
        return ax*by-bx*ay
    def cross_lines(self, x1, y1, x2, y2, x3, y3, x4, y4):
        eps = 1e-10
        v1=self.multy(x4-x3,y4-y3,x1-x3,y1-y3)
        v2=self.multy(x4-x3,y4-y3,x2-x3,y2-y3)
        v3=self.multy(x2-x1,y2-y1,x3-x1,y3-y1)
        v4=self.multy(x2-x1,y2-y1,x4-x1,y4-y1)
        return (v1*v2)<eps and (v3*v4)<eps
    def enter_handler(self, event):
        self.xlab["text"] = "x: " + str(event.x)
        self.ylab["text"] = "y: " + str(event.y)
    def belongs_to_line(self, x1, y1, x2, y2, x3, y3):
        return y3 * (x2 - x1) == (y2 - y1) * x3 + y1 * x2 - y2 * x1
    def delete(self):
         self.canv.delete("all")
         self.triangles = []
         self.points = []
         
    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        #self.columnconfigure(3, weight=1) 
        self.rowconfigure(2, weight=1) 

        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind("<Button-1>", self.draw_handler) 

        size_lab = Label(self, text="Choose drawing mode: ")
        size_lab.grid(row=0, column=0, padx=5)
        self.point_but.grid(row=0, columnspan = 2, column=1)
        self.triangle_but.grid(row=0, columnspan = 2, column=3)
        self.canv.bind("<Motion>", self.enter_handler)
        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.delete(),
                           activebackground = "#555",
                           background="#105",
                           foreground="red",
                           padx="15",
                           pady="5",
                           font="16")
        clear_btn.grid(row=0, column=5, sticky=W)
        lab = Label(self, text="Enter next point: ")
        lab.grid(row=1, column=0, padx=5)
        labx = Label(self, text="x: ")
        labx.grid(row=1, column=1, padx=5)
        self.x_e.grid(row = 1, column = 2, sticky =W)
        laby = Label(self, text="y: ")
        laby.grid(row=1, column=3, padx=5)
        self.y_e.grid(row = 1, column = 4, sticky =W)
        but_enter =  Button(self, text="Enter", width=10,
                           command=lambda: self.enter(),
                           activebackground = "#555",
                           background="#105",
                           foreground="red",
                           padx="15",
                           pady="5",
                           font="16")
        but_enter.grid(row=1, column=5, sticky=W)
        self.xlab.grid(row = 3, column = 0, padx=5)
        self.ylab.grid(row = 3, column = 1, padx=5)
        find_but = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"),
                           activebackground = "#555",
                           background="#105",
                           foreground="red",
                           padx="15",
                           pady="5",
                           font="16")
def show_error(message):
    mb.showwarning("Ошибка", message)
def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()
if __name__ == '__main__':
    main()
