class BankAccount:
    def __init__(self, input_holder_name, balance, type):
        self.holder_name = input_holder_name
        self.balance = balance
        self.type = type
        self._rates = {
            "personal": 10,
            "business": 50 
        }
    
    def pay_in(self, amount):
        self.balance += amount

    def pay_montly_fee(self):
        self.balance -= 50
    
    def pay_monthly_fee(self):
# problem with this is that it can be accessed by the outside world :/ 
#        if self.type == "personal":
#            self.balance -= 10
#        elif self.type == "business":
#            self.balance -= 50 
         
# better to assign the method inside the class. with (_) before the variable.    
         self.balance -= self._rates[self.type]
        

