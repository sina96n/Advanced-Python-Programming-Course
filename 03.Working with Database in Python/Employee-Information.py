import mysql.connector as mysql

# creating connection with database
con = mysql.connect(
    user="username",
    password="password",
    database="employee"
)
# creating a cursor
cur = con.cursor()

# writing query to extract all of rows in database ordered by height and weight
query = "select * from workers order by height desc, weight asc"
cur.execute(query)
results = cur.fetchall()

# commiting changes (no changes applied in this case)
con.commit()
# closing connection
con.close()


# printing output
for i in results:
    print(f"{i[0]} {i[2]} {i[1]}")



# By Sina Kazemi
# https://github.com/sina96n