from points import Point3D

class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Cube:
    def __init__(self, center, side_length):
        self.center = center
        self.side_length = side_length

class Pyramid:
    def __init__(self, base_vertices, apex):
        self.base_vertices = base_vertices
        self.apex = apex
