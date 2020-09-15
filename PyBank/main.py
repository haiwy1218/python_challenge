import csv

#open data file for reading
with open ('Resources/budget_data.csv') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    #store header row
    headers=next(csvfile)
    #declare variables
    linecount=0
    total=0
    deltas=[]
    prioramount=0
    monthmaxincrease=''
    amountmaxincrease=0
    monthmaxdecrease=''
    amountmaxdecrease=0
    #iterate each row in data file
    for row in csvreader:
        # read month and amount accumulating total
        month=row[0]
        amount=int(row[1])
        total+=amount
        #check for new max deltas for increases and decreases in profitability
        if linecount>0:
            delta=amount-prioramount
            if (delta>0) and (delta>amountmaxincrease):
                amountmaxincrease=delta
                monthmaxincrease=month
            if(delta<0) and (delta<amountmaxdecrease):
                amountmaxdecrease=delta
                monthmaxdecrease=month
            # add delta to list
            deltas.append(delta)
        # store prior amount
        prioramount=amount
        linecount+=1
    count=linecount 
    #calculate average of deltas
    average=sum(deltas)/len(deltas) 
    #print result of analysis    
    print('Financial Analysis')
    
    print ('----------------------------')
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
   
    print(f'Average  Change: ${average:.2f}')
    print(f'Greatest Increase in Profits:{monthmaxincrease} (${amountmaxincrease})')
    print(f'Greatest Decrease in Profits: {monthmaxdecrease} (${amountmaxdecrease})')
    #store analysis in file
    with open ('analysis/results.txt','w') as fw:
        print('Financial Analysis',file=fw)
        print ('----------------------------',file=fw)
        print(f'Total Months: {count}',file=fw)
        print(f'Total: ${total}', file=fw)
    
        print(f'Average  Change: ${average:.2f}',file=fw)
        print(f'Greatest Increase in Profits:{monthmaxincrease} (${amountmaxincrease})',file=fw)
        print(f'Greatest Decrease in Profits: {monthmaxdecrease} (${amountmaxdecrease})',file=fw)
        fw.close()




