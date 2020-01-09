import os
import csv

budget_data_file = os.path.join(".",".","02-Homework","03-Python","Instructions","PyBank","Resources","budget_data.csv")


#creating the empty lists

month = []
profit_losses = []


#read CSV and parse data into lists
with open(budget_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        month.append(row[0])
        profit_losses.append(int(row[1]))

#First question - number of months
months_total = len(month)

greatst_inc = profit_losses[0]
greatst_dec = profit_losses[0]
total_over_period = 0

#Second question - Total amount of "Profit/Losses' over the entire period +
#forth and fifth questions - Greatest increase and greatest decrease profit/losses

for amount in range(len(profit_losses)):
    if profit_losses[amount] >= greatst_inc:
        greatst_inc = profit_losses[amount]
        greatst_inc_month = month[amount]
    elif profit_losses[amount] <= greatst_dec:
        greatst_dec = profit_losses[amount]
        greatst_dec_month = month[amount]
    total_over_period += profit_losses[amount]

#Third question - Average of changes in Profit/losses over the entire period
average_total = round(total_over_period/months_total, 2)


# Path not working .... homework_output = os.path.join('PyBank', 'final_file_PyBank.txt')
homework_output= '/Users/macchina/Desktop/BootCamp/Boot/02-Homework/PyBank_Output.txt'

with open (homework_output, 'w') as final_file:
    final_file.writelines('\n Financial Analysis\n')
    final_file.writelines('_______________________________\n')
    final_file.writelines('Total Months: ' + str(months_total) + '\n')
    final_file.writelines('Total: $' + str(total_over_period) + '\n')
    final_file.writelines('Average Change: $' + str(average_total) + '\n')
    final_file.writelines('Greatest Increase in Profit: ' + greatst_inc_month + ' ($ ' + str(greatst_inc) +')'+ '\n')
    final_file.writelines('Greatest Decrease in Profit: ' + greatst_dec_month + '($ ' + str(greatst_dec) +')')

#print to terminal

with open(homework_output, 'r') as final_file_terminal:
    print(final_file_terminal.read())