from datetime import datetime
class transaction():
    def __init__(self, customer_id=None, transaction_id=None, items_name=None, items_quantity=None, items_price=None, items_value=None, transaction_time=datetime.now()):
        self.customer_id=customer_id
        self.transaction_id=transaction_id
        self.items_name=items_name
        self.items_quantity=items_quantity
        self.items_price=items_price
        self.items_value=items_value#value=quantity*price
        self.transaction_time=transaction_time
        self.order_review=""
        self.order_rate=None
    def write_review(self, review):
        self.order_review=self.order_review+review
    def rate_order(self, rate):
        self.order_rate=rate
    #def return_goods(self):
        #pass
    
    def get_order_info(self):
        info_dict={
            "customer id": self.customer_id,
            "name": self.items_name,
            "quantity": self.items_quantity,
            "price": self.items_price,
            "value": self.items_value,
            "transaction time": self.transaction_time,
            "rate": self.order_rate,
            "review": self.order_review
        }
        return info_dict

"""
def create_new_transaction():
    customer_id=input("Please input your member id")
    items_name=[]
    items_quantity=[]
    items_price=[]
    items_value=[]
    while True:
        item_name=input("Please input item name")
        item_quantity=input("Please input your item quantity")
        item_price=input("Please input yor item price")

        items_name.append(item_name)
        items_quantity.append(item_quantity)
        items_price.append(item_price)
        items_value.append(float(item_quantity)*float(item_price))
        add_more=input("Do you want to add more items? yes/no")
        if add_more.lower()=='no':
            break
    return transaction(customer_id, items_name, items_quantity, items_price, items_value)
"""

def new_review(Transaction):
    review=input("Please input your review about this order")
    Transaction.write_review(review)
    return Transaction.order_review
def new_rate(Transaction, rate):
    rate=input("Please rate this order")
    Transaction.rate_order(rate)
    return Transaction.order_rate
#def reorder(Transaction):
    #Transaction.reorder()


#def deposit_deduction