from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
import pandas as pd

PUBLIC_IP = "18.132.73.146"
USERNAME = "consultants"
PASSWORD = "WelcomeItc@2022"
DB_NAME = "testdb"
PORT = "5432"
ENCODED_PASSWORD = quote_plus(PASSWORD)

database_url = f"postgresql://{USERNAME}:{ENCODED_PASSWORD}@{PUBLIC_IP}:{PORT}/{DB_NAME}"
# print(database_url)
engine = create_engine(database_url, echo=False)

db1 = pd.read_sql("bank", con=engine)
print(db1)

 # result = pd.read_csv("people_data.csv")
 # result.to_sql('new_table', con=engine, if_exists="replace", index=False)
