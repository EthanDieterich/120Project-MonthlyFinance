#This code uses multiple class methods to read a csv file into a matrix then
#manipulate that matrix 
#column labels - Index - Cost - Name - Category  
#ADD NAMES HERE
#Ethan Dieterich, Logan Young , Natnael Tadesse, Jahmaal Hall, and Chris Cosgrove
import csv
import os

class CSV_File_Manager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tempData = []
        
    def create_file_name(self):
        print('\nEnter Finance Record Name\n------------------')
        #accepted value range
        months = {"Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec",'test'}
        years = {'18','19','20','21','22','23','24','test'}
    
        file_name = 'null'
        while (file_name == 'null'):
            startMonth = input('Start Month(Abrv):')
            startYear = input('Start Year(2 digit):')
            if startMonth in months and startYear in years:
                file_name = startMonth+startYear+'Record.csv'
            else: 
                print('Try again')
        self.file_name = file_name

    def open_record(self):
        header = ['Index', 'Cost', 'Name', 'Category']
    
        print("You Selected Open Record.")
        #User Input
        self.create_file_name()
        if os.path.exists(self.file_name):
            print("\nOpening",self.file_name+'...')
            with open(self.file_name, mode = 'r') as file:
                csv_reader = csv.reader(file)
        # Iterate through each row in the CSV and append it to the matrix
                for (row) in csv_reader:
                    self.tempData.append(row)
        
        else:
            print("File does not exist." )
            choice = input("\nwould you like to create a new file? Enter Yes(1) No(0): ")
            if choice == '1':
                with open(self.file_name, mode = 'w', newline = '') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(header)
                    self.tempData.append(header) 
        
    def close_record(self):
        print("You Selected Close Record.")
        print("Would you like to save file as", self.file_name+str("(0)"), "or choose a new name(1)?")
        choice = input("Enter choice: ")
        if int(choice) == 1:
            self.create_file_name()
        with open(self.file_name, mode = 'w', newline = '') as file:
            csv_writer = csv.writer(file)
            for row in self.tempData:
                csv_writer.writerow(row)
            print("File saved as", self.file_name)
            self.tempData.clear()   
            self.file_name = ''
            
    def add_to_record(self):
        print("You Selected Add to Record")
        i = len(self.tempData)
        categories = {
            'R' : "Rent/Mortgage",
            'F' : "Food",
            'T' : "Transportation",
            'U' : "Utilities",
            'S' : "Subscriptions",
            'P' : "Personal",
            'I' : "Investment/Savings",
            'D' : "Debt/Loan Payment",
            'H' : "Health",
            'M' : "Misc"
            }
        while True:
            print("\nCreating row", i)
            row = [i]
        
            cost = input("Enter Cost: ")
            row.append(cost)
            name = input("Enter Name: ")
            row.append(name)
            print("[Rent/Mortgage, Food, Transportation, Utilities, Subscriptions]")
            print("[Personal, Savings/Investment, Debt/Loan Payment, Health, Misc]")
            c = input("Enter the first letter of the selected Category: ")
            row.append(categories[c])
        
            self.tempData.append(row)
            i += 1
            choice = input("Would you like to add more? Enter Yes(1) No(0):")
            if choice == '0':
                break
    def delete_from_record(self):
        print("You Selected Delete From Record.")
        if len(self.tempData) <= 1:
            print("Data set is empty. Nothing to delete.")
            return

        index_to_delete = input("Enter the index of the row to delete: ")

        if index_to_delete.isdigit():
            index_to_delete = int(index_to_delete)
           
            if 0 <= index_to_delete < len(self.tempData):
                deleted_row = self.tempData.pop(index_to_delete)
                print("Row deleted:")
                print(deleted_row)
            else:
                print("Invalid index. No row deleted.")
        else:
            print("Invalid input. Please enter a valid index (a non-negative integer).")
    def sum_record(self):
        print('You Selected Sum Record')
        column_to_sum = 1
        
        if len(self.tempData) <= 1:
            print("Data set is empty.")
            return
        if not self.tempData:
            print("No data selected pr the data set is empty")
        
        total_sum = 0
        for row in self.tempData:
            try:
                cost = float(row[column_to_sum])
                total_sum += cost
            except ValueError:
                print("Invalid value found while calculating the sum.")
        
        print(f"Total sum of costs: {total_sum}")

    def sort_record(self):
        print('You Selected Sort Record.')
        if len(self.tempData) <= 1:
            print("Data set is empty or contains only one row. Nothing to sort.")
            return
    
        # Prompt the user for the sorting order
        print("Select the sorting order:")
        print("0. Sort by Index")
        print("1. Sort by Category")
        print("2. Sort by Cost")
    
        try:
            order_choice = input("Enter the number corresponding to the sorting order: ")
            if int(order_choice) == 0:
                self.tempData[1:] = sorted(self.tempData[1:], key=lambda row: int(row[0]))
            if int(order_choice) == 1:
                # Sort by Category
                self.tempData[1:] = sorted(self.tempData[1:], key=lambda row: row[3])  # 3 corresponds to the "Category" column
            elif int(order_choice) == 2:
                #sort by Cost
                self.tempData[1:] = sorted(self.tempData[1:], key=lambda row: float(row[1]))  # 1 is "Cost" column
            else:
                print("Invalid sorting order choice. No sorting performed.")
                return
            print("Record sorted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def display_data(self):
        if len(self.tempData) == 0:
           print("Data set not selected")
        elif len(self.tempData) == 1: 
            print(self.file_name)
            print("Data set is empty")
        elif len(self.tempData) > 1:
            print(self.file_name)
            for row in self.tempData: 
                print()
                for element in row: 
                    print(element, end=', ')
        print("\n---------------")
       
if __name__ == '__main__':
    #Menu
    csv_file = CSV_File_Manager("")
    menu = {
        '1': csv_file.open_record,
        '2': csv_file.close_record,
        '3': csv_file.add_to_record,
        '4': csv_file.delete_from_record,
        '5': csv_file.sum_record,
        '6': csv_file.sort_record
        }
    while True:
        print("---------------")
        csv_file.display_data()
        
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
        print()
        if choice in menu:
            menu[choice]()
        elif choice == '7':
            print('bye')
            break
        else:
            print("invalid choice")
    
