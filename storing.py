import csv
import datetime

def markIt(name, presence,date_time = datetime.date.today()):


    with open('./records/attendance.csv', 'a', newline='') as csvfile:
        file = open('./records/attendance.csv', 'r')
        fieldnames = ['Name', 'Date', 'Presence']

        reader = csv.reader(file)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        condition = False

        for row in reader:
            for i in range(0, len(row)):
                if row[i] == str(date_time):    
                    condition = True
                if row[i] == name:
                    condition=True
                

        if condition==True:
            print("Attendance already marked")
            return "Attendance already marked"

        else:
            
            writer.writerow({'Name': name, 'Date': date_time, 'Presence': presence})
            return "Attendance done"

if __name__=="__main__":
    markIt("prat", True)