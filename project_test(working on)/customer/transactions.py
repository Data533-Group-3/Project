from datetime import datetime
class transaction():
    def __init__(self, customer_id=None, transaction_id=None, items_name=None, items_quantity=None, items_price=None, items_value=None, transaction_time=datetime.now(), order_review=None, order_rate=None):
        self.customer_id=customer_id
        self.transaction_id=transaction_id
        self.items_name=items_name
        self.items_quantity=items_quantity
        self.items_price=items_price
        self.items_value=items_value#value=quantity*price
        self.transaction_time=transaction_time
        self.order_review=order_review
        self.order_rate=order_rate
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


def get_order_total(Transaction):
    value=Transaction.get_order_info()['value']#should be a 'a,b,c' format string
    #value=value.split(',')
    total_consumption=0
    #for i in value:
        #total_consumption=total_consumption+eval(i)
    total_consumption=sum(eval(value))
    return total_consumption

def new_review(Transaction):
    review=input("Please input your review about this order\n")
    Transaction.write_review(review)
    return Transaction
def new_rate(Transaction):
    rate=input("Please rate this order from a scale of 1 to 5 stars\n")
    Transaction.rate_order(rate)
    return Transaction
