import mariadb

connection = mariadb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "Python",
    database = "Game",
    autocommit = True
)

def get_airport(connection,ICAO):
    ICAO = ICAO.upper()
    sql=f"SELECT ident,name,municipality FROM airport WHERE ident= {ICAO}"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if result:
        for a in result:
            print(f'Airport name:{a[1]}, Location:{a[2]} ')
    else:
        print(f'No record found with this ICAO code')


ICAO = input("Enter the ICAO code of the airport you want: ")
get_airport(connection,ICAO)