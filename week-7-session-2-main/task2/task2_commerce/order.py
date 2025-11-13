# write code to import product and customer
from customer import Customer
from product import Product

# define a Order class with the following fields:
# (1) order_id: a unique order id
# (2) customer: an instance of Customer
# (3) products: a list of Product instances
class Order():
    def __init__(self,order_id,customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def __str__(self):
        string = f"Order ID: {self.order_id} \n Customer: {self.customer.name} ({self.customer.customer_id}) \n Products: \n"
        for product in self.products:
            string = string + f"- {product.name} - £{product.price}"
        return string




# this class has the following methods:
# (1) add_product(product): add a Producet instance to the order. Products are added only through this method
# (2) __str__: return the order id, customer, and list of produces
#     Example output
#     Order ID: O456
#     Customer: Jane Doe (ID: C123)
#     Products:
#     - Laptop - £999.99
#     - Mouse - £25.99





# When done, 
# (1) create an instance of Customer with your details
# (2) create two instances of Product, any product that you like
# (3) create an instance of Order, with a order_id and the customer you just created
# (4) add the products you have just created to the order
# (5) print(order)
customer1242 = Customer("Dan",1242)
product1 = Product("Football",45)
order = Order(3231,customer1242)
order.add_product(product1)
print(order)