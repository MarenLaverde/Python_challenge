# Import modules 
    # os module allows to create file paths across operating systems
    # csv module allows the reading of csv files    
import os 
import csv

# Store csvpath associated with the csv raw data 
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Read the file using the csv module and store the contents in variable called csvfile
with open(csvpath) as csvfile:
    # Specify delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first and store in variable 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)