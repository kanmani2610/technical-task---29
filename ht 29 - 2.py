class Restaurant:
    def __init__(self):
        self.menu = {}

    def add_item(self, item, price):
        self.menu[item] = price

    def get_menu(self):
        return self.menu


class Delivery:
    def __init__(self):
        self.rider_details = {}

    def assign_rider(self, rider, order_id):
        self.rider_details[order_id] = rider

    def get_rider(self, order_id):
        return self.rider_details.get(order_id, "No rider assigned")


class Order(Restaurant, Delivery):
    def __init__(self):
        Restaurant.__init__(self)
        Delivery.__init__(self)

    def place_order(self, item, rider):
        if item in self.menu:
            order_id = f"Order#{len(self.rider_details) + 1}"
            self.assign_rider(rider, order_id)
            return f"{item} ordered. {rider} will deliver. Order ID: {order_id}"
        return "Item not available."
system = Order()
system.add_item("IDLY", 10)
system.add_item("SAMBHAR", 5)
print(system.get_menu())  
print(system.place_order("Pizza", "Rider1"))  
print(system.get_rider("Order#1")) 
