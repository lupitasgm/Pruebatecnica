import pyodbc

def connectDB():
    SERVER = 'DESKTOP-1G83COF'
    DATABASE = 'GestionEmpleados'
    USERNAME = 'sa'
    PASSWORD = '123456'

    connectionString = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    conn = pyodbc.connect(connectionString) 
    return conn