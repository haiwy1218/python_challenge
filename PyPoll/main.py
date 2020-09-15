import csv
# open data file for reading
with open ('Resources/election_data.csv') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    #store header row
    headers=next(csvfile)
    # declare variables
    linecount=0
    # use dictionary for candidates and totals
    candidates={}
    #iterate each row in data file
    for row in csvreader:
        
        linecount+=1
        candidate=row[2]
        #calculate vote count per candidate
        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate]=1
    # declare variables for winner
    winner=''
    winnervotes=0
    count=linecount-1
    #print result of analysis
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {count}')
    print(f'-------------------------')
    # print results for each candidate
    for candidate in candidates:
        total=candidates[candidate]
        pct=total/count*100
        #determine winner
        if total>winnervotes:
            winner=candidate
            winnervotes=total
        print(f'{candidate}: {pct:.3f}% ({total})')

   
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')
    #store analysis in file
    with open ('analysis/results.txt','w') as fw:


        print(f'Election Results',file=fw)
        print(f'-------------------------',file=fw)
        print(f'Total Votes: {count}',file=fw)
        print(f'-------------------------',file=fw)

        for candidate in candidates:
            total=candidates[candidate]
            pct=total/count*100
            if total>winnervotes:
                winner=candidate
                winnervotes=total
            print(f'{candidate}: {pct:.3f}% ({total})',file=fw)

    
        print(f'-------------------------',file=fw)
        print(f'Winner: {winner}',file=fw)
        print(f'-------------------------',file=fw)
        #close file
        fw.close()
