class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name)
        stroka = file.read()
        file.close()
        return stroka

    def add(self, *products):
        for t in products:
            proverka = Shop.get_products(self)
            if t.name in proverka:
                print(f'Продукт {t.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{t}\n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)

s1.add(p1, p2, p3)
print(s1.get_products())

# proverka = open(self.__file_name)
# if t in proverka:
#     print(f'Продукт {t} уже есть в магазине')
#     proverka.close()
# else:
# # proverka.close()