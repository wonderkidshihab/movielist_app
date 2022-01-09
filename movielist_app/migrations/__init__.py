class shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am a area mathod of shape class")


class Triangle (shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("I am area of triangle : ", area)


class rectriangle (shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("I am area of rectriangle : ", area)


t1 = Triangle(10, 20)
t1.area()


r1 = rectriangle(11, 22)
r1.area()
