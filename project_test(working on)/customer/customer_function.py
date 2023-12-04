import sqlite3
from datetime import datetime
import uuid
import members
import transactions
try:
    cnx=sqlite3.connect("Supermarket.db")
    cursor=cnx.cursor()
    cursor.execute("CREATE TABLE members (id int, name varchar(100), email varchar(100), phone varchar(20), address varchar(200), credits decimal(100,2), deposit decimal(100, 2), total_consumption amount decimal(100, 2), premium membership status bool, primary key (id));")
    cursor.execute("CREATE TABLE transactions (customer_id int, transaction_id varchar(1000000000000000000), items_name varchar(1000000), items_quantity varchar(100000), items_price varchar(1000000), items_value varchar(100000), transaction_time datetime, primary key(customer_id, transaction_id);)")# order_review varchar(10000000000), order_rate varchar(10000000000),
    sql_query = """SELECT name FROM sqlite_master 
    WHERE type='table';"""
    cursor.execute(sql_query)
    print("List of tables\n")
    print(cursor.fetchall())
except sqlite3.Error as err:
    print(err)
    
def login():
    member_status=input("Are you a new member? Input yes or no")
    if member_status=='yes':
        #'member' object
        global member
        member=members.create_new_member()#prompt info request
        try:
            new_member_info_dict=member.get_member_info()
            id=new_member_info_dict['id']
            name=new_member_info_dict['name']
            email=new_member_info_dict['email']
            phone=new_member_info_dict['phone']
            address=new_member_info_dict['address']
            write_new_member_query="INSERT INTO members VALUES (%s, %s, %s, %s, %s, 0, 0, 0, FALSE)"
            cursor.execute(write_new_member_query, (id, name, email, phone, address))
        except:
            print("Something wrong happened")

    else:
        global member_id
        member_id=input("Please input your customer id")
        
        login_choice=input("Do you want to 1. check your membership information\n2. change your membership information\n3. check your history transactions")
        if login_choice=="1":
            old_member_info_sql="SELECT * from members where id=%s"
            cursor.execute(old_member_info_sql, member_id)
            for row in cursor:
                try:
                    #actually global variable; get old_member
                    member=members.member(row)
                except:
                    print("Some thing went wrong when get the old member object")
        elif login_choice=="2":
            change_prompt=input("You can only change\na: email\nb: phone number\nc: address")
            if change_prompt=="a":
                new_email=input("Please input your new email")
                member.change_email(new_email)
                change_email_sql="UPDATE members set email=%s where id=%s"
                cursor.execute(change_email_sql, new_email, member_id)
            elif change_prompt=="b":
                new_phone=input("Please input your new phone number")
                member.change_phone(new_phone)
                change_phone_sql="UPDATE members set phone=%s where id=%s"
                cursor.execute(change_phone_sql, new_phone, member_id)
            elif change_prompt=="c":
                new_address=input("Please input your new address")
                member.change_address(new_address)
                change_address_sql="UPDATE members set address=%s where id=%s"
                cursor.execute(change_address_sql, new_address, member_id)
        elif login_choice=="3":
            member_transaction_sql="SELECT * from transactions where customer_id=%s"
            cursor.execute(member_transaction_sql, member_id)
            for row in cursor:
                print(row)


def checkout():
    transaction_time=datetime.now()
    customer_id=member_id
    transaction_id=str(transaction_time.minute+transaction_time.second)+str(uuid.uuid4().int)[:4]# randomly generate transactionid according to time and uuid
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
    transaction_record_sql="INSERT INTO transactions VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(transaction_record_sql, (customer_id, transaction_id, items_name, items_quantity, items_price, items_value, transaction_time))
    new_transaction=transactions.transaction(customer_id, transaction_id, items_name, items_quantity, items_price, items_value, transaction_time)
    return new_transaction

def payment_and_rate():
    total_consumption_update_sql="UPDATE members SET total_consumption=%s "
    credits_update_sql="UPDATE members SET credits=%s"
    #deposit_update_sql="UPDATE members SET deposit=%s"
    #member should be a global variable
    login()
    new_transaction=checkout()
    total_consumption=sum(new_transaction.items_value)
    print(f"Your transaction value is {total_consumption}")
    #print(f"Your account deposit is {member.deposit}")
    #deposit_request=input("Do you want to add your account deposit, yes/no")
    #if deposit_request.lower()=='yes':
        #deposit_amount=float(input("How much you want to deposit"))
        #member.add_deposit(float(deposit_amount))
        #cursor.execute(deposit_update_sql, member.deposit)
        #total_consumption=member.deposit-sum(new_transaction.items_value)
        #if total_consumption<0:
            #print("Fail for not enough deposit")
    #else:
        #payment_choice=input("Do you want to pay with your account deposit, yes/no")
        #if payment_choice.lower()=='yes':
         
    member.add_consumption(total_consumption)# credits added at the same time
    cursor.execute(total_consumption_update_sql, total_consumption)
    cursor.execute(credits_update_sql, member.account_credits)
    transactions.new_review(new_transaction)
    transactions.new_rate(new_transaction)


cnx.close()