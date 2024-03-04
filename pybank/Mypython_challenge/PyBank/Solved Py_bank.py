import os
import csv
budget_data_csv = os.path.join("PyBank","Resources", "budget_data.csv")
budget_data_txt = os.path.join("PyBank", "output", "budget_data.txt")
# list of datas/ tracking datas
total_months= 0
Total_profit = 0
initial_profit = 0
Net_Total = 0
monthly_changes = []
Greatest_increase = ["",0]
Greatest_decrease = ["",0]
date = []
Average_Change = []
Net_change_list = []
total_change_profit = 0
with open(budget_data_csv) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    header = next(csvreader)
    firstrow = next(csvreader)
    initial_profit = int(firstrow[1])
   
    for row in csvreader:
       #To calculate Totals
        total_months +=1
        Net_Total+= int(row[1])
        
     # To calculate the Average Change  
       # firstly we get the revenues 
        Net_change = int(row[1]) - initial_profit
        initial_profit = int(row[1])
        Net_change_list += [Net_change]
        monthly_changes = monthly_changes + [row[0]]
#Average_Change = (total_change_profit/total_months)
# to greatest_increase_profit
        if (Net_change > Greatest_increase[1]):
            Greatest_increase[0] = row[0]
            Greatest_increase[1] = Net_change
# to calculate greatest decrease
        if (Net_change < Greatest_decrease[1]):
            Greatest_decrease[0] = row[0]
            Greatest_decrease[1] = Net_change
#Average 
Average_Change = round(sum(Net_change_list)/ len(Net_change_list),2)
        
#greatest_decrease_profits = min(monthly_exp)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
Result = ( 
f"Financial Analysis\n"  
f"----------------------\n"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    #Average_Change+= 
f"Total Months: {total_months}\n"
f"Total: ${Net_Total}\n"
f"Average Change:  ${Average_Change}\n"
f"Greatest Increase : {Greatest_increase[0]} (${Greatest_increase[1]})\n"
f"Greatest Decrease: {Greatest_decrease[0]} (${Greatest_decrease[1]})\n")
print(Result)

#Export the result to terminal
#budget_data_csv = os.path.join("Output", "budget_data.txt")
with open(budget_data_txt, "w") as outfile:
    outfile.write(Result)