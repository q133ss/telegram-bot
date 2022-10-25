from mysql.connector import connect, Error

class Order:
    def insert(self, name='-', login='-'):
        try:
            with connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="anpei",
            ) as connection:
                with connection.cursor() as cursor:
                    create_db_query = "INSERT into `orders` (name, login) VALUES  (%s, %s)"
                    reviewers_records = [(name,login)]
                    cursor.executemany(create_db_query,
                                       reviewers_records)
                    connection.commit()
        except Error as e:
            print(e)