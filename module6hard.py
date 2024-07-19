from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, rgb, *sides):
        self.__sides = []
        if len(sides) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(sides[i])
            #print("Sides count == New sides")
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)
            #print("All sides = 1")
        if len(rgb) != 3:
            #print("Incorrect number of color arguments. The color is set by default")
            self.__color = [255, 255, 255]
        elif self.__is_valid_color(rgb[0], rgb[1], rgb[2]):
            self.__color = [rgb[0], rgb[1], rgb[2]]
        else:
            #print("Invalid value of color. The color is set by default")
            self.__color = [255, 255, 255]
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            #print("Invalid value of color")
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *args):
        verify = True
        if len(args) == self.sides_count:
            for i in range(len(args)):
                if not isinstance(args[i], int) or args[i] < 1:
                    #print("Incorrect data input")
                    verify = False
                    break
        else:
            verify = False
            #print("Wrong count of sides")
        return verify

    def get_sides(self):
        return self.__sides

    def __len__(self):
        len_ = 0
        for i in range(len(self.__sides)):
            len_ += self.__sides[i]
        return len_

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = []
            for i in range(self.sides_count):
                self.__sides.append(new_sides[i])


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius * self.__radius)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *sides):
        super().__init__(rgb, *sides)
        self.__high = self.__calcul_high()

    def get_square(self):
        p = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2
        list_ = self.get_sides()
        return sqrt(p * (p - list_[0]) * (p - list_[1]) * (p - list_[2]))

    def __calcul_high(self):
        list_ = self.get_sides()
        min_ = list_[0]
        for i in range(1, 3):
            if list_[i] < min_:
                min_ = list_[i]
        return (self.get_square() * 2) / min_

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__high = self.__calcul_high()


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *sides):
        if len(sides) == 1:
            list_ = [sides[0]]
            for i in range(1, 12):
                list_.append(list_[0])
            super().__init__(rgb, *list_)
        else:
            super().__init__(rgb, *sides)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] * sides[0] * sides[0]


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
