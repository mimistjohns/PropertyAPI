'''
Filename: homes.py
Author:   Mimi St Johns
Created:  12/30/2020
Last Modified:  1/2/2020
Python Version: 3.8
'''
import pandas as pd
import sqlite3

conn = sqlite3.connect('my_data.db')
c = conn.cursor()
users = pd.read_csv('redfinData.csv')
# write the data to a sqlite table
users.to_sql('redfinData', conn, if_exists='append', index = False)
c.execute('''SELECT * FROM redfinData''').fetchall()


