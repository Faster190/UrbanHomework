import matplotlib.pyplot as plt
from random import randint


x = sorted([randint(0, 100) for _ in range(30)])
y = sorted([randint(0, 100) for _ in range(30)])
print(x, y)

# создаем рисунок fig и 1 график на нём ax, plt.subplots(1, 1, 1)
fig, ax = plt.subplots()

# задаем значение точек по x и y, меняем цвет линии на красный, точки будут выделены маркерами для наглядности
ax.plot(x, y, color="red", marker="o")

# даём названия осям
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")

# ограничиваем разметку оси и обозначаем её шаг
ax.set_xticks(range(20, 80, 5))
ax.set_yticks(range(20, 80, 5))

# добавляем пунктирную сетку
ax.grid(linestyle="--")

# запускаем окно вывода графика
plt.show()
