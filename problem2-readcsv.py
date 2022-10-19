#Provide the program to read the csv file.

import pandas as pd
from datetime import date
from dateutil import parser
import math


        

def readcsv(filepath,delimeter,quote):

    

    if __checkextension(filepath):
    
    #Read csv file and return dataframe object
    
        df = pd.read_csv(filepath,sep = delimeter,quotechar = quote)
    
    #convert columns into list
    
        birthdate = df['Birthdate'].tolist()
        name = df['Name'].tolist()
        salary = df['Salary'].tolist()
        age = []
    
    #find age and append into age list

        for bd in birthdate:
        
            a = __findAge(bd)
            age.append(a) 
        
        print("{:<8} {:<15} {:<10} {:<5}".format('Name','Birthdate','Salary','Age'))

    #print data into table format

        for i in range(0,(len(birthdate))):
            print("{:<8} {:<15} {:<10} {:<5}".format(name[i],birthdate[i],salary[i],age[i]))

    else:
        print("Filetype (.csv) does not match!!!")
   
#find the age from the birthdate
def __findAge(bd):
    #convert string object into datetime object to perform date calculation

    bdate = parser.parse(bd).date()
    #return today's date

    today = date.today()
    total_days = (today - bdate).days
    return(math.ceil(total_days/365))


#To check the file extension
def __checkextension(filepath):

    templist = filepath.split(sep = '.')
    if templist[-1] == 'csv':
        return True
    else:
        return False

def main():
    filepath = input("Enter your filepath: ")
    delimeter = input("Enter Delimeter: ")
    quote = input("Enter Quote char: ")
    
    readcsv(filepath,delimeter,quote)

if __name__ =='__main__':
    main()
