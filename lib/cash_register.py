#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = list()

    @property
    def discount (self):
        return self._discount
    
    @discount.setter
    def discount(self, discount):
        self._discount = discount


    def add_item(self, title, price, quantity=1):
        self.last_items_total = price * quantity
        self.total += price * quantity
        self.items.extend([title] * quantity)
        

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            cash_discount = (float(self.discount) * self.total) / 100
            self.total = self.total - cash_discount
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total = self.total - self.last_items_total