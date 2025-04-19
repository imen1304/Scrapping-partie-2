import pandas as pd
import psycopg2

def load_data():
    conn = psycopg2.connect(
        dbname="scrapping",
        user="postgres",
        password="1",
        host="localhost",
        port="5432"
    )
    query = "SELECT * FROM annonces_automobile"  
    df = pd.read_sql(query, conn)
    conn.close()
    return df
