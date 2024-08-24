from threading import Thread
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables_):
        self.q = queue.Queue()
        self.tables = tables_

    def guest_arrival(self, *guests_):
        for guest in guests_:
            verify = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                    verify = False
                    break
            if verify:
                print(f"{guest.name} в очереди")
                self.q.put(guest)

    def discuss_guests(self):
        for table in self.tables:
            if table.guest is not None:
                table.guest.start()
        verify = True
        while not self.q.empty() or verify:
            verify = False
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    table.guest.join()
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    if self.q.empty():
                        table.guest = None
                    else:
                        table.guest = self.q.get()
                        print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
                        table.guest.start()
                if table.guest is not None:
                    verify = True



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
