from datetime import datetime

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f'{message}\n')

    def _log_not_funds(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f'{message}\n')

    def deposit(self, amount):
        """
        Deposita una cantidad en la cuenta y devuelve el saldo nuevo.

        :param amount: Cantidad de dinero a depositar (debe ser positiva).

        Ejemplos:
        >>> account = BankAccount(100)
        >>> account.deposit(50)
        120
        >>> account.deposit(-10)
        150
        >>> account.deposit(0)
        150
        """
        if amount > 0:
            self.balance += amount
            self._log_transaction(f'Deposited {amount}. New balance: {self.balance}')
        return self.balance
    
    def withdraw(self, amount):
        now = datetime.now()
        today = now.weekday()
        days_not_allows = [5,6]
        if today in days_not_allows:
            raise WithdrawalDayRestrictionError("Saturday and Sunday withdraw is not allow it")
        else:
            if now.hour < 8 or now.hour > 17:
                raise WithdrawalTimeRestrictionError("Time not allo it")
            else:
                if amount > 0:
                    self.balance -= amount
                    self._log_transaction(f'Withdraw {amount}. New balance: {self.balance}')
        return self.balance
    
    def get_balance(self):
        self._log_transaction(f'Current balance: {self.balance}')
        return self.balance
    
    def transfer(self, amount, account_number):
        if amount > self.balance:
            self._log_not_funds("Sin fondos suficiente para la transferencia")
            raise InsufficientFunds("No tienes fondos para realizar esta transferencia")
        elif len(account_number) < 10:
            raise AccountNumberNotValid("El número de cuenta debe de ser mayor o igual a 10 dígitos")
        else:
            self.balance -= amount
            self._log_transaction(f'Transferido {amount}. Nuevo saldo: {self.balance}')
            return f'Se transfirió la cantidad {amount} al número de cuenta {account_number}. El balance de la cuenta es {self.balance}'
        
class InsufficientFunds(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class AccountNumberNotValid(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class WithdrawalTimeRestrictionError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class WithdrawalDayRestrictionError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


withdrawal = BankAccount()

withdrawal.withdraw(100)
