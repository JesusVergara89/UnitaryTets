import unittest
from src.bank_account import BankAccount
import os

class BankAccount_test(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as r:
            return len(r.readlines())
        
    def test_deposit(self):
        balance = self.account.deposit(500)
        self.assertEqual(balance, 1500, "el balance no es igual")

    def test_withdraw(self):
        balance = self.account.withdraw(500)
        self.assertEqual(balance, 500)

    def test_get_balance(self):
        balance = self.account.get_balance()
        self.assertEqual(balance, 1000)
    
    def test_transfer(self):
        result = self.account.transfer(500, '12345678901')
        self.assertEqual(result, f'Se transfirió la cantidad 500 al número de cuenta 12345678901. El balance de la cuenta es 500')
    
    def test_transfer_transfer(self):
        self.account.transfer(200, "222222223333444444")
        self.assertTrue(os.path.exists("transaction_log.txt"))
    
    def test_transaction_log(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))
    
    def test_count_transctions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.transfer(200, "222222223333444444")
        assert self._count_lines(self.account.log_file) == 2


