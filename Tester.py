import transactionManager

a = transactionManager.Account("Alex")
a.checkBalance()

b = transactionManager.Account("Bob")

a.credit(1000)
a.checkBalance()

b.credit(2500)
b.checkBalance()

a.debit(300)
a.checkBalance()


