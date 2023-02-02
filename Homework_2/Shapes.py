import math

class Polygon:
    def __init__(self, side_length, num_faces):
        self.side_length = side_length
        self.num_faces = num_faces
        
    def surface_area(self):
        return (self.num_faces * (self.side_length * 2)) / (4 * math.tan(math.pi / self.num_faces))
    
    def volume(self):
        return (self.num_faces * (self.side_length * 2) * self.height) / (4 * math.tan(math.pi / self.num_faces))

