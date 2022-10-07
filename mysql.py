from sqlalchemy import create_engine
import pandas as pd
import os

hostname = '35.223.129.10' # external IP address
user = os.environ.get('username')
pwd = os.environ.get('password')
database = 'db1' 

# connect to mysql
connection_string = f'mysql+pymysql://{user}:{pwd}@{hostname}/{database}'

db = create_engine(connection_string) 


# load data 
df = pd.read_csv('https://raw.githubusercontent.com/rimashah1/hha-data-cleaning/main/data/School_Learning_Modalities.csv')

# push data to database 'db1'
df.to_sql('school_learning_modalities', con=db, if_exists='replace')