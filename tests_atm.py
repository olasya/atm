import unittest

from atm import Atm


class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = Atm()
        self.atm.enter_pin(777)

    def test_atm_gives_money(self):
        money = self.atm.get_money(1000)
        self.assertEqual(1000, money)


if __name__ == '__main__':
    unittest.main()