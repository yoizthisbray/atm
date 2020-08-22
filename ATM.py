from datetime import *
currentYear = datetime.now().year


def atm():
    User = input("Welcome to Luminescent Bank!Create your account. State your name: ")
    Balance = int(input("Enter the amount of money you own. Lie and you die :) - "))
    YOB = input("Year of birth: ")


    age = currentYear - int(YOB)

    print("You are " + str(age) + ".")

    moneyOption = input("What would you like to do? Withdraw or Deposit? ")

    if moneyOption == "Withdraw":

        withdrawal = int(input("How much would you like to withdraw? "))

        Balance = int(Balance - withdrawal)
        print("$" + str(Balance))

    if moneyOption == "Deposit":
        deposit = int(input("How much would you like to deposit? "))

        Balance = Balance + deposit
        print("$" + str(Balance))

    restart = input("Restart? ")

    if restart in "r" or "yes" or "y" or "restart" or "Yes" or "R" or "Y":
        atm()
    if restart == "no" or "No" or "NO" or "n" or "N" or "nah" or "im good" or "Nah" or "Nope" or "nope":
        print("Thanks for choosing our services")


atm()






