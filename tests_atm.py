import unittest

from atm import Atm
from atm_exceptions import *

class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_atm_gives_money(self):
        """ money are present in atm """      
        self.assertEqual(1000, self.atm.get_money(1000))

    def test_atm_gives_money_and_check_balance(self):
        """ Atm gives money and check balance
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.check balance.Balance should be 9000 """
        self.atm.get_money(1000)        
        self.assertEqual(9000,self.atm.check_balance())

    def test_atm_gives_money_twice_and_check_balance(self):
        """ Atm gives money twice and check balance
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.enter correct pin
            4.withdraw 3000
            4.check balance.Balance should be 6000 """
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
            5.Recieve message "Enter pin first!!!"  """
        self.atm.get_money(1000)
        with self.assertRaises(EnterPin) as cm:
            self.atm.get_money(3000)

    def test_atm_has_not_enough_money(self):
        """ ATM balance is not enough """      
        with self.assertRaises(AtmBalance) as cm:
            self.atm.get_money(100000000000)


class WrongPin(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()

    def test_wrong_pincode(self):
        """ Enter wrong pin """
        with self.assertRaises(IncorrectPin) as cm:
            self.atm.enter_pin(111)
 
    def test_wrong_pincode_three_times(self):
        """ Enter wrong pin three times """
        try: 
            self.atm.enter_pin(111)
        except IncorrectPin:
            try: 
                self.atm.enter_pin(111)
            except IncorrectPin:
                with self.assertRaises(AttemptsOver) as cm:
                    self.atm.enter_pin(111)

class TestCheckBalance(unittest.TestCase):
    
    def setUp(self):
        self.atm = Atm()

    def test_check_balance_without_pin(self):
        """ Check balance without pin"""
        with self.assertRaises(EnterPin) as cm:
            self.atm.check_balance()

class TestRiseMoney(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()

    def test_rise_money(self):
        """ Add some money to the ATM
            1.Enter correct pin
            2.Rise money 1000000"""
        self.atm.enter_pin(777)
        self.assertEqual(1010000, self.atm.rise_money(1000000))  

    @unittest.skip("Bug #002")
    def test_rise_money_without_pin(self):
        """ Doesn't add money to the Atm without pin
            1.Rise money 1000000"""
        with self.assertRaises(EnterPin) as cm:
            self.atm.rise_money(1000000)

    @unittest.skip("Bug #003  ATM doesn't rise")
    def test_rise_money_and_check_balance(self):
        """ Add money to the Atm and check balance 10000
            1.enter correct pin       
            2.Rise money 10000
            3.Check the balance.Balance should be 13000"""
        self.atm.enter_pin(777)
        self.atm.rise_money(3000)
        self.assertEqual(13000,self.atm.check_balance())

    def test_rise_money_get_money_check_balance(self):
        """ Add some money to the ATM, get money and check balance
            1.Enter correct pin
            2.Rise money 1000000
            3.Get 500000
            4.Balance 90000"""
        self.atm.enter_pin(777)
        self.atm.rise_money(3000)
        self.atm.enter_pin(777)
        self.atm.get_money(1000)
        self.assertEqual(3000,self.atm.check_balance())  






if __name__ == '__main__':
    unittest.main()