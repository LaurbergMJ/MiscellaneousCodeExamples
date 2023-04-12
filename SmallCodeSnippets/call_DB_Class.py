from databaseConnectioClass import *
try:
    with open(path, 'r') as file:
        full_data = pd.read_csv(file, sep=',')
except Exception as e:
        print(e)

access_info = {
    'DRIVER' : 'SQL Server',
    'Server' : 'DWPROD', 
    'Database' : 'RiskDatamart', 
    'Trusted_connection' : 'Yes',
    }

try:
    with Database(access_info) as db:
        bondData = db.query_tbl(x, (PARAMS**)) # Notice that params needs to be a tuple, even if there is only one parameter!
                                                   # x is a string containing a SQL statement as a string 

except:
    print('Error in connection')

try:
    with Database(access_info) as db_:
        Fwd_bond = db_.query_tbl(x, (PARAMS)) # x is a string containing a SQL statement as a string
except:
    print('Error in connection')