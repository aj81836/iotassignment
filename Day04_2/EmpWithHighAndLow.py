import mysql.connector
import dbconn

def highest_salary():
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = "SELECT MAX(salary) as Highest_Salary from employee;"

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    # fetch the result
    result = cursor.fetchone()

    # print the result
    print(f"Highest salary in the table: {result[0]}")

    # close cursor and connection
    cursor.close()
    conn.close()

def lowest_salary():
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = "SELECT MIN(salary) as Lowest_Salary from employee;"

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    # fetch the result
    result = cursor.fetchone()

    # print the result
    print(f"Lowest salary in the table: {result[0]}")

    # close cursor and connection
    cursor.close()
    conn.close()

# call the functions to find the highest and lowest salaries in the table
highest_salary()
lowest_salary()
