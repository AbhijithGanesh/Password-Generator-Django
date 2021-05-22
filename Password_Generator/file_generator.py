import sqlite3
import csv
try:
    C = sqlite3.connect(r'C:\Users\HP\VSCODE\ANNUAL-CSC-PROJECT\Django_Annual\db.sqlite3')
    cursor = C.cursor()
    print("Successfully Connected to SQLite")

    Query = 'SELECT * FROM Password_Generator_Registration'
    cursor.execute(Query)
    record = cursor.fetchall()
    cursor.close()
    _records = []
    for i in record:
        _records.append(list(i))

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if C is True:
        C.close()
        print("The SQLite connection is closed")
def file_handling():
    global _records
    _rows = [] 
    for i in range(len(_records)):
        a = [_records[i][1],_records[i][2],_records[i][3],_records[i][4],_records[i][5]] 
        _rows.append(a)
    filename = 'Registrations.CSV'
    with open(filename, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['Name', 'Email', 'Contact Number', 'Organization', 'Country'])
        csvwriter.writerows(_rows)
if __name__ == "__main__":
    file_handling()