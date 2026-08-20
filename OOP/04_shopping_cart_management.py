"""
4. Shopping Cart Management
"""

class Cart:
    def __init__(self,name,item,item_price,total):
        self.name=name
        self.item=item
        self.total=total
        self.item_price=item_price


    def add_items(self):

        self.total=sum(self.item_price)

    def remove_items(self,ittm):

        for x in ittm:
            if x in self.item:
                idx=self.item.index(x)
                self.item.pop(idx)
                self.item_price.pop(idx)
                print(f"{x} has been removed from the cart")

            else:
                print(f"Item not found in the list.")
        self.total=sum(self.item_price)
        print(f"\nCustomer : {self.name}\n")
        print("Your final cart items are :\n")
        for i in range(len(self.item)):
            print(f"{self.item[i]} : Rs {self.item_price[i]}")
        print(f"Your total cart value is : {self.total}")

nm=input("Enter your name : ")
itm=input(f"Enter the names of the items u want to purchase separated by space: \n").split()
price=list(map(float,input("Enter the individual prices of the entered items separated by space: \n").split()))
ttl=0.0

crt=Cart(nm,itm,price,ttl)
crt.add_items()

itm=input("Enter the items u want to remove seprated by space (This is the last chance, no more modification is supported): ").split()
crt.remove_items(itm)
