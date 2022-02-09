class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        customer = str(customer)
        flavor = str(flavor)
        scoops = int(scoops)
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        if scoops in [1, 2, 3] and flavor in self.flavors:
            self.orders.enqueue(order)
            print("Order Created!")
        else:
            print("wrong number of scoops or flavor unavailable. \n")

    def show_all_orders(self):
        print("All Pending Ice Cream Orders: \n")
        for st in self.orders.items:
            print(st)

    def next_order(self):
        f = self.orders.dequeue()
        print("\n Next order up is: ", f)


# q = Queue()
# q.enqueue("a")
# q.enqueue("b")
# q.enqueue("c")

# print("Pass" if (q.size() == 3) else "Fail")

# q.enqueue("d")
# print("Pass" if (q.size() == 4) else "Fail")
# print("Pass" if (q.dequeue() == "a") else "Fail")
# print("Pass" if (q.dequeue() == "d") else "Fail")
# print("Pass" if (q.size() == 2) else "Fail")
# q.show_queue()


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
