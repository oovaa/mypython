import time


class item:
    num = 0
    all = []

    def test(self) -> bool:
        x = {"a", "b", "c"}
        y = {"f", "e", "d", "c", "b", "a"}
        z = x.issubset(y)
        print(z)

    def __init__(self, quantity: int, price: int, name: str = "car"):
        assert price >= 0, "price is less than 0"
        assert quantity >= 0, "quantity is less than 0"
        item.num += 1

        self.quantity = quantity
        self.price = price
        self.name = name
        item.all.append(self)

    #   print(f"u just created a {name}")

    def calcprice(self):
        return int(self.quantity) * self.price

    def __repr__(self):
        return self.name


# n=time.time()
# print(n)
# item1.quantity = 12
# item1.name = "car"
# item1.price = 4000
# print(item1.quantity)
# print(item1.name.upper())
# print(item1.calcprice())
# item1.test()
# a=time.time()
# print(a)
# print("a-n",a-n)
item1 = item(4, 4000, "lambo")
item2 = item(12, 123, "ponan")
item3 = item(5, 5151, "motosicly")
item4 = item(1, 10000, "firari")
item5 = item(20, 234, "toy car")

print(item.all)
print("(here)".replace("(", ""))
