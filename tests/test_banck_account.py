import unittest
from src.bank_account import BankAccount,WithdrawalTimeRestrictionError,WithdrawalDayRestrictionError
from unittest.mock import patch
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
    
    @patch("src.bank_account.datetime")
    def test_Withdrawal_TimeRestriction(self, mock_datetime):
        mock_datetime.now.return_value.hour = 9
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_Withdrawal_TimeRestriction_raises(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    
    @patch("src.bank_account.datetime")
    def test_Withdrawal_DayRestriction(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 0
        mock_datetime.now.return_value.hour = 9
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_Withdrawal_DayRestriction_raises(self, mock_datetime):
        mock_datetime.now.return_value.weekday.return_value = 6
        with self.assertRaises(WithdrawalDayRestrictionError):
            self.account.withdraw(100)

    def test_deposit_various_amounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                account = BankAccount(1000, log_file="transaction_log.txt")
                new_balance = account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])

        



