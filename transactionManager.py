class Account:

    def __init__(self, name, balance = 0, credit = 0, debit = 0, transactionNum = 0):
        self._name = name
        self._balance = balance
        self._credit = credit
        self._debit = debit
        self._transactions = transactionNum

    def credit(self, amount):
        self._balance += amount
        self._transactions += 1
        print("*** Hello %s, $%.2f has been CREDITED to your account" %(self._name, amount))
        print("Transation number: %d\n" %self._transactions)
        return

    def debit(self, amount):
        self._balance -= amount
        self._transactions += 1
        print("*** Hello, %s, $%.2f has been DEBITED to your account" % (self._name, amount))
        print("** $%.2f has been debited to your account" % amount)
        print("Transation number: %d\n" % self._transactions)
        return

    def checkBalance(self):
        print("## Dear %s, Your account balance is $%.2f ##\n" %(self._name,self._balance))
        return