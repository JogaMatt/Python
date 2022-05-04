class Store:
    products = []
    def __init__(self, name):
        self.name = name

    def add_product(self, new_product):
        pass

    def sell_product(self, id):
        pass

    def inflation(self, percent_increase):
        pass

    def set_clearance(self, category, percent_discount):
        pass

class Product:
    def __init__(self, name, price, catagory):
        self.name = name
        self.price = price
        self.catagory = catagory

    def update_price(self, percent_change, is_increased):
        self.percent_change = 0.10
        self.is_increased = True

    def print_info(self):
        pass

new_store = Store("JogaStore")