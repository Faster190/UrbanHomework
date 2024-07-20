class Product:
    def __init__(self, name, weigh, category):
        self.name = name
        self.weigh = weigh
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weigh}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'a')
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        string = self.get_products()  # Строка с информацией из файла
        list_ = []  # Список для названий продуктов из файла
        word = ""  # Временное хранилище имени продукта
        comma = True  # Указатель на участок строки с именем продукта
        for i in range(len(string)):  # Заносим в отдельный список названия продуктов из файла
            if string[i] == ',':
                if comma:
                    list_.append(word)
                word = ""
                comma = False
            if comma:
                word += string[i]
            if string[i] == '\n':
                comma = True
        file = open(self.__file_name, 'a')
        for i in range(len(products)):
            verify = True
            for j in range(i - 1):
                if products[i].name == products[j].name:
                    verify = False
                    print(f"Продукт {products[i].name} уже есть в магазине")
                    break
            if not verify:
                continue
            for j in range(len(list_)):
                if products[i].name == list_[j]:
                    verify = False
                    print(f"Продукт {products[i].name} уже есть в магазине")
                    break
            if verify:
                file.write(f"{str(products[i])}\n")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
