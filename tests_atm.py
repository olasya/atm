import unittest

from atm import Atm
from atm_exceptions import *

class TestAtm(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_atm_gives_money(self):
        money = self.atm.get_money(1000)
        self.assertEqual(1000, money)


class TestAtmExceptions(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_exception(self):
        try:
            self.atm.get_money(1000000)
        except Exception as e:
            self.assertEqual('Atm balance is no enough!!!', e.message)


if __name__ == '__main__':
    unittest.main()