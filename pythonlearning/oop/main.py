class Point:
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print(str(cls))
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point(1, 2)
pt.set_coords(1, 2)
print(pt.get_coords())

#pt1 = Point()
#pt1.set_coords(4, 5)
#
#pt2 = Point()
#pt2.set_coords(3, 4)
#
#print(pt1.__dict__)
#print(pt2.__dict__)
