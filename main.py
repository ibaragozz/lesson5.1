# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.


class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item = {}

    def add_item(self, item):
        self.item[item] = price

    def remove_item(self, item):
        if item in self.item:
            del self.item[item]

    def get_price(self, item):
        if item in self.item:
            return self.item[item]
        else:
            return None

    def update_price(self, item, new_price):
        if item in self.item:
            self.item[item] = new_price
        else:
            print(f"Товара {item} нет в ассортименте")

magnit = Store('Магнит', 'Москва')
kb = Store('КрасноБелое', 'Мурманск')
lenta = Store('Лента', 'Апатиты')
bristol = Store('Бристоль', 'Неман')

magnit.add_item('яблоки', 50)
magnit.add_item('бананы', 75)
kb.add_item('яблоки', 48)
kb.add_item('бананы', 70)
lenta.add_item('яблоки', 57)
lenta.add_item('бананы', 69)
bristol.add_item('яблоки', 44)
bristol.add_item('бананы', 80)

print(magnit.get_price('яблоки'))
print(kb.get_price('яблоки'))
print(lenta.get_price('яблоки'))
print(bristol.get_price('яблоки'))
print(magnit.get_price('бананы'))
print(kb.get_price('бананы'))
print(lenta.get_price('бананы'))
print(bristol.get_price('бананы'))