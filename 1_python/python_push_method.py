class Order :
    def __init__(self, order_id, customer_name, order_date, total_amount):
      try :
        self.order_id = str(order_id)
        self.customer_name = str(customer_name)
        self.order_date = str(order_date)
        self.total_amount = float(total_amount)
      except:
        print('total_amount kudu angka')

    def calculate_tax(self, tax_rate) :
        self.tax_rate = tax_rate
        self.tax_amount = self.total_amount * self.tax_rate
        return self.tax_amount

    def display_order(self) :
        string = f"Order ID: {self.order_id}\nCustomer Name: {self.customer_name}\nOrder Date: {self.order_date}\
                  \nTotal Amount: {self.total_amount}\nTax Amount: {self.tax_amount}"
        print(string)


class OrderManager(Order):
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append([order.order_id, order.customer_name, order.order_date, order.total_amount, order.tax_amount])
        print(f"Order {order.order_id} added.")

    def calculate_total_revenue(self):
        total_revenue = 0
        for order in self.orders:
            total_revenue += order[3]
        return f"Total Revenue : {total_revenue}"

    def calculate_total_tax(self):
        total_tax = 0
        for order in self.orders:
            total_tax += order[4]
        return f"Total Tax : {total_tax}"

    def list_orders(self):
        print(["order_id", "customer_name", "order_date", "total_amount", "tax_amount"])
        for order in self.orders:
            print(order)

## SET UP OBJECT (ORDER)
order_1 = Order(1, "John Doe", "2023-05-01", 12)
order_2 = Order(2, "Jane Smith", "2023-05-02", 15)

list_order = [order_1, order_2]

## CALCULATING TAX IN EVERY OBJECT
tax_rate = 0.1
for i in list_order :
    i.calculate_tax(tax_rate)

## DISPLAYING EVERY ORDER
for i in list_order :
    print("##########################")
    i.display_order()

print("##########################")

## ADDING ORDER TO ORDER MANAGER

manager = OrderManager()
manager.add_order(order_1)
manager.add_order(order_2)

## CALCULATING TOTAL REVENUE

manager.calculate_total_revenue()

## CALCULATING TOTAL TAX

manager.calculate_total_tax()

## DISPLAYING ORDERS IN ORDER MANAGER IN LIST
manager.list_orders()