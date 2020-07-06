import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

engine = create_engine('sqlite:///chinook.db')

#metadata = MetaData()
#metadata.create_all(engine)
#inspector = inspect(engine)
#cols=inspector.get_columns('employees')
#for row in cols:
#    print(row)
con = engine.connect()
rs = con.execute('SELECT FirstName,LastName FROM employees')
df=pd.DataFrame(rs.fetchall())

print(df.head())