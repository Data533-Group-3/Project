# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:48:50 2023

@author: Administrator
"""

import unittest
import sys
sys.path.append('administer')
sys.path.append('customer')
import customer
from administer.Testaccount import Testpromotion
from administer.Testinventory import TestInventory
from customer.test_members import Testmembers
from customer.test_transactions import Testtransactions
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestInventory('testupdate'))
    suite.addTest(TestInventory('testprofit'))
    suite.addTest(Testpromotion('testElimiate')) 
    suite.addTest(Testmembers('test_check_premium_status')) 
    suite.addTest(Testmembers('test_add_deposit'))
    suite.addTest(Testmembers('test_add_credits'))
    suite.addTest(Testmembers('test_add_consumption'))
    suite.addTest(Testmembers('test_get_member_info'))
    suite.addTest(Testmembers('test_change_email'))
    suite.addTest(Testmembers('test_change_phone'))
    suite.addTest(Testmembers('test_change_address'))
    suite.addTest(Testmembers('test_create_new_member'))
    suite.addTest(Testtransactions('test_write_review'))
    suite.addTest(Testtransactions('test_rate_order'))
    suite.addTest(Testtransactions('test_get_order_info'))
    suite.addTest(Testtransactions('test_get_order_total'))
    suite.addTest(Testtransactions('test_new_review'))
    suite.addTest(Testtransactions('test_new_rate'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()