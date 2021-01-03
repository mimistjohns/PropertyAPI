'''
Filename: application.py
Author:   Mimi St Johns
Created:  12/30/2020
Last Modified:  1/2/2020
Python Version: 3.8
'''
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
db = SQLAlchemy(app)
#Create Model
engine = create_engine('sqlite:///my_data.db', echo=True)
Base = declarative_base(engine)

class Homes(Base):
    __tablename__ = 'redfinData'
    __table_args__ = {"autoload": True}


def loadSession():
    Session = sessionmaker(bind=engine)
    return Session()

session = loadSession()

res = session.execute('select * from redfinData order by :val', {'val': 'PRICE'})
for item in res:
    break
#Home Endpoint
@app.route('/')
def home():
    return get_sorted('"DAYS ON MARKET"', 'asc')
#Display all info related to a specific property
@app.route('/address/<id>')
def get_data(id):
    session = loadSession()
    res = session.execute('select * from redfinData where ADDRESS = :val', {'val': id})
    for item in res:
        return dict(item)

#Sort by specified parameters
@app.route('/sorted/<column>/<sort>')
def get_sorted(column, sort):
    session = loadSession()
    sort_ = 'asc' if sort == 'asc' else 'desc'
    where = ''

    for key, val in dict(request.args).items():
        if key.endswith('min'):
            mode = '>='
        elif key.endswith('max'):
            mode = '<='
        else:
            continue
        if not where:
            where = ' where '
        else:
            where = where + 'and '
        col = key.split('_')[0].upper()
        where += f'{col} {mode} {val} '

    cmd_str = f'select * from redfinData'# order by {column} {sort_}'

    cmd_str += f'{where} order by {column} {sort_}'
    cmd = text(cmd_str)
    res = session.execute(cmd)
    results = []
    keys = ['ADDRESS', 'PRICE', 'LOCATION', 'BEDS', 'BATHS', 'DAYS ON MARKET']
    for item in res:
        data = {}
        for key in keys:
            data[key] = item[key]
        results.append(data)
    return {'results': results}



app.run()
