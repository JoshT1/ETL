from requestPage import requestPage
from requestDetails import requestDetails
import g
import sqlite3

def main(requestKey):
    # connect to DB
    sqliteConnection = sqlite3.connect('refusa.db')

    # create cursor
    cursor = sqliteConnection.cursor()

    # Drop tables if already exists
    cursor.execute("DROP TABLE IF EXISTS bus")

    # Create table
    table = '''
    CREATE TABLE bus
    (RecordId TEXT PRIMARY KEY,
    CompanyName TEXT,
    Address TEXT,
    City TEXT,
    State TEXT,
    Zip TEXT,
    CreditScore TEXT,
    ExecName TEXT,
    ExecTitle TEXT,
    Phone TEXT,
    Fax TEXT,
    IUSA TEXT,
    EmpMin TEXT,
    EmpMax TEXT,
    SIC TEXT,
    NAICS TEXT,
    InsertTime DATETIME DEFAULT CURRENT_TIMESTAMP
    ); '''

    # Initialize table
    cursor.execute(table)

    # Get the page count from the request
    pages = requestPage(requestKey, 0)
    g.sleep(g.st)

    # For each page, find request parameters for the business details
    for i in range(pages):
        busObj = g.Bus()
        i += 1
        # Find recordId parameters and store it in a list
        requestList = requestPage(requestKey, i)
        g.sleep(g.st)
        busList = requestDetails(requestList, requestKey, busObj)
        query = '''INSERT INTO bus 
                   (RecordId, CompanyName, Address, City, State, Zip, CreditScore, ExecName, ExecTitle, 
                    Phone, Fax, IUSA, EmpMin, EmpMax, SIC, NAICS)
                   VALUES 
                   (:RecordId, :CompanyName, :Address, :City, :State, :Zip, :CreditScore, :ExecName, :ExecTitle, 
                    :Phone, :Fax, :IUSA, :EmpMin, :EmpMax, :SIC, :NAICS)'''

        for j in range(len(busList)):
            cursor.execute(query, {'RecordId': busList[j].recordId,
                                   'CompanyName': busList[j].companyName,
                                   'Address': busList[j].address,
                                   'City': busList[j].city,
                                   'State': busList[j].state,
                                   'Zip': busList[j].zip,
                                   'CreditScore': busList[j].cs,
                                   'ExecName': busList[j].execName,
                                   'ExecTitle': busList[j].execTit,
                                   'Phone': busList[j].phone,
                                   'Fax': busList[j].fax,
                                   'IUSA': busList[j].iusa,
                                   'EmpMin': busList[j].empMin,
                                   'EmpMax': busList[j].empMax,
                                   'SIC': busList[j].sic,
                                   'NAICS': busList[j].naics})
            cursor.commit()
        print("gottem")


if __name__ == '__main__':
    requestKey = 'dabfa2679990450084246c25c56df1bf'
    main(requestKey)
