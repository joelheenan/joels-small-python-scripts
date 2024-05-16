import pyodbc

def connect_to_db(db_file):
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=' + db_file + ';'
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    return cursor

def get_data_from_db(cursor, table_name):
    cursor.execute(f'SELECT * FROM {table_name}')
    return cursor.fetchall()

def compare_dbs(db1_file, db2_file, table_name):
    cursor1 = connect_to_db(db1_file)
    cursor2 = connect_to_db(db2_file)

    db1_data = get_data_from_db(cursor1, table_name)
    db2_data = get_data_from_db(cursor2, table_name)

    if db1_data != db2_data:
        print('Differences found:')
        print('DB1 data:', db1_data)
        print('DB2 data:', db2_data)
    else:
        print('No differences found.')

# replace with your file paths and table name
db1_file = r'path\to\your\firstDB.accdb'
db2_file = r'path\to\your\secondDB.accdb'
table_name = 'your_table_name'

compare_dbs(db1_file, db2_file, table_name)
