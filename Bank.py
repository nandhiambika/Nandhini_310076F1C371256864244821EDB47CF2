# BankAccount class
class Bankaccount:
  def--init--(self):
  # Function to deposit amount
def deposit(self):
  amount=float(input("Enter amount to be deposited:"))
  self.balance+=amount
  print("/n Amount Deposited:", amount)
  #Function to withdraw the amount
def withdraw(self):
  amount= float(input("Enter amount to be withdrawn:"))
  if self.balance >= amount
  self.balance -= amount
print("/n you withdraw:", amount )
else:
print("/n Insufficient balance ")
# Function to display the amount
def display(self):
  print("/n New Available Balance=",self.balance)
  # python program to create Bankaccount class
# with both a deposit () and a withdraw() function
class Bank_Account:
  def--init--(self):
  self. balance=0
  print("Hello!!! welcome to the deposit & withdrawal machine")
  def deposit(self):
    amount=float(input("Enter amount to be Deposited:"))
    self.balance += amount
    print("/n Amount Deposited:",amount)
    def withdraw(self):
      amount=float(input("Enter amount to be withdraw:"))
      if self.balance >= amount:
        self.balance -=amount:
        print("/n you withdraw:",amount)
      else:
        print("/n New Available Balance=",self balance)
        #Driver code
# creating an object of class
s = Bank_Account()
#calling functions with that class object
s.deposit()
s.withdraw()
s.display()

  
