class Building:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, *args):
        self.info = args

    def __eq__(self, other):
        return self.info[1] == other.info[1] and self.info[2] == other.info[2]

    def __del__(self):
        print(self.info[0], "снесён, но он останется в истории")


b1 = Building('ЖК Эльбрус', 8, "High")
b2 = Building('ЖК Акация', 8, "High")
b3 = Building('ЖК Матрёшки', 2, "Small")
print(b1 == b2)
print((b1 == b3))
del b2
del b3
print(Building.houses_history)
