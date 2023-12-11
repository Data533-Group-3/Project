# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:28:46 2023

@author: Administrator
"""
from administer import inventory
from administer.inventory import rollback2
# import customer as c
from datetime import datetime as dt
import sqlite3 
import random


def eliminate():
    # if tran_class.transaction_time
    # points=c.members.member().get_member_info(1,2,3,4,5,6,7,8)["credits"]
    # def eliminate(self):
    #     purchase_day=c.transactions.Transaction(1,1,1,1,1).get_order_info()[2]
    #     if (dt.today()-purchase_day).day>=31:
    #         points=0
    expired_member=[]
    cnx=sqlite3.connect("Supermarket.db")
    cursor=cnx.cursor()
    cursor.execute("select customer_id,transaction_time from transactions")
    for row in cursor:
        if (dt.today()-row[1]).day>=31:
            points=0
            expired_member.append(row[0])
            # return f"It's so sorry that there are {row[0]} credits expiring from your account"
        else:
            points=row[1]
            # return f"There are {row[0]} credits in your account. Enjoy your shopping in Superman!"
    cursor.commit()
    cursor.close()
    ##update
    cnx=sqlite3.connect("Supermarket.db")
    cursor=cnx.cursor()
    cursor.execute("update members set credits=0 when id in ?", (expired_member))
    cursor.commit()
    cursor.close()
    return expired_member
def promotion(member_class):#账户充钱
    if member_class.account_credits>100000:
        member_class.deposit=round(member_class.deposit*1.01,1)
        # deposit_account[member_class.id]=member_class.deposit
        return f"Congratulation! You gain {member_class.deposit} in your account"
    elif member_class.account_credits>50000:
        member_class.deposit=round(member_class.deposit*1.008,1)
        # deposit_account[member_class.id]=member_class.deposit
        return f"Congratulation! You gain {member_class.deposit} in your account"
    elif member_class.account_credits>10000:
        member_class.deposit=round(member_class.deposit*1.001,1)
        # deposit_account[member_class.id]=member_class.deposit
        return f"Congratulation! You gain {member_class.deposit} in your account"
    else:
        return "Nothing change about the deposit"

    # deposit_account={}
    # cnx=sqlite3.connect("Supermarket.db")
    # cursor=cnx.cursor()
    # cursor.execute("select id,deposit,credits from members")
    # cursor.commit()                                                    
    # for row in cursor:
    #     if row[2]>100000:
    #         deposit_account[row[0]]=row[1]*1.01
    #         # return f"Congratulation! You gain {row[1]*1.01} in your account"
    #     elif row[2]>50000:
    #         deposit_account[row[0]]=row[1]*1.008
    #         # return f"Congratulation! You gain {row[1]*1.008} in your account"
    #     elif row[2]>10000:
    #         deposit_account[row[0]]=row[1]*1.001
    #         # return f"Congratulation! You gain {row[1]*1.001} in your account"
    # cursor.close()
    
    # ##update
    # cnx=sqlite3.connect("Supermarket.db")
    # cursor=cnx.cursor()
    # for i in deposit_account:
    #     cursor.execute("""update members set deposit=? where id=?"""(i.values(),i.key()))
    # cursor.commit()                                                    
    # cursor.close()
    # return deposit_account
    # # if points>100000:
    # #     price=[]
    # #     for i in inventory_informa.store[1:]:
    # #         price.append(i[3]*0.8)
    # # elif points>50000:
    # #     price=[]
    # #     for i in inventory_informa.store[1:]:
    # #         price.append(i[3]*0.85)
    # # elif points>50000:
    # #     price=[]
    # #     for i in inventory_informa.store[1:]:
    # #         price.append(i[3]*0.95)
    

def promotion1():#分配
    list1=[]
    gift={}
    cnx=sqlite3.connect("Supermarket.db")
    cursor=cnx.cursor()
    cursor.execute("""select customer_id from members order by credits limit 3""")
    cursor.commit()      
    for row in cursor:
        list1.append(row)
    cursor.close()
    items=rollback2(inventory.inventory_informa.store)
    
    probability_1 = 0.5
    probability_2 = 0.3
    probability_3 = 0.2
    
    
    for i in list1:
        rand_num = random.random()
    
        # 根据概率分布确定随机数的范围
        if rand_num < probability_1:
           present=items[0]
           gift[i]=present   
        elif rand_num < probability_1 + probability_2:
            present=items[1]
            gift[i]=present   
        else:
           present=items[2]
           gift[i]=present   
           
    return gift




        
    

    