import csv

def res_fun(row1,row2,row3):
    
    fields = ['name','age','phone number']

    
    with open('test.csv','a') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(fields)
    with open('test.csv','a') as csvfile:
        csvwriter = csv.writer(csvfile)
        rows = [row1,row2,row3]
        csvwriter.writerow(rows)