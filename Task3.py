class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:


    def __init__(self):
        self.products = []
        self.income = 0


    def add(self, product, amount):
        if type(product) != Product:
            raise ValueError('Incorrect product type!')
        else:
            product.price = product.price * 1.3
            self.products.append({'product': product, 'amount': amount})


    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type != 'name' and identifier_type != 'type':
            raise ValueError('Incorrect identifier type!')
        if percent > 100 or percent < 0:
            raise ValueError('Invalid percentage!')
        for p in self.products:
            if identifier_type == 'type' and p['product'].type == identifier:
                p['product'].price *= (100-percent)/100
            elif identifier_type == 'name' and p['product'].name == identifier:
                p['product'].price *= (100-percent)/100


    def sell_product(self, product_name, amount):
        for p in self.products:
            if p['product'].name == product_name:
                if p['amount'] <= 0:
                    raise ValueError('No products left')
                else:
                    p['amount'] -= amount
                    self.income += p['product'].price * amount
                    return
        raise ValueError('There is no such product')


    def get_income(self):
        return self.income


    def get_all_products(self):
        return [(p['product'].name, p['product'].type, p['product'].price, p['amount']) for p in self.products]

    def get_product_info(self, product_name):
        for p in self.products:
            if p['product'].name == product_name:
                return (p['product'].name, p['amount'])
        raise ValueError('There is no such product')

product1 = Product('drinks', 'Cola', 30)
product2 = Product('snacks', 'Lays', 20)
product3 = Product('drinks', 'Pepsi', 35)

store = ProductStore()

store.add(product1, 4)
store.add(product2, 1)
store.add(product3, 5)

store.set_discount('Cola', 10, 'name')

store.sell_product('Pepsi', 2)
store.sell_product('Cola', 1)

print(store.get_income())

print(store.get_all_products())

print(store.get_product_info('Lays'))
