import csv

with open ('Resources/budget_data.csv') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    linecount=0
    total=0
    deltas=[]
    prioramount=0
    monthmaxincrease=''
    amountmaxincrease=0
    monthmaxdecrease=''
    amountmaxdecrease=0
    for row in csvreader:
        if linecount ==0:
            linecount+=1
        else:
            month=row[0]
            amount=int(row[1])
            total+=amount
            
            
            delta=amount-prioramount
            if (delta>0) and (delta>amountmaxincrease):
                amountmaxincrease=delta
                monthmaxincrease=month
            if(delta<0) and (delta<amountmaxdecrease):
                amountmaxdecrease=delta
                monthmaxdecrease=month
            if linecount>1:
               
                deltas.append(delta)
            prioramount=amount
            linecount+=1
    count=linecount-1  
    average=sum(deltas)/len(deltas)     
    print('Financial Analysis')
    
    print ('----------------------------')
    print(f'Total Months: {count}')
    print(f'Total: ${total}')
   
    print(f'Average  Change: ${average:.2f}')
    print(f'Greatest Increase in Profits:{monthmaxincrease} (${amountmaxincrease})')
    print(f'Greatest Decrease in Profits: {monthmaxdecrease} (${amountmaxdecrease})')
    
    with open ('analysis/results.txt','w') as fw:
        print('Financial Analysis',file=fw)
        print ('----------------------------',file=fw)
        print(f'Total Months: {count}',file=fw)
        print(f'Total: ${total}', file=fw)
    
        print(f'Average  Change: ${average:.2f}',file=fw)
        print(f'Greatest Increase in Profits:{monthmaxincrease} (${amountmaxincrease})',file=fw)
        print(f'Greatest Decrease in Profits: {monthmaxdecrease} (${amountmaxdecrease})',file=fw)
        fw.close()




