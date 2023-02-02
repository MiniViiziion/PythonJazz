import csv
from Shapes3D import Cube, Cuboid, Cylinder, Sphere, Prism

class Solver:
    def __init__(self, file_path):
        self.shapes = []
        self.total = 0
        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'cube':
                    self.shapes.append(Cube(float(row[1])))
                elif row[0] == 'cuboid':
                    self.shapes.append(Cuboid(float(row[1]), float(row[2]), float(row[3])))
                elif row[0] == 'cylinder':
                    self.shapes.append(Cylinder(float(row[1]), float(row[2])))
                elif row[0] == 'sphere':
                    self.shapes.append(Sphere(float(row[1])))
                elif row[0] == 'prism':
                    self.shapes.append(Prism(float(row[1]), float(row[2]), float(row[3])))
                elif row[0] == 'area':
                    for shape in self.shapes:
                        self.total += shape.surface_area()
                    self.total * int(row[1])
                elif row[0] == 'volume':
                    for shape in self.shapes:
                        self.total += shape.volume()
                    self.total * int(row[1])

    def get_total(self):
        return self.total

if __name__ == '__main__':
    import sys
    solver = Solver(sys.argv[1])
    print(f'The sum of measurements is {solver.get_total():,.2f}.')
