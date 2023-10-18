class Worker:
    def __init__(self, height, weight, age, ex):
        self.height = height
        self.weight = weight
        self.age = age

    def set_worker(self, height, weight, age, ex):
        self.height = height
        self.weight = weight
        self.age = age
        self.ex = ex


    def get_worker(self):
        return [self.height, self.weight, self.age, self.ex]