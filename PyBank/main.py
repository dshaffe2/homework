import csv
import os




csv_file = 'budget_data.csv'
profit = []
row_count = 0
difference = []
months = []

with open(csv_file) as hw:
        csv_reader = csv.reader(hw)
        next(csv_reader, None)



        #row_count = sum(1 for row in csv_reader) Why does this cause my next loop not to be able to be able to be stepped into?

        #get the number of months in the data
        #get total amount of Profits/Losses
        #get average change

        for i in csv_reader:
               
                profit.append(int(i[1]))
                row_count += 1
                months.append(i[0])
              
        # for i in range(1,len(profit)):#Why doesn't this work?? It only returns the last difference on the list
        #         difference = profit[i] - profit[i-1]
        difference = [profit[i] - profit[i-1] for i in range(1,len(profit))]

print("Total Months:", row_count)
print("Total Profit: $", sum(profit))
print("Average Change:", round(sum(difference) / (row_count-1),2))
print("Greatest monthly increase: $", {months[difference.index(max(difference))+1]}, max(difference))
print("Greatest monthly decrease: $", {months[difference.index(min(difference))+1]}, min(difference))

hw = open('PyBankResults.txt', 'w')
hw.close()
	# for row in csv_reader:
	# 	row_count += 1
	# 	row_count = len(row_count)
	# 	print(row_count)


	# 	if line_count == 0:
	# 		print(f'Column names are {", ".join(row)}')
	# 		line_count +=1
	# 	else:
	# 		print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
	# 		line_count += 1
	# print(f'Processed {line_count} lines.')
