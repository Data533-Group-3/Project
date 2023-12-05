# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:22:04 2023

@author: Administrator
"""
from datetime import datetime as dt
from datetime import timedelta 
milk_expire=dt.strptime("20231123", "%Y%m%d")

class inventory_informa:
    #单位成本
    kinds=0
    store=[["item_name-measurement_unit","quantity","unit cost","unit price","date"],["milk-b",1000,3,6,milk_expire]]
    def __init__(self,item,quantity,cost,price,expire):
        self.item=item
        self.quantity=quantity
        self.cost=cost
        self.price=price
        self.expire=dt.strptime(expire,"%Y%m%d")
        inventory_informa.store.append([self.item,self.quantity,self.cost,self.price,self.expire])
        inventory_informa.kinds+=1
    
    def update(self,item,quantity,cost=0):
        """You update the quantity when selling and purchasing items
            by negative or positive values of quantity"""
        for i in inventory_informa.store[1:]:
            if i[0]==item:
                if quantity>0 & i[2]!=cost: #这里是进货
                    i[2]=(quantity*cost+i[1]*i[2])/(quantity+i[1])
                    i[1]+=quantity
                    return ("Suggest to adjust the price."+f"{i[0]} remains {i[1]}")
                else:
                    i[1]+=quantity
                    return f"{i[0]} remains {i[1]}"
    @property
    def profit(self):
        profits=(self.price-self.cost)*self.quantity
        return profits  
    
    def delete(self,item):
        for i in inventory_informa.store[1:]:
            if i[0]==item:
                inventory_informa.store.remove(i)


            

#你想弄一个加法，每次initialize的时候是不是会重复计算
class extend_informa(inventory_informa):
    Kinds=0
    Store=[["item_name-measurement_unit","quantity","unit cost","unit price","date"]]
    #滞销商品
    def __init__(self, item, quantity, cost, price, expire):
        self.item=item
        self.quantity=quantity
        self.cost=cost
        self.price=price
        self.expire=dt.strptime(expire,"%Y%m%d")
        extend_informa.Store.append([self.item,self.quantity,self.cost,self.price])
        extend_informa.Kinds+=1 
    def __add__(self,other):
        if self.item==other.item:
            quantity=self.quantity+other.quantity
            cost=(self.cost+other.cost)/quantity
            for i in extend_informa.Store[1:]:
                if i[0]==other.item:
                   i[1]=quantity
                   i[2]=cost
            return (other.item,quantity,cost)
        else:
            print("""There are none matching items. Are you sure you writing the standard name?\n
                  Call 1 if other are different items;
                  Call 2 if you want to rewrite""")
            choice=int(input("Which one do you choose:"))
            if choice==1:
                inventory_informa.store.append([other.item,other.quantity,other.cost,other.price,other.expire])
            elif choice==0:            
                return "Rewrite the standard style like {self.item}"         
 
    def __str__(self):
        return f"{self.item} have {self.quantity} in store. The profit they can make is {self.profit}"
 
def rollback2():
    top3=[]
    max=10000
    for i in extend_informa.Store[1:]:
        
        if i[1]>max:
            max=i[1]
            top3.append([i[0],i[1]],i[2])
    top3.sort(key=lambda x: x[1],reverse=True)
    top3[0:3].sort(key=lambda x: x[2],reverse=False)
    return top3[0:3]        
        
def rollback():#放外面
    today=dt.today()
    sale_50=[]
    sale_80=[]
    sale={}
    for i in range(1,len(inventory_informa.store)):
        due=(today-inventory_informa.store[i][-1]).days
        if due<3:
            discount=0.5
            sale_50.append([inventory_informa.store[i][0],inventory_informa.store[i][3]*discount,due])
            sale_50=sorted(sale_50,key=lambda x:x[2])
        elif due<7:
            discount=0.8
            sale_80.append([inventory_informa.store[i][0],inventory_informa.store[i][3]*discount,due])
            sale_80=sorted(sale_80,key=lambda x:x[2])
    sale["50%"]=sale_50
    sale["80%"]=sale_80
    return sale  



flower=inventory_informa("flower", 520, 3, 10, (dt.today()+timedelta(days=3)).strftime("%Y%m%d"))
fish=inventory_informa("fish", 100, 12, 20, (dt.today()+timedelta(days=2)).strftime("%Y%m%d"))
pork=inventory_informa("pork", 60, 25, 35, (dt.today()+timedelta(days=1)).strftime("%Y%m%d"))
beef=inventory_informa("beef", 150, 30, 43,( dt.today()+timedelta(days=6)).strftime("%Y%m%d"))
snack=inventory_informa("snack", 1000, 5, 13, (dt.today()+timedelta(days=20)).strftime("%Y%m%d"))