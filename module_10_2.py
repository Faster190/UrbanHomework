import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.count_of_enemy = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.count_of_enemy > 0:
            self.count_of_enemy -= self.power
            self.days += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.days} днень(дня)..., осталось {self.count_of_enemy} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
