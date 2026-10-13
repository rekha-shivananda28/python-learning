expenses=[250,120,500,80,300]
total=sum(expenses)
lowest=max(expenses)
highest=min(expenses)
average=total/len(expenses)

print("---Expense analyzer---")
print("Expenses:",expenses)
print("Total Expense:",total)
print("Highest expense:",highest)
print("Lowest Expense:",lowest)
print("Average Expense:",average)