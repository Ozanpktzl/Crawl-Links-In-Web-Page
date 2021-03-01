import mariadb
import sys
try:
    conn = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        port=3306,
        database="deneme"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute(
    "SELECT search_engine,url FROM list",)
with open('wordlist.txt', 'w') as the_file: #w
    for (search_engine, url) in cur:
        print(f"First Name: {search_engine}, Last Name: {url}")
        the_file.write(f"{url}\n")