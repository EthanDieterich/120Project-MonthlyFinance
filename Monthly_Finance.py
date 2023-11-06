#This code uses multiple functions to read a csv file into a matrix then
#manipulate that matrix 
#column labels - Index - Cost - Name - Category - description 
import csv
import os


def createfile_Name():
    print('\nEnter Finance Record name\n------------------')
    #accepted value range
    months = {"Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec",'test'}
    years = {'18','19','20','21','22','23','24','test'}
    
    file_Name = 'null'
    while (file_Name == 'null'):
        startMonth = input('Start Month(Abrv):')
        startYear = input('Start Year(2 digit):')
        if startMonth in months and startYear in years:
            file_Name = startMonth+startYear+'Record.csv'
        else: 
            print('Try again')
           
    return file_Name
    

def openRecord(tempData):
    header = ['Index', 'Date', 'Cost', 'Name', 'Category', 'Description']
    
    print("You Selected Open Record.")
      #User Input
    file_Name = createfile_Name()
    if os.path.exists(file_Name):
        print("\nOpening",file_Name+'...')
        with open(file_Name, mode = 'r') as file:
            csv_reader = csv.reader(file)
    # Iterate through each row in the CSV and append it to the matrix
            for (row) in csv_reader:
                tempData.append(row)
        return 
        
    else:
        print("File Does not exist." )
        choice = input("\nwould you like to create a new file? Enter Yes(1) No(0): ")
        if choice == '1':
            with open(file_Name, mode = 'w', newline = '') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(header)
                tempData.append(header)
            return 
        elif choice == '0': 
            return 
        
        

def closeRecord(tempData):
    print("You Selected Close Record.")
    file_Name = createfile_Name()
    with open(file_Name, mode = 'w', newline = '') as file:
        csv_writer = csv.writer(file)
        for row in tempData:
            csv_writer.writerow(row)
        tempData.clear()
    return
    

def addToRecord(tempData):
    i = 0
    while i < len(tempData) and tempData[i]:
        i += 1
    while True:
        print("\nCreating row", i)
        row = []
        Index = i
        row.append(Index)
        Cost = input("Enter Cost: ")
        row.append(Cost)
        Name = input("Enter Name: ")
        row.append(Name)
        Category = input("Enter Category: ")
        row.append(Category)
        Description = input("Enter Description: ") 
        row.append(Description)
        
        tempData.append(row)
        i+=1
        choice = input("Would you like to add more? Enter Yes(1) No(0):")
        if choice == '1':
            continue
        elif choice == '0':
            break
    return

def deleteFromRecord(tempData):
    print("You selected option 4.")
    return
    
def sumRecord(tempData):
    print('You selected option 5.')
    return

def sortRecord(tempData):
    print('You selected option 6.')
    return

            
    
if __name__ == '__main__':
    #Menu
    menu = {
        '1': openRecord,
        '2': closeRecord,
        '3': addToRecord,
        '4': deleteFromRecord,
        '5': sumRecord,
        '6': sortRecord
        }
    tempData = []
    file_Name = ""
    while True:
        if len(tempData) == 0:
            print("Data set not selected")
        elif len(tempData) == 1: 
            print("Data set is empty")
        elif len(tempData) > 1:
            for row in tempData:
                print()
                for element in row: 
                    print(element, end=', ')
                    
        print("\n---------------")
        print("Menu:")
        print("1. Open Record")
        print("2. Close and Save Record")
        print("3. Add to Record")
        print("4. Delete from Record")
        print("5. Sum Record")
        print("6. Sort Record")
        print("7. Exit")
        print("---------------")
    
        choice = input("Enter Your Choice: ")
    
        if choice in menu:
            menu[choice](tempData)
        elif choice == '7':
            print('bye')
            break
        else:
            print("invalid choice")
    
