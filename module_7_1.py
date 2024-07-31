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
        file.close()
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        list_ = []  # Список для названий продуктов из файла
        new_product = True
        for j in range(len(products)):
            if new_product:
                string = self.get_products()  # Строка с информацией из файла
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
            new_product = True
            for i in range(len(list_)):
                if products[j].name == list_[i]:
                    new_product = False
                    print(f"Продукт {products[j].name} уже есть в магазине")
                    break
            if new_product:
                file = open(self.__file_name, 'a')
                file.write(f"{str(products[j])}\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
