import random
#from src.util.dbhelper import DbHelper #it is an example on how we would import a database helper

class DataBaseHelper:
    def __init__(self, database_adress, username, password):
        self.connection = 'i just connected'
    def write_to_db(self):
        print('writing to db')
    def read_from_db(self):
        print('readding from db')


class Account (DataBaseHelper):
    def __init__(self, user_id,database_adress, username, password, currency = 'USD'):
        super().__init__(database_adress, username, password)
        self.currency = currency
        self.user_id = user_id
        self.balance = self.__balance()
        print(f'current balance is: {self.balance}')

    def withdraw(self, amout):
        self.amout = self.balance - float(amout)
        print(f'new balance is: {self.balance}')


    def deposit(self, amout):
        self.write_to_db()
        self.amout = self.balance + float(amout)
        print(f'new balance is: {self.balance}')



    def generate_statement(self):
        pass
    def __balance(self):
        self.read_from_db()
        print(f'getting the balance from db for: {self.user_id}')
        return  random.randint(100,1000)



    def __write_balance_to_db(self):
        print('saving to db')

class Account2 (object):
    pass

#example of composition
class Account (DataBaseHelper):
    def __init__(self, user_id,database_adress, username, password, currency = 'USD'):
        super().__init__(database_adress, username, password)
        self.currency = currency
        self.user_id = user_id
        self.balance = self.__balance()
        print(f'current balance is: {self.balance}')
        self.account2 = Account2()
        self.db_helper = DataBaseHelper(database_adress, username, password)

    def withdraw(self, amout):
        self.amout = self.balance - float(amout)
        print(f'new balance is: {self.balance}')


    def deposit(self, amout):
        self.db_helper.write_to_db()
        self.amout = self.balance + float(amout)
        print(f'new balance is: {self.balance}')



    def generate_statement(self):
        pass
    def __balance(self):
        self.db_helper.read_from_db()
        print(f'getting the balance from db for: {self.user_id}')
        return  random.randint(100,1000)



    def __write_balance_to_db(self):
        print('saving to db')


