class BankAccount:
    def __init__(self, ano, name, balance):
        self.account_number = ano
        self.holder_name = name
        self.balance = balance
    def __str__(self):
        return f"Bank account {self.account_number} for {self.holder_name} with a balance of {self.balance}"
    def __repr__(self):
        return f"BankAccount(ano='{self.account_number}', name='{self.holder_name}', balance={self.balance})"

# Define the __str__ and __repr__ in the following format:
# (1) for __str__: Bank account 12345678 for John Doe with a balance of 1500.00
# (2) for __repr__: BankAccount(ano='12345678', name='John Doe', balance=1500.00)
      
