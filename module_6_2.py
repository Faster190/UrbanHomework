class Vehicle:
    __COLOR_VARIANTS = ["red", "green", "blue", "black", "white"]

    def __init__(self, name, model, color, power):
        self.owner = name
        self.__model = model
        self.__engine_power = power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f"Владелец: {self.owner}", sep="\n")

    def set_color(self, new_color):
        verify = True
        for i in range(len(self.__COLOR_VARIANTS)):
            if self.__COLOR_VARIANTS[i] == new_color.lower():
                self.__color = new_color
                verify = False
        if verify:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
