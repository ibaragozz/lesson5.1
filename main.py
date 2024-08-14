class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_price(self, item):
        return self.items.get(item, None)

    def update_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
        else:
            print(f"Товара {item} нет в ассортименте")

# Создаем магазины
magnit = Store('Магнит', 'Москва')
kb = Store('КрасноБелое', 'Мурманск')
lenta = Store('Лента', 'Апатиты')
bristol = Store('Бристоль', 'Неман')

# Добавляем товары
magnit.add_item('яблоки', 50)
magnit.add_item('бананы', 75)
kb.add_item('яблоки', 48)
kb.add_item('бананы', 70)
lenta.add_item('яблоки', 57)
lenta.add_item('бананы', 69)
bristol.add_item('яблоки', 44)
bristol.add_item('бананы', 80)

# Проверяем цены
print('Цена на яблоки в магазине Магнит:', magnit.get_price('яблоки'))
print('Цена на яблоки в магазине КрасноБелое:', kb.get_price('яблоки'))
print('Цена на яблоки в магазине Лента:', lenta.get_price('яблоки'))
print('Цена на яблоки в магазине Бристоль:', bristol.get_price('яблоки'))

print('Цена на бананы в магазине Магнит:', magnit.get_price('бананы'))
print('Цена на бананы в магазине КрасноБелое:', kb.get_price('бананы'))
print('Цена на бананы в магазине Лента:', lenta.get_price('бананы'))
print('Цена на бананы в магазине Бристоль:', bristol.get_price('бананы'))
