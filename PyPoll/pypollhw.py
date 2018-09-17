import csv
filename = "C:/Users/dshaf/Documents/School/election_data.csv"
totalvotes = 0
candidates = []
candidate1count = 0
candidate2count = 0
candidate3count = 0
candidate4count = 0
cand1_per = 0
cand2_per = 0
cand3_per = 0
cand4_per = 0
counts = []

with open(filename, 'r') as file:
    data = csv.reader(file)
    header = next(data)    

    for row in data:
        totalvotes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            candidate1count += 1
        elif row[2] == candidates[1]:
            candidate2count += 1
        elif row[2] == candidates[2]:
            candidate3count += 1
        elif row[2] == candidates[3]:
            candidate4count += 1
    
    counts = [candidate1count, candidate2count, candidate3count, candidate4count]
    winner = candidates[counts.index(max(counts))]

cand1_per = round(float(candidate1count / totalvotes * 100), 3)     
cand2_per = round(float(candidate2count / totalvotes * 100), 3)
cand3_per = round(float(candidate3count / totalvotes * 100), 3)
cand4_per = round(float(candidate4count / totalvotes * 100), 3)
            
   
    
print("Election Results")
print("------------------------------")
print(f"Total Votes: {totalvotes}")
print("------------------------------")
print(f"{candidates[0]}: {cand1_per}% ({candidate1count})")
print(f"{candidates[1]}: {cand2_per}% ({candidate2count})")
print(f"{candidates[2]}: {cand3_per}% ({candidate3count})")
print(f"{candidates[3]}: {cand4_per}% ({candidate4count})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")



filename = "C:/Users/dshaf/Documents/School/PythonHW_Take2/PyPoll/PyPoll_results.txt"
with open(filename, 'w') as results:
    csvwriter = csv.writer(results, delimiter = ' ')
    
    csvwriter.writerow("Election Results")
    csvwriter.writerow("------------------------------")
    csvwriter.writerow(f"Total Votes: {totalvotes}")
    csvwriter.writerow("------------------------------")
    csvwriter.writerow(f"{candidates[0]}: {cand1_per}% ({candidate1count})")
    csvwriter.writerow(f"{candidates[1]}: {cand2_per}% ({candidate2count})")
    csvwriter.writerow(f"{candidates[2]}: {cand3_per}% ({candidate3count})")
    csvwriter.writerow(f"{candidates[3]}: {cand4_per}% ({candidate4count})")
    csvwriter.writerow("------------------------------")
    csvwriter.writerow(f"Winner: {winner}")
    csvwriter.writerow("------------------------------")
