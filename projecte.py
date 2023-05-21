class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_product(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print("Checkout completed. Total amount: $", total)
        self.shopping_cart.products = []

def main():
    
    product1 = Product("Shirt", 25)
    product2 = Product("Jeans", 50)
    product3 = Product("Shoes", 80)

    
    customer = Customer("mohan krishna","mksompalli@gmail.com")

    
    customer.add_to_cart(product1)
    customer.add_to_cart(product2)
    customer.add_to_cart(product3)


    customer.checkout()


if __name__ == '__main__':
    main()
