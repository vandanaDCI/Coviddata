import csv
import copy
import random

#  Create a dictionary for each day with date as key and other data as values

cov_d = {
    "date": "00/00/0000" ,
    "new_cases":0 ,
    "deaths":0 ,
    "recoveries":0
}
"""
for key , value in cov_d.items():  #Safwan dint use this step
    print("{}:{}".format(key,value)) #Safwan dint use this step
"""
myDatalist = [] #Creating a list of days : to be filled from the file

with open ('Day 4\covid_data.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') #Here, we could have skipped use of delimiter if we used 'r'(read function) after the file name in line above(19)
    print(csvReader)
    lineCount = 0
    for row in csvReader:
        if lineCount == 0: #here, we can use next(reader) function to skip header without defining linecount now
            print(f'Column names are: {",".join(row)}')
            lineCount += 1
        else:
            print(f'date:{row[0]},new_cases: {row[1]},deaths:{row[2]},recovered:{row[3]}')
            currentCases = copy.deepcopy(cov_d)
            currentCases["date"] = row[0]    #while defining, because it is stored in tabular form, we use row and column interchangeably
            currentCases["new_cases"] = row[1] #Here, if we define data type as int, then will not have to define it as float while calculating no of cases in line no 42
            currentCases["deaths"] = row[2] 
            currentCases["recovered"] = row[3] 
            myDatalist.append(currentCases)
            lineCount += 1
    print(f'Processed {lineCount} lines.')
    final_line_count = int(lineCount - 1)

# Calculating the total number of cases 
count_cases = 0
for i in myDatalist:
    count_cases += float(i["new_cases"]) #float because i is an item in mydatalist which is a dictionary. i.e. supposed to be in string and new cases gives integer value. so to bring both tgthr we need float
print("The total number of cases are: " ,count_cases)
final_count_cases = count_cases

# Calculating the total number of deaths 
count_deaths = 0         # count_deaths = sum(i["deaths"] for i in myDatalist) in 1 line the solution
for i in myDatalist:
    count_deaths += float(i["deaths"])
print("The total number of deaths are: " , count_deaths)

# Calculating the total number of recoveries
count_recoveries = 0
for i in myDatalist:
    count_recoveries += float(i["recovered"])  
print("The total number of recoveries are: " , count_recoveries)

# Calculating average number of cases per day
average_cases = final_count_cases/final_line_count #average = count_cases / len(myDatalist)
print("The average number of cases per day are :" , average_cases)

print("A random day data is :" , random.choice(myDatalist)) # random is a module we are trying to run and choice is a method

"""
USED FROM CHATGPT SOME ERROR
from datetime import datetime

def calculate_total_days (csvfile):
    total_days = 0

    with open ('Day 4\covid_data.csv') as csvfile:
        reader = csv.reader('Day 4\covid_data.csv')
        next(reader)

    for row in reader:
        date_str = row[0]
        date_obj = datetime.strptime(date_str , '%Y-m-%d')
        total_days += 1

    return total_days 

csv_file = 'dates.csv'
total_days = calculate_total_days('Day 4\covid_data.csv')
print(f"The total number of days is: {total_days}")
"""


"""
for i in myDatalist:
    for key,value in i.items():
        print("{}:{}".format(key,value))
        print("")
"""
"""
    here, in below block, the defining of variable was fine but I missed using a loop. 
    #total_cases = 0
    #total_cases = total_cases + new_cases
    #print("Total cases : " , total_cases)
"""
        


        




