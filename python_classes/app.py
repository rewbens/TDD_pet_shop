from modules.bank_account import * 

account = BankAccount("John", 500, "business")

#account.holder_name = "Ada"  Updates from holder_name "John"

#print(account.holder_name)

account.pay_montly_fee()
print(account.balance)

account_1 = BankAccount("Ada", 600, "personal")
account_1.pay_monthly_fee()
print(account_1.balance)
