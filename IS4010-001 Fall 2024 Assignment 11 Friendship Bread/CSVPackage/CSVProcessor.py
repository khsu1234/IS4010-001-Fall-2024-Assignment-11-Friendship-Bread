# CSVProcessor.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv

class CSVProcessor:
    
    def __init__(self, filename):
        self.__filename = filename
        
    def process(self):
        print("Processing", self.__filename)
        data = self.readData()

    def readData(self):
        return None
        
