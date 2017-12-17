import unittest

from atm import Atm
from atm_exceptions import *

class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()

    def test_atm_gives_money(self):
        """ money are present in atm"""
        # money = self.atm.get_money(1000)
        self.atm.enter_pin(777)        
        self.assertEqual(1000, self.atm.get_money(1000))

    def test_atm_gives_money_and_check_balance(self):
        """ Atm gives money and check balance
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.check balance.Balance should be 9000"""
        self.atm.enter_pin(777)
        self.atm.get_money(1000)        
        self.assertEqual(9000,self.atm.check_balance())

    def test_atm_gives_money_twice_and_check_balance(self):
        """ Atm gives money twice and check balance
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.enter correct pin
            4.withdraw 3000
            4.check balance.Balance should be 6000"""
        self.atm.enter_pin(777)
        self.atm.get_money(1000)
        self.atm.enter_pin(777)
        self.atm.get_money(3000)        
        self.assertEqual(6000,self.atm.check_balance())    
        
    @unittest.skip("Bug #001")    
    def test_atm_doesnt_give_money(self):
        """ Atm doesn't give money second time without entered pin
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.withdraw 3000
            5.Don't recieve message incorrect pin """
        self.atm.enter_pin(777)
        self.atm.get_money(1000)
        with self.assertRaises(EnterPin) as cm:
            self.atm.get_money(3000)

    def test_atm_has_not_enough_money(self):
        """ ATM balance is not enough """
        # money = self.atm.get_money(100000000000)
        # self.assertRaises(AtmBalance("Atm balance is no enough!!!"), money)
        self.atm.enter_pin(777)
        with self.assertRaises(AtmBalance) as cm:
            self.atm.get_money(100000000000)

        # the_exception = cm.exception
        # self.assertEqual(the_exception.message, "Atm balance is no enough!!!")

    # def balance_after_get_money(self):
    #     """ balance after get money"""    
    #     balance = self.atm.chekc_balance()
    #     self.assertEqual(1000000, balance)
    def test_wrong_pincode(self):
        with self.assertRaises(IncorrectPin) as cm:
            self.atm.enter_pin(111)

    
    def test_wrong_pincode_three_times(self):
        try: 
            self.atm.enter_pin(111)
        except IncorrectPin:
            try: 
                self.atm.enter_pin(111)
            except IncorrectPin:
                with self.assertRaises(AttemptsOver) as cm:
                    self.atm.enter_pin(111)

class TestCheckBalance(unittest.TestCase):
    """docstring for TestCheckBalance"""
    def setUp(self):
        self.atm = Atm()
        
    def test_check_balance(self):
        self.atm.enter_pin(777)
        self.assertEqual(10000, self.atm.check_balance())

    def test_check_balance_without_pin(self):
        with self.assertRaises(EnterPin) as cm:
            self.atm.check_balance()

        
            

# class TestAtmExceptions(unittest.TestCase):

#     def setUp(self):
#         self.atm = Atm()
#         self.atm.enter_pin(777)

#     def test_exception(self):
#         try:
#             self.atm.get_money(100000000000000)
#         except Exception as e:
#             self.assertEqual('Atm balance is no enough!!!', e.message)

    



if __name__ == '__main__':
    unittest.main()