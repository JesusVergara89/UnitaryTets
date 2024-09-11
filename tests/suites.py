import unittest
from test_banck_account import BankAccount_test

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccount_test("test_deposit"))
    suite.addTest(BankAccount_test("test_withdraw"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())


