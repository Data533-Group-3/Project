# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:08:10 2023

@author: Administrator
"""
from datetime import datetime as dt
import sqlite3 
import random
from administer import inventory
import customer as c

# make template table of inventory
cnx = sqlite3.connect("Supermarket.db")
cursor = cnx.cursor()
cursor.execute("""CREATE TABLE inventory (item int, 
                quantity numeric,
                cost numeric,
                price numeric,
                expire text)""")
cnx.close()

# make template table of inventory
cnx = sqlite3.connect("Supermarket.db")
cursor = cnx.cursor()
cursor.execute("""CREATE TABLE sub_inventory (item int, 
                quantity numeric,
                cost numeric,
                price numeric,
                expire text)""")
cnx.close()

while True:
    judge_ini=int(input("""Which part do you want to refer?
              choose 1: manage customer account
              choose 2: go to the inventory"""))
    if judge_ini==1:
        cus_judge=int(input("""What do you want to do?
                  choose 1: Purnishment:changing credits on unactive-customer
                  choose 2: Promotion 1:providing gifts for top 3 active-customer
                  choose 3: Promotion 2: increasing deposit according to credits
                  choose 4: Advertising: Announce close-due day items"""))
        if cus_judge==4:
            print("Today's discount items as following:"+inventory.rollback())
        elif cus_judge==3:
            pass
        elif cus_judge==2:
            print()
            options =inventory.rollback2()
            probabilities = [0.5, 0.3, 0.2]
            result = random.choices(options, weights=probabilities, k=1)[0]
            print(result)
        else:
            pass
        ifquit=int(input("If you have another operation, press any button; Exiting interface presses 0"))
        if ifquit==0:
            break
    elif judge_ini==2:
         # while True:   
            judge=int(input("""What do you want to do?
                      choose 1: Add new items into main_inventory
                      choose 2: Update main_inventory
                      choose 3: Manage sub_inventory
                """))
            if judge==1:
                # items={}
                cnx = sqlite3.connect("Supermarket.db")
                cursor = cnx.cursor()
                while judge:
                    item=input("Please input your item name(str):")
                    quantity=int(input("Please input your quantity(int):"))
                    cost=float(input("Please input your cost(float):"))
                    price=float(input("Please input your price(float):"))  
                    expire=input("Please input your expire(20231123):")
                    
                    a=inventory.inventory_informa(item, quantity, cost, price, expire)
                    cursor.execute("""INSERT INTO sub_inventory VALUES(item, 
                                    quantit,
                                    cost,
                                    price,
                                    expire)""")
                    print("The total profit of this %s is %f"%(a.item,a.profit))
                    judge=input("""Want to add more items?
                              choose 1: "Yes"
                              choose 0： "Quit"
                              """)
                cnx.close()
                break
           
            elif judge==2:
                while True:
                    #initialize
                    milk_expire=dt.strptime("20231123", "%Y%m%d")
                    u=inventory.inventory_informa("test",1000,3,6,milk_expire)
                    #input
                    item=input("Please input your item name(str):")
                    quantity=int(input("Please input your quantity(int):"))
                    cost=float(input("Please input your cost(float):"))
                    u.update(item, quantity,cost)
                    #delete
                    u.remove("test")
                    ifquit=int(input("If you have another operation, press any button; Exiting interface presses 0"))
                    if ifquit==0:
                        break
            else:
                invent_judge=int(input("""What do you want to do?
                          choose 1: Add new items
                          choose 2: Update sub_inventory
                          choose 3: combine inventory from main_inventory
                    """))
                if invent_judge==1:
                        judge=1
                        while judge:
                            item=input("Please input your item name(str):")
                            quantity=int(input("Please input your quantity(int):"))
                            cost=float(input("Please input your cost(float):"))
                            price=float(input("Please input your price(float):"))  
                            expire=input("Please input your expire(20231123):")    
                            cnx = sqlite3.connect("Supermarket.db")
                            cursor = cnx.cursor()
                            b=inventory.extend_informa(item, quantity, cost, price, expire)
                            cursor.execute("""INSERT INTO sub_inventory VALUES(item, 
                                            quantit,
                                            cost,
                                            price,
                                            expire)""")
                            print(b)
                            cnx.close()    
                            judge=input("""Want to add more items?
                                      choose 1: "Yes"
                                      choose 0： "Quit"
                                      """)
                elif invent_judge==2:
                    while True:
                        #initialize
                        milk_expire=dt.strptime("20231123", "%Y%m%d")
                        u=inventory.extend_informa("test",1000,3,6,milk_expire)
                        #input
                        item=input("Please input your item name(str):")
                        quantity=int(input("Please input your quantity(int):"))
                        cost=float(input("Please input your cost(float):"))
                        u.update(item, quantity,cost)
                        cnx = sqlite3.connect("Supermarket.db")
                        cursor = cnx.cursor()
                        cursor.execute("""Update sub_inventory 
                                            set quantity=u.quantity,cost=u.cost
                                            where item=item""")     
                        cnx.close()    
                        #delete
                        u.remove("test")
                        ifquit=int(input("If you have another operation, press any button; Exiting interface presses 0"))
                        if ifquit==0:
                            break
                else:
                    while True:
                        item=input("which item do you want to add to sub_inventory from the main_inventory")
                        cursor = cnx.cursor()
                        cursor.execute("""select * from inventory 
                                            where item=item""") 
                        #only one row-main                 
                        for row in cursor:
                            milk_expire=dt.strptime("20231123", "%Y%m%d")
                            A=inventory.inventory_informa("test",1000,3,6,milk_expire)
                            A.remove(row[0])
                            #first delete and then initialize
                            A=inventory.inventory_informa(row[0],row[1],row[2],row[3],row[4])  
                            A.remove(item)
                        cnx.close() 
                        
                        cursor = cnx.cursor()
                        cursor.execute("""select * from sub_inventory 
                                            where item=item""") 
                        #sub
                        for row in cursor:
                            milk_expire=dt.strptime("20231123", "%Y%m%d")
                            U=inventory.extend_informa("test",1000,3,6,milk_expire)
                            U.remove(row[0])
                            U=inventory.extend_informa(row[0],row[1],row[2],row[3],row[4]) 
                        cnx.close() 
                        
                        #combine
                        S=U+A
                        print("The new item add in sub_inventory is",S)
                        A.remove(item)
                        cursor = cnx.cursor()
                        cursor.execute("""Update sub_inventory 
                                            set quantity=S.quantity,cost=S.cost
                                            where item=item""")     
                        cnx.close()
                        #delete
                        cursor = cnx.cursor()   
                        cursor.execute("""Delete from inventory 
                                            where item=item""")     
                        cnx.close() 
                        ifquit=int(input("If you have another operation, press any button; Exiting interface presses 0"))
                        if ifquit==0:
                            break
                    
            ifquit=int(input("If you have another operation, press any button; Exiting interface presses 0"))
            if ifquit==0:
                break
    else:
        continue     




