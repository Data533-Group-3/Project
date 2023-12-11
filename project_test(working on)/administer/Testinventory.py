# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:05:17 2023

@author: Administrator
"""

import unittest
import administer.inventory
from administer.inventory import inventory_informa
from datetime import datetime as dt
from datetime import timedelta 
import importlib

importlib.reload(administer.inventory)

class TestInventory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    def setUp(self):
        self.p1=inventory_informa("flowers", 520, 3, 10, (dt.today()+timedelta(days=3)).strftime("%Y%m%d"))
        self.p2=inventory_informa("snacks", 1000, 5, 13, (dt.today()+timedelta(days=20)).strftime("%Y%m%d"))
    def testprofit(self):
        self.assertEqual(self.p1.profit, 3640)
        self.assertEqual(self.p2.profit, 8000)
    def testupdate(self):
        self.assertEqual(self.p1.update("flowers", 520,6), "Suggest to adjust the price."+"flowers remains 1040")
        self.assertEqual(self.p1.update("flowers", -520,6), "flowers remains 520")
        self.assertEqual(self.p2.update("snacks", 1000, 5), "snacks remains 2000")
        self.assertEqual(self.p2.update("snacks", -1000,5), "snacks remains 1000")
    def tearDown(self):
        print("tear down")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")
# unittest.main(module="Testinventory")