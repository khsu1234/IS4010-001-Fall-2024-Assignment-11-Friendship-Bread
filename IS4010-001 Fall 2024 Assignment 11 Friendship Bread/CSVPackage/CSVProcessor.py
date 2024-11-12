# CSVProcessor.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu


class CSVProcessor:
    
    def __init__(self, filename):
        self.__filename = filename
        
    def process(self):
        print("Processing", self.__filename)
        
