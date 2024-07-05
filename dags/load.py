import pandas as pd
import psycopg2
from psycopg2 import sql
from airflow.decorators import task
from datetime import datetime

@task(task_id='Load')
def load_to_postgresql(df, table_name):
    # Add a date column with the current timestamp
    df['date'] = datetime.now()
    
    # Connection string for psycopg2
    conn_string = "dbname='postgres' host='localhost' user='postgres' password='26111999Map' port=5432"
    
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        # Insert DataFrame rows into the PostgreSQL table
        for index, row in df.iterrows():
            insert_query = sql.SQL("""
                INSERT INTO {table} (news, sentiment, date)
                VALUES (%s, %s, %s)
            """).format(table=sql.Identifier(table_name))
            cursor.execute(insert_query, (row['news'], row['sentiment'], row['date']))
        
        # Commit the transaction
        conn.commit()
        print(f"Data successfully loaded into {table_name} table.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        cursor.close()
        conn.close()