import math
from Shapes_2 import Polygon

class Cuboid:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        
    def surface_area(self):
        return (2 * (self.width * self.height + self.height * self.depth + self.depth * self.width))
    
    def volume(self):
        return self.width * self.height * self.depth

class Cube(Cuboid):
    def __init__(self, side_length):
        super().__init__(side_length, side_length, side_length)
        
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius * 2
    
    def volume(self):
        return math.pi * (self.radius * 2) * self.height

class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)
    
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

class Prism(Polygon):
    def __init__(self, side_length, num_faces, height):
        super().__init__(side_length, num_faces)
        self.height = height
