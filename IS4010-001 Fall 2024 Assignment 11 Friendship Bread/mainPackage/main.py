# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu


from CSVPackage.CSVProcessor import *

if __name__ == "__main__":
    print("main.py")
    myCSVProcessor = CSVProcessor("Data/fuelPurchaseData.csv")
    myCSVProcessor.process()
    print(myCSVProcessor.readData())