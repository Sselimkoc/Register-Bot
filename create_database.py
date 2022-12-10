from database import *
from openpyxl import Workbook

def create_db():                   #use this function to create adatabase with our data 
    wb= Workbook()                         #create a excel file
    ws = wb.active
    ws.title="Database"                        
    headers =["Tag"]+ list(data["p1"].keys())       #we add the attributes name on the excel file
    ws.append(headers)
    for person in data:
        all_data = list(data[person].values())      #we add the data on the our excel file
        ws.append([person]+all_data)   
    wb.save("database.xlsx")            #and save the excel file