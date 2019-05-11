import pandas as pd

months = ('all', 'january', 'february', 'march', 'april', 'may' , 'june')

while True:
    month = input("Which month do you want data from [all , or any from January to June]: ")

    if month in months:
        break
    else:
        print("invalid input, enter valid month")
        
        
    
    