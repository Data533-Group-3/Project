# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:48:50 2023

@author: Administrator
"""

import unittest
import sys
sys.path.append('administer')
from administer.Testaccount import Testpromotion
from administer.Testinventory import TestInventory
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestInventory('testupdate'))
    suite.addTest(TestInventory('testprofit'))
    suite.addTest(Testpromotion('testPromotion'))                                            
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()