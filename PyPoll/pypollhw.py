import csv

votes = 0
candidates = []
cand_votes = []

filename = 'C:/Users/dshaf/Documents/School/Homework/homework/PyPoll/election_data.csv'

with open(filename) as pypoll:
	csv_reader = csv.reader(pypoll)
	next(csv_reader, None)

	for i in csv_reader:

		votes +=1

		if (i[2] in candidates):
				cand_votes[candidates.index(i[2])] += 1
		else:
				candidates.append(i[2])
				cand_votes.append(1)

winner = candidates[cand_votes.index(max(cand_votes))]
percents = [i*100/votes for i in cand_votes]

pypoll = open('PyPollResults.txt','w')
		
print("Election Results")
print("-----------------")
print("Total Votes:", votes)
print("-----------------")

for d in range(0,len(candidates)) :

	print(f'{candidates[d]}: {round(percents[d])}.000% ({cand_votes[d]}), file=pypoll)

print("-------------------------", file=f)
print(f'Winner: {winner}, file=f)
print("-------------------------", file=f)


pypoll.close()

