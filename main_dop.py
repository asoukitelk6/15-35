'''*Дополнительное задание:
Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети
имеет свои особенности, но также существуют общие характеристики, такие как адрес,
название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет
использовать для создания различных магазинов.

Шаги:
1. Создай класс Store:
-Атрибуты класса:
name: название магазина.
address: адрес магазина.
items: словарь, где ключ - название товара, а значение - его цена. Например,
{'apples': 0.5, 'bananas': 0.75}.
Методы класса:
__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь
дляitems`.
-  метод для добавления товара в ассортимент.
метод для удаления товара из ассортимента.
метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
метод для обновления цены товара.

2. Создай несколько объектов класса Store:
Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый
 из них несколько товаров.

3. Протестировать методы:
Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
обнови цену, убери товар и запрашивай цену.'''

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

    def new_product (self,product,price):#метод для добавления товара в ассортимент.название товара, а значение - его цена
        assortiment = {'product': product, 'price': price}
        self.items.append(assortiment)
        print(f'Добавлен товар "{product}" с ценой "{price}" в магазин "{self.name}"')

    def del_product (self,product):#метод для удаления товара из ассортимента.
        for assortiment in self.items:
            if assortiment['product'] == product:
                self.items.remove(assortiment)
                print(f'Товар "{product}" удален из базы')
                break
        else:
            print(f'Товар "{product}" отсутствует')

    def price_product (self,product):#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
        for assortiment in self.items:
            if assortiment['product'] == product:
                print(f'У товара "{product}" цена "{assortiment["price"]}"')
                break
        else:
            print(f'Товар "{product}" отсутствует')

    def new_price_product (self,product,new_price):#метод для обновления цены товара.
        for assortiment in self.items:
            if assortiment['product'] == product:
                assortiment['price'] = new_price
                print(f'У товара "{product}" новая цена "{new_price}"')
                break
        else:
            print(f'Товар "{product}" отсутствует')

    def list_assortiment (self):#вывода списка текущих (не выполненных) задач.
        if not self.items:
            print(f'Товары отсутствуют в магазине {self.name}')
        else:
            print(f'В магазине {self.name} по адресу {self.address} есть товары:')
            n = 1
            for assortiment in self.items:
                print(f'{n}) {assortiment["product"]}, цена - {assortiment["price"]}')
                n += 1



mag1 = Store('Гроздь','г.Саратов')
mag2 = Store('Пятерочка','г.Москва')
mag3 = Store('Магнит','г.Краснодар')

mag1.new_product('Молоко 2.5',55)
mag1.new_product('Молоко 3.2',80)
mag1.new_product('сыр тильзитер',750)
mag1.new_product('сливочное масло',1000)

mag2.new_product('Молоко',80)
mag2.new_product('сыр',600)
mag2.new_product('масло',200)

mag3.new_product('Вода',20)
mag3.new_product('Сахар',60)
mag3.new_product('Мука',100)

mag2.list_assortiment()
mag1.list_assortiment()
mag3.list_assortiment()

mag1.new_price_product('Молоко',55)
mag1.new_price_product('сыр тильзитер',650)
mag1.del_product('Молоко 3.2')
mag1.del_product('Молоко 3.3')
mag1.price_product('сливочное масло')
