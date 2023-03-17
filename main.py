import tkinter as tk
import math

class Cube:
    def __init__(self, size):
        self.size = size
        self.vertices = [
            (-size/2, -size/2, -size/2),
            (size/2, -size/2, -size/2),
            (size/2, size/2, -size/2),
            (-size/2, size/2, -size/2),
            (-size/2, -size/2, size/2),
            (size/2, -size/2, size/2),
            (size/2, size/2, size/2),
            (-size/2, size/2, size/2),
        ]
        self.faces = [
            (0, 1, 2, 3),
            (1, 5, 6, 2),
            (5, 4, 7, 6),
            (4, 0, 3, 7),
            (0, 4, 5, 1),
            (3, 2, 6, 7),
        ]
        self.colors = [
            '#ff0000', # red
            '#00ff00', # green
            '#0000ff', # blue
            '#ffff00', # yellow
            '#ff00ff', # magenta
            '#00ffff', # cyan
        ]
        self.angle = 0

    def rotate(self, dx, dy, dz):
        sin_x = math.sin(dx)
        cos_x = math.cos(dx)
        sin_y = math.sin(dy)
        cos_y = math.cos(dy)
        sin_z = math.sin(dz)
        cos_z = math.cos(dz)
        for i, vertex in enumerate(self.vertices):
            x, y, z = vertex
            # rotate around x-axis
            y, z = cos_x*y - sin_x*z, sin_x*y + cos_x*z
            # rotate around y-axis
            x, z = cos_y*x - sin_y*z, sin_y*x + cos_y*z
            # rotate around z-axis
            x, y = cos_z*x - sin_z*y, sin_z*x + cos_z*y
            self.vertices[i] = (x, y, z)

    def draw(self, canvas):
        for face_index, face in enumerate(self.faces):
            vertices = [self.vertices[i] for i in face]
            coords = [(100 + x + y) for vertex in vertices for x, y in zip(vertex, (0,0,0))]
            color = self.colors[(face_index + int(self.angle/5)) % len(self.colors)]
            canvas.create_polygon(*coords, fill=color)

    def update(self):
        self.angle += 1
        self.rotate(math.radians(1), math.radians(2), math.radians(3))

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='#000000')
        self.canvas.pack()
        self.cube = Cube(50)
        self.root.after(0, self.animation)

    def animation(self):
        self.cube.update()
        self.canvas.delete(tk.ALL)
        self.cube.draw(self.canvas)
        self.root.after(10, self.animation)

if __name__ == '__main__':
    app = App()
    app.root.mainloop()
