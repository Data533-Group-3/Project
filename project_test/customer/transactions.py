from datetime import datetime
class Transaction():
    def __init__(self, items_name=None, items_value=None, transaction_time=datetime.now()):
        self.items_name=items_name
        self.items_value=items_value
        self.transaction_time=transaction_time
        self.order_review=""
        self.order_rate=None
    def write_review(self, review):
        self.order_review=self.order_review+review
    def rate_order(self, rate):
        self.order_rate=rate
    def reorder(self):
        return Transaction(self.items_name, self.items_value, datetime.now())
    def get_order_info(self):
        info_dict={
            "name": self.items_name,
            "value": self.items_value,
            "transaction time": self.transaction_time,
            "rate": self.order_rate,
            "review": self.order_review
        }
        return info_dict

def new_transaction():
    items_name=input("Please input item name list")
    items_value=input("Please input items value list")
    return Transaction(items_name, items_value)

def new_review(Transaction):
    review=input("Please input your review about this order")
    Transaction.write_review(review)
    return Transaction.order_review()
def new_rate(Transaction, rate):
    rate=input("Please rate this order")
    Transaction.rate_order(rate)
    return Transaction.order_rate()
def reorder(Transaction):
    Transaction.reorder()


