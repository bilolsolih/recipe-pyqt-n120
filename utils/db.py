import pymysql
from pymysql import cursors


def create_connection(host="localhost", user="root", password="mysql", database="recipe", port=3306):
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database, port=port, cursorclass=cursors.DictCursor)
        print("Connection to MySQL DB successful")
        return connection
    except Exception as e:
        print(f"Error creating database connection: {e}")
        raise pymysql.Error(e)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Exception as e:
        print(f"The error '{e}' occurred")
        raise pymysql.Error(e)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")
        raise pymysql.Error(e)
