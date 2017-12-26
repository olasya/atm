"""
ATM Exceptions
"""

class AttemptsOver(Exception):
    pass


class AtmBalance(Exception):
    pass


class EnterPin(Exception):
    pass


class IncorrectPin(Exception):
    pass


class MinusGetMoney(Exception):
    pass


class MinusRiseMoney(Exception):
    pass