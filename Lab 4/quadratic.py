import math

class Quadratic():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def get_discriminant(self):
        return self.b**2 - 4*self.a*self.c

    def get_root1(self):
        return (self.b * (-1) + math.sqrt(self.get_discriminant())) / (2 * self.a)

    def get_root2(self):
        return (self.b * (-1) - math.sqrt(self.get_discriminant())) / (2 * self.a)
