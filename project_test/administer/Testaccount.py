# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:03:00 2023

@author: Administrator
"""

import unittest
import customer.members
import administer.account
from administer.account import promotion
from customer.members import member
import importlib
importlib.reload(administer.account)
importlib.reload(customer.members)

class Testpromotion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def setUp(self):
        self.q1=member(id=1, name="Bob", email="Bob@gmail.com", phone="12345", address="kelowna")
        self.q2=member(id=2, name="Nancy", email="Nancy@gmail.com", phone="678910", address="richmond")
        self.q3=member(id=2, name="Maria", email="MA@gmail.com", phone="unknown", address="unknown")
        self.q4=member(id=2, name="Mike", email="ME@gmail.com", phone="456788", address="Vancouver")
    def tearDown(self):
        print("tearDown")
    def testElimiate(self):
        self.q1.add_deposit(100000)
        self.q2.add_deposit(50000)
        self.q3.add_deposit(10000)
        self.q4.add_deposit(100)
        
        
        # self.q1.add_credits(110000)
        # self.q2.add_credits(55000)
        # self.q3.add_credits(11000)
        # self.q4.add_credits(200)
        

        self.assertEqual(promotion(self.q1), "Congratulation! You gain 106050.0 in your account")
        self.assertEqual(promotion(self.q2), "Congratulation! You gain 52920.0 in your account")
        self.assertEqual(promotion(self.q3), "Congratulation! You gain 10510.5 in your account")
        self.assertEqual(promotion(self.q4), "Nothing change about the deposit")
unittest.main(module='Testaccount')