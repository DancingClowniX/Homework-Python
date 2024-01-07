class Bank_account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def show_bank(self):
        print(f'{self.name},{self.balance}')
    def input_money(self,money):
        self.balance += money
    def delete_money(self, money):
        self.balance -= money

account = Bank_account("Леонид",0)

account.input_money(1000)
account.show_bank()
account.delete_money(500)
account.show_bank()