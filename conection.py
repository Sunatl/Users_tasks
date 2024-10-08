import psycopg2
from secret import database
conn = psycopg2.connect(
        database="Edicationdb",
        user="postgres",
        host='localhost',
        password= database,
        port=5432
    )
