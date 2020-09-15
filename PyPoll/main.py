import csv

with open ('Resources/election_data.csv') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    linecount=0
    next(csvfile)
    candidates={}
    for row in csvreader:
        
        linecount+=1
        candidate=row[2]
        if candidate in candidates:
            candidates[candidate]+=1
        else:
            candidates[candidate]=1

    winner=''
    winnervotes=0
    count=linecount-1
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {count}')
    print(f'-------------------------')

    for candidate in candidates:
        total=candidates[candidate]
        pct=total/count*100
        if total>winnervotes:
            winner=candidate
            winnervotes=total
        print(f'{candidate}: {pct:.3f}% ({total})')

   
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')
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
        fw.close()
