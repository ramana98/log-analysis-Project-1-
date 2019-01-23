#!/usr/bin/env python3
import psycopg2

# Database query 1: What are the three most popular articles of all time?
query1 = """select * from firstquery order by amount desc limit 3;"""

# Database query 2: Who are the most popular article authors of all time?
query2 = """select * from secondquery order by total desc;"""

# Database query 3: On which day did more than 1% of requests lead to errors?
query3 = """select * from thirdquery where per>1.0;"""


# Opening and closing connections
def query_db(sql_request):
    try:
        conn = psycopg2.connect(database="news")
    except psycopg2.Error as e:
        print ("Unable to connect to the database")
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results

# Print the top three articles of all time
def toparticles():
    toparticles = query_db(query1)
    print("\n\t\tQuery-1 Print top three articles of all the time\n")
    for title, firstquery in toparticles:
        print(" \"{}\" with {} views".format(title, firstquery))


# Print the top  three authors of all time
def topauthors():
    topauthors = query_db(query2)
    print("\n\t\tQuery-2 Print top three authors of all time\n")
    for name, secondquery in topauthors:
        print(" \"{}\" with {} views".format(name, secondquery))


# Print the days in which there were more than 1% bad requests
def days():
    days = query_db(query3)
    print("\n\t\tQuery-3 Print days with more than one percentage"
          "of bad requests\n")
    for day, thirdquery in days:
        print("""{0:%B %d, %Y} with {1:.2f} % errors
              \n""".format(day, thirdquery))


if __name__ == '__main__':
    toparticles()
    topauthors()
    days()
