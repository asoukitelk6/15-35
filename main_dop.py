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

    def new_tovar (self,tovar,money):#метод для добавления товара в ассортимент.название товара, а значение - его цена
        assortiment = {'tovar': tovar, 'money': money}
        self.items.append(assortiment)
        print(f'Добавлен товар "{tovar}" с ценой "{money}" в магазин "{self.name}"')

    def del_tovar (self,tovar):#метод для удаления товара из ассортимента.
        for assortiment in self.items:
            if assortiment['tovar'] == tovar:
                self.items.remove(assortiment)
                print(f'Товара "{tovar}" удален из базы')
                break
        else:
            print(f'Товар "{tovar}" отсутствует')

    def money_tovar (self,tovar):#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
        for assortiment in self.items:
            if assortiment['tovar'] == tovar:
                print(f'У товара "{tovar}" цена "{assortiment["money"]}"')
                break
        else:
            print(f'Товар "{tovar}" отсутствует')

    def new_money_tovar (self,tovar,new_money):#метод для обновления цены товара.
        for assortiment in self.items:
            if assortiment['tovar'] == tovar:
                assortiment['money'] = new_money
                print(f'У товара "{tovar}" новая цена "{new_money}"')
                break
        else:
            print(f'Товар "{tovar}" отсутствует')

    def itog_assortiment (self):#вывода списка текущих (не выполненных) задач.
        if not self.items:
            print(f'Товары отсутствуют в магазине {self.name}')
        else:
            print(f'В магазине {self.name} по адресу {self.address} есть товары:')
            n = 1
            for assortiment in self.items:
                print(f'{n}) {assortiment["tovar"]}, цена - {assortiment["money"]}')
                n += 1



mag1 = Store('Гроздь','г.Саратов')
mag2 = Store('Пятерочка','г.Москва')
mag3 = Store('Магнит','г.Краснодар')

mag1.new_tovar('Молоко 2.5',55)
mag1.new_tovar('Молоко 3.2',80)
mag1.new_tovar('сыр тильзитер',750)
mag1.new_tovar('сливочное масло',1000)

mag2.new_tovar('Молоко',80)
mag2.new_tovar('сыр',600)
mag2.new_tovar('масло',200)

mag3.new_tovar('Вода',20)
mag3.new_tovar('Сахар',60)
mag3.new_tovar('Мука',100)

mag2.itog_assortiment()
mag1.itog_assortiment()
mag3.itog_assortiment()

mag1.new_money_tovar('Молоко',55)
mag1.new_money_tovar('сыр тильзитер',650)
mag1.del_tovar('Молоко 3.2')
mag1.del_tovar('Молоко 3.3')
mag1.money_tovar('сливочное масло')
