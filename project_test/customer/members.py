class member:
    def __init__(self, name=None, id=None, email=None, phone=None, address=None):
        self.__name=name
        self.__id=id
        self.__email=email
        self.__phone=phone
        self.__address=address
        self.deposit=0.0
        self.account_credits =0.0
        self.total_consumption=0.0
        self.is_premium=False
    def check_premium_status(self):
        if self.total_consumption>500000:
            self.is_premium=True
            return True
    def add_deposit(self, value):
        self.deposit=self.deposit+ value
    def add_credits(self, value):
        self.account_credits=self.account_credits+value

    def add_consumption(self, value):
        self.total_consumption=self.total_consumption+value
        # regular member: $100 equals to 1 credit; premium member: $10 equals to 1 credit
        if self.check_premium_status():
            new_credit=value/10
        else:
            new_credit=value/100 
        self.add_credits(new_credit)

    def get_member_info(self):
        info_dict={
            "name": self.__name,
            "id": self.__id,
            "email": self.__email,
            "phone": self.__phone,
            "address": self.__address,
            "credits": self.account_credits,
            "deposit": self.deposit,
            "total consumption amount": self.total_consumption
        }
        return info_dict
    def change_email(self, email):
        self.__email=email
    def change_phone(self, phone):
        self.__phone=phone
    def change_address(self, address):
        self.__address=address


def new_member():
    name=input("Please input customer name")
    id=input("Please input customer id")
    email=input("Please input customer email")
    phone=input("Please input customer phone number")
    address=input("Please input customer address")
    return member(name, id, email, phone, address)

def deactivate_member(member):
    del member

        