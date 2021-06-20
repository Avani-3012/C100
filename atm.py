class atm():

    def __init__(self,cardNumber,pin):
        
        self.cardNumber = cardNumber
        self.pin= pin
    

cashWithdrawal = atm("1200-819-900",3012)
balanceEnquiry = atm("3450-200-100",1203)
print(cashWithdrawal.pin)
print(balanceEnquiry.cardNumber)



