# Import modules 
    # os module allows to create file paths across operating systems
    # csv module allows the reading of csv files    
import os 
import csv

# Store csvpath associated with the csv raw data 
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')


# Read the file using the csv module and store the contents in variable called csvfile
with open(csvpath) as csvfile:
    # Specify delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row and store in variable 
    csv_header = next(csvreader)
    ##print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    
    # Define start of first row 
    pre_net = int(first_row[1])

    # Create empty lists to store outputs 
    total_months = []
    total_profits = []
    net_change_list = []

    # Read each row of data after the header
    for row in csvreader:
    # Store read values in previously created lists (profits as integer to convert to decimal and to later perform mathmatical operations)
        total_months.append(row[0])
        total_profits.append(int(row[1]))

        # Increase row every time the for loop runs 
        net_change = int(row[1])-pre_net
        pre_net = int(row[1])
        net_change_list +=[net_change]
    # Calculate lengths of total_months list and print result
    print(f"Total Months: {len(total_months)}")
    # Calculate grand total of profits and print result 
    print(f"Total Profits: ${sum(total_profits)}")
    
    # Calculate average change and print result, adjust decimal place
    average_change=sum(net_change_list)/len(net_change_list)
    print(f"Average Change: ${average_change:.2f}")

    # Calculate change in profits for every month through iteration
    for i in range(len(total_profits)-1):
        monthly_change = (total_profits[i+1]-total_profits[i])
    # Append results to the empty net change list. 
        net_change_list.append(monthly_change)

    # Calculate the greatest increase and greatest decrease in profits
        greatest_increase = max(net_change_list)   
        greatest_decrease = min(net_change_list)
    
    # Index the months list to get the month and year associated with the increase & decrease results, assign variable, print results
    greatest_increase_month = net_change_list.index(max(net_change_list))
    greatest_decrease_month = net_change_list.index(min(net_change_list))

    # Print results of greatest increase and greatest decrease with associated dates
    print (f"Greatest Increase In Profits: {total_months[greatest_increase_month]} ${(str(greatest_increase))}")
    print (f"Greatest Decrease In Profits: {total_months[greatest_decrease_month]} ${(str(greatest_decrease))}")
    
# Define path for the outputfile, store in variable
analysis_file = os.path.join('.', 'Analysis', 'Analysis.txt')

# Open output file 
with open(analysis_file, "w", newline= ") as datafile:
    writer = txt.writer(datafile)
    
