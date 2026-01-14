import pandas as pd
import sqlalchemy
import psycopg2

data = pd.read_csv('C:\python_data_analysis_project\Sources\customer_shopping_behavior.csv')
# print(data.tail())

data.columns = data.columns.str.lower()
data.columns = data.columns.str.replace(" ","_")
data.rename(columns={'purchase_amount_(usd)':'purchase_amount'},inplace=True)
# print(data.columns)
# print(data.isnull().sum()) 
data['review_rating'] = data.groupby('category')['review_rating'].transform(lambda x : x.fillna(x.median()))
# print(data.isnull().sum()) 
labels =["Young Adult","Adult","Middle_Aged","Senior"]
data['age_group'] = pd.qcut(data['age'],q=4,labels = labels)
# print(data[['age_group','age']].head())

frequency ={
 "Fortnightly" :14,
 "Weekly" : 7,
"Annually" : 365,
 "Quarterly" : 90,
 "Every 3 Months" : 90,
 "Bi-Weekly":14
}
data['purchase_frequency_days']= data['frequency_of_purchases'].map(frequency)
# print((data['discount_applied']==data['promo_code_used']).all())
data.drop('promo_code_used',axis=1)
print(data.head())

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
from sqlalchemy import create_engine

username = "postgres"      # default user
password = "1234"      # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "customer_behavior"  # the database you created in pgAdmin

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"    # choose any table name
data.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
