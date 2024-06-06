import sqlalchemy
import pandas as pd

def fetch_data(table_name, fields, connection_string):
    engine = sqlalchemy.create_engine(connection_string)
    query = f"SELECT {', '.join(fields)} FROM {table_name}"
    with engine.connect() as conn:
        data = pd.read_sql(query, conn)
    return data
