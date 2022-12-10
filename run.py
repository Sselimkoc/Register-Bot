import openpyxl,time
from web_selen import Login
from create_database import create_db

create_db()    # firstly create our database from the data

wb = openpyxl.load_workbook("database.xlsx")
ws = wb.active
with Login() as login:               
    rows= ws.iter_rows(2,5,2,5)        #we reach our data from the  table 
    for a,b,c,d in rows:               # each of one contains special attribute
        login.first_page()         
        time.sleep(3)
        login.register_button_handler()
        time.sleep(3)
        login.fill_page(a.value,b.value,c.value,d.value)
        time.sleep(3)
        login.register_page()