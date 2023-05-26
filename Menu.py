from Database import DB
from time import sleep

class Menu():
    def __init__(self) -> None:
        self.database = DB()

    def mainMenu(self):
        def showMenu():
            uopt = input("Please, select an option!\n1)Show all Crypto in DataBase\n2)Update all Crypto info\n3)Show best Crypto\n4)Search for a specific Crypto\n5)Show most expensive Cryptos\n6)Add new Crypto to DataBase\n0)Exit\n")
            return int(uopt)

        print("********Welcome to CryptoDB!********")
        while True:
            sleep(2)
            opt = showMenu()
            if opt == 1:
                self.database.showDatabase()
            elif opt == 2:
                self.database.updateCrypto()
                print("Crypto info has been updated (any Crypto not in original list has been removed)\n")
            elif opt == 3:
                self.bestCrypto()
            elif opt == 4:
                self.searchCrypto()
            elif opt == 5:
                self.mostExpensive()
            elif opt == 6:
                self.addNew()
            elif opt == 0:
                print("Exiting...\n")
                break
            else:
                print("Non valid option, please try again\n")
                

    def bestCrypto(self):
        N = int(input("Please enter how Many Cryptos you want to see\n"))
        self.database.bestCrypto(N)

    def searchCrypto(self):
        name = input("Please enter Name/Symbol of desired Crypto\n")
        self.database.searchCrypto(name)

    def mostExpensive(self):
        N = int(input("Please enter how Many Cryptos you want to see\n"))
        self.database.mostExpensive(N)
    
    def addNew(self):
        url = input("Please enter new Crypto's URL\n")
        self.database.addCrypto(url)