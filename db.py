import psycopg2

def conn():
    return psycopg2.connect(
            host="localhost",
            database="mydb",
            user="postgres",
            password="postgrespw"
        )