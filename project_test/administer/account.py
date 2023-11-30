# -*- coding: utf-8 -*-
<<<<<<< HEAD
#change have made ffff
=======
#hopefully some change here 
>>>>>>> administor
"""
Created on Mon Nov 20 21:28:46 2023

@author: Administrator
"""
from Administer import inventory
import customer as c
from datatime import datatime as dt

class customer():
#    user_information.customer
#    user_record.goods
#    def __init__(self,name,birth,address):
#       user_details.__init__
#    def __str__(self):
#        return ""
    points=c.members.member().get_member_info(1,2,3,4,5,6,7,8)["credits"]
    def eliminate(self):
        purchase_day=c.transactions.Transaction(1,1,1,1,1).get_order_info()[2]
        if (dt.today()-purchase_day).day>=31:
            points=0
        #当你一个月没有购物，10%,直到为0。
    def promotion(self):
        if points>100000:
            price=[]
            for i in inventory_informa.store[1:]:
                price.append(i[3]*0.8)
        elif points>50000:
            price=[]
            for i in inventory_informa.store[1:]:
                price.append(i[3]*0.85)
        elif points>50000:
            price=[]
            for i in inventory_informa.store[1:]:
                price.append(i[3]*0.95)
#        i=input("do you want to change something:")
        