import unittest

from atm import Atm
from atm_exceptions import *


class CheckEnterPin(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()

    def test_check_balance_without_pin(self):
        """ Check balance without pin"""
        with self.assertRaises(EnterPin) as cm:
            self.atm.check_balance()    

    def test_enter_correct_pin_check_balance(self):
        """ Enter correct pin check balance """
        self.atm.enter_pin(777)
        self.assertEqual(10000,self.atm.check_balance())

    def test_wrong_pincode_number(self):
        """ Enter wrong pin """
        with self.assertRaises(IncorrectPin) as cm:
            self.atm.enter_pin(111)

    def test_wrong_pincode_letter(self):
        """ Enter wrong pin- letter """
        with self.assertRaises(IncorrectPin) as cm:
            self.atm.enter_pin("a")
 
    def test_wrong_pincode_three_times(self):
        """ Enter wrong pin three times """
        try: 
            self.atm.enter_pin(111)
        except IncorrectPin:
            try: 
                self.atm.enter_pin(111)
            except IncorrectPin:
                try: 
                    self.atm.enter_pin(111)
                except IncorrectPin:
                    with self.assertRaises(AttemptsOver) as cm:
                        self.atm.enter_pin(111)

    # @unittest.skip(" Bug 222")
    def test_wrong_two_times_last_right(self):
        """ two times wrong ,last right 
            1.enter incorrect pin(111)
            2.enter incorrect pin(111)
            3.enter correct pin (777)"""
        try: 
            self.atm.enter_pin(111)
        except IncorrectPin:
            try: 
                self.atm.enter_pin(111)
            except IncorrectPin:
                try:
                    self.atm.enter_pin(777) 
                finally:
                    self.assertEqual(10000,self.atm.check_balance())

class TestGetMoney(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()

    def test_atm_gives_money_min1(self):
        """ money are present in atm and get_money(-1)
            1.enter correct pin
            2.get -1
            3.Recieve message "Number can't be negative!!!" """ 
        self.atm.enter_pin(777)    
        with self.assertRaises(MinusGetMoney) as cm:
            self.atm.get_money(-1)


    def test_atm_gives_money_0(self):
        """ money are present in atm and get_money(0)
            1.enter correct pin
            2.get 0
            3.check balance """ 
        self.atm.enter_pin(777) 
        self.atm.get_money(0)     
        self.assertEqual(10000, self.atm.check_balance())

    def test_atm_gives_money_1(self):
        """ money are present in atm and get_money(1)
            1.enter correct pin
            2.get 1
            3.check balance """ 
        self.atm.enter_pin(777) 
        self.atm.get_money(1)     
        self.assertEqual(9999, self.atm.check_balance())

          
    def test_atm_gives_money_5000(self):
        """ money are present in atm and get_money(5000)
            1.enter correct pin
            2.get 5000
            3.check balance """ 
        self.atm.enter_pin(777)
        self.atm.get_money(5000)      
        self.assertEqual(5000, self.atm.check_balance())

    def test_atm_gives_money_10000(self):
        """ money are present in atm and get_money(10000)
            1.enter correct pin
            2.get 10000
            3.check balance """ 
        self.atm.enter_pin(777)
        self.atm.get_money(10000)      
        self.assertEqual(0, self.atm.check_balance())
       
    def test_atm_has_not_enough_money(self):
        """ ATM balance is not enough """
        self.atm.enter_pin(777)             
        with self.assertRaises(AtmBalance) as cm:
            self.atm.get_money(100000000000)   

    @unittest.skip("Bug #001")
    def test_atm_doesnt_give_money(self):
        """ Atm doesn't give money second time without entered pin
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.withdraw 3000
            5.Recieve message "Enter pin first!!!"  """
        self.atm.enter_pin(777) 
        self.atm.get_money(1000)
        with self.assertRaises(EnterPin) as cm:
            self.atm.get_money(3000)

               
class TestCheckBalance(unittest.TestCase):
    

    def setUp(self):
        self.atm = Atm()     
        
    def check_balance():
        self.atm.enter_pin(777)
        self.atm.check_balance()

    def test_atm_gives_money_twice_and_check_balance(self):
        """ Atm gives money twice and check balance
            1.money present in atm
            2.enter correct pin
            3.withdraw 1000
            4.enter correct pin
            4.withdraw 3000
            4.check balance.Balance should be 6000 """
        self.atm.enter_pin(777)
        self.atm.get_money(1000)
        self.atm.enter_pin(777)
        self.atm.get_money(3000)        
        self.assertEqual(6000,self.atm.check_balance())    


class TestRiseMoney(unittest.TestCase):


    def setUp(self):
        self.atm = Atm()

    @unittest.skip("Bug #002")
    def test_rise_money_without_pin(self):
        """ Doesn't add money to the Atm without pin
            1.Rise money 1000000
            2.Enter correct pin """
        with self.assertRaises(EnterPin) as cm:
            self.atm.rise_money(1000000)

    @unittest.skip("Bug #003")
    def test_rise_money_and_check_balance(self):
        """ Add money to the Atm and check balance
            1.Enter correct pin       
            2.Rise money 10000
            3.Enter correct pin
            3.Check the balance.Balance should be 13000 """
        self.atm.enter_pin(777)
        self.atm.rise_money(3000)
        self.atm.enter_pin(777)
        self.assertEqual(13000,self.atm.check_balance())

    @unittest.skip("Bug #004")
    def test_rise_money_get_money_check_balance(self):
        """ Add some money to the ATM, get money and check balance
            1.Enter correct pin
            2.Rise money 3000
            3.Enter correct pin
            4.Get money 1000
            5.Check the balance.Balance should be 8000 """
        self.atm.enter_pin(777)
        self.atm.rise_money(3000)
        self.atm.enter_pin(777)
        self.atm.get_money(1000)
        self.assertEqual(8000,self.atm.check_balance())  


if __name__ == '__main__':
    unittest.main()