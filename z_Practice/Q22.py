# Multimode
# we will build 

from statistics import multimode

def main():
    # combining

    number = get_total_years()
    print(f"The total number of Years is {number}")

    years_data, manager_data = get_data(number)
     

    print("\n      SHOWING DATA      \n")
    for year, data in years_data.items():
        print(f"{year} -> {data}")

    print("\n      SHOWING DATA UNDER WHICH MANAGER DATA GOT LEAKED SAME      \n")
    leak_database = calc_leak(years_data)
    
    for manager, (year, data) in zip(manager_data, years_data.items()):
        print(f"    {manager}")
        if year in leak_database:
            print(f"      {year} : {data}")

def get_total_years():
    while True:
        try:
            years = int(input("Enter the total number of years you wanna compare (only 50 years): "))

            if 1 <= years <= 50:
                return years

            print("Invalid Quantity")
        except ValueError:
            print("Please Enter Correct Number of Years")

def get_managers():
    while True:
        name = input("Enter the Manager name: ").strip().capitalize()

        if name.replace(" ", "").isalpha():
            return name
           

        print("Please enter correct manager name!!!")


def get_data(number):
    database = {}
    manager_list = []
    print("\n             ENTER THE REQUIRED DATA            \n")
    for i in range(number):
        #                      YEARS INPUT
        while True:
            taking_years = input("Enter the Year: ").strip()

            if taking_years.isdigit() and len(taking_years) == 4:
                years = int(taking_years)

                if 1970 <= years <= 2030:

                    if years in database:
                        print("This year has already been entered. Please enter another year.")
                        continue
                    break

                print("Please Enter correct range")

            else:
                print("Please Enter correct Year")
        

       #                      DATA INPUT
        while True:
            try:
                data = int(input("Enter the data: "))

                if 1 <= data <= 1000:
                    database[years] = data
                    break
                print("Out of Range!!!")

            except ValueError:
                print("Data is wrong")

        #                      MANAGER INPUT        
        manager = get_managers()
        manager_list.append(manager)
        print("\n")

    return database, manager_list


def calc_leak(years_data):
    datas = list(years_data.values())
    leaks = multimode(datas)

    leak = {}

    for year, data in years_data.items():           # here year means keys and data means its values in dictionary
        if data in leaks:           # if values are in leaks list
            leak[year] = data       # add that that data in leak dictionary

    return leak
    

main()







"""
What we wanna build

manager = [ m1, m2, m3, m4 ]
databse = {
            "Year 1" : 23,
            "Year 2" : 33,
            "Year 3" : 23,
            "Year 4" : 23
        }
"""


# things i need to solve in this code 
#   -> chnage variable naming
#   -> alignment
