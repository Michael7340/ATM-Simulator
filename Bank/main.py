#class Bank:


class Customer:
    def __init__(self,amount,account_number,account_name):
        self.amount = amount
        self.account_number = account_number
        self.account_name = account_name
        self.pin = 1234
        
    def debit(self,debit_amount):
        print('debit initialized')
        previous_amount = self.amount
        if debit_amount > self.amount:
            print("You're too poor")
            return

        else:
            self.amount -= debit_amount
            print("Your account has been debitted with {0} \nPrevious amount: {1} \nCurrent amount: {2}".format(debit_amount,previous_amount,self.amount))

    def credit(self, credit_amount):
        print('credit initialized')
        previous_amount = self.amount
        self.amount += credit_amount
        print('Your account has been credited with {0} \nPrevious amount: {1} \nCurrent amount: {2}'.format(credit_amount,previous_amount,self.amount))

customer1 = Customer(3500,'01248956948','Tola')
customer2 = Customer(5000,'12858294950','Femi')
customer1.debit(4500)
customer1.credit(2000)
customer1.debit(4500)
print(customer1.pin)

