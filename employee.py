"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, commissionType, initialPay, finalPay, commissionValue, contracts, hours):
        self.name = name
        self.contractType = contractType
        self.commissionType = commissionType
        self.initialPay = initialPay
        self.finalPay = finalPay
        self.commissionValue = commissionValue
        self.contracts = contracts
        self.hours = hours
        

    def get_pay(self):
        if (self.contractType == "salary"):
            if (self.commissionType == 0):
                return self.initialPay
            
            elif (self.commissionType == "bonus"):
                self.finalPay = self.initialPay + self.commissionValue
                return self.finalPay
            
            elif (self.commissionType == "contract"):
                self.finalPay = self.initialPay + (self.contracts * self.commissionValue)
                return self.finalPay
            
        elif (self.contractType == "hourly"):
            if (self.commissionType == 0):
                return (self.initialPay * self.hours)
            
            elif (self.commissionType == "bonus"):
                self.finalPay = (self.hours * self.initialPay) + self.commissionValue
                return self.finalPay
            
            elif (self.commissionType == "contract"):
                self.finalPay = ((self.hours * self.initialPay) + (self.contracts * self.commissionValue))
                return self.finalPay
    
    
    def __str__(self):
        if self.contractType == "hourly":
            if self.commissionType == "bonus":
                return f"{self.name} works on a contract of {self.hours} hours at {self.initialPay}/hour and receives a bonus commission of {self.commissionValue}. Their total pay is {self.get_pay()}."
            elif self.commissionType == "contract":
                return f"{self.name} works on a contract of {self.hours} hours at {self.initialPay}/hour and receives a commission for {self.contracts} contract(s) at {self.commissionValue}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.initialPay}/hour. Their total pay is {self.get_pay()}."
        elif self.contractType == "salary":
            if self.commissionType == "bonus":
                return f"{self.name} works on a monthly salary of {self.initialPay} and receives a bonus commission of {self.commissionValue}. Their total pay is {self.get_pay()}."
            elif self.commissionType == "contract":
                return f"{self.name} works on a monthly salary of {self.initialPay} and receives a commission for {self.contracts} contract(s) at {self.commissionValue}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.initialPay}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", commissionType=0, initialPay=4000, finalPay=0, commissionValue=0, contracts=0, hours=0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", commissionType=0, initialPay=25, finalPay=0, commissionValue=0, contracts=0, hours=100)
#print(charlie.get_pay())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", "contract", initialPay=3000, finalPay=0, commissionValue=200, contracts=4, hours=0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410. !!!
jan = Employee('Jan', "hourly", "contract", initialPay=25, finalPay=0, commissionValue=220, contracts=3, hours=150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", "bonus", initialPay=2000, finalPay=0, commissionValue=1500, contracts=0, hours=0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", "bonus", initialPay=30, finalPay=0, commissionValue=600, contracts=0, hours=120)