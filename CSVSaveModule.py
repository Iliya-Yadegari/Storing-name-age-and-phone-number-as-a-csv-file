import csv

def res_fun():
    
    fields = ['name','age','phone number']

    
    with open('test.csv','a') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        csvwriter.writerow(fields)
