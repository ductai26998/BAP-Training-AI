from mysql import connector


class Database:
    """
        Database class is used to create a object which can connect to mySQL database and handle with this database.
        When you initialize a object of Database class, you have to transfer a kawargs contains host, user, password, port, database.
    """
    def __init__(self, **kwargs):
        self.__host = kwargs['host']
        self.__user = kwargs['user']
        self.__password = kwargs['password']
        self.__port = kwargs['port']
        self.__database = kwargs['database']

    def connect_database(self):
        """
            connect_database function is used to connect to your mySQL Database.
        """
        try:
            self.conn = connector.connect(host=self.__host,
                                          user=self.__user,
                                          password=self.__password,
                                          port=self.__port,
                                          database=self.__database)
            self.my_cursor = self.conn.cursor(buffered=True)
        except:
            print("Can't connect database !!!")

    def get(self):
        try:
            sql = "SELECT * FROM customers"
            data = self.my_cursor.execute(sql)
            print(data)
        except:
            print("Can't get data !!!")

    def insert_item(self, sql: str, *args):
        """
            insert function is used to insert a new record into your table database.
            It receive an args contain name, address, age make variable
        """
        try:
            # sql = "INSERT INTO customers(name, address, age) VALUES (%s, %s, %s)"
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't Insert !!!")

    def insert_list(self, items):
        """
            insert function is used to insert a new record into your table database.
            It receive an args contain name, address, age make variable
        """
        try:
            sql = "INSERT INTO customers(name, address, age) VALUES (%s, %s, %s)"
            self.my_cursor.executemany(sql, items)
            self.conn.commit()
        except:
            print("Can't Insert !!!")

    def update(self, sql: str, *args):
        """
            update function is used to update a specifically record by old_name in your table database.
            It receive an args contain new_name, new_address, new_age and old_name in the same order as above make variable
        """
        try:
            # sql = "UPDATE customers SET name=%s, address=%s, age=%s WHERE name=%s"
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't update!!!")

    def delete(self, sql: str, *param):
        """
           delete function is used to delete a record in your table database by the name record.
           It receive an args contain new_name, new_address, new_age and old_name in the same order as above make variable
        """
        try:
        # sql = "DELETE FROM customers WHERE name=%s"
            self.my_cursor.execute(sql, param)
            self.conn.commit()
        except:
            print("Can't delete !!!")

my_db = Database(host='localhost',
                 user='root',
                 password='ductai2207',
                 port='3307',
                 database='bap_ai')
my_db.connect_database()

my_db.get()
#
def testInsert():
    sql = "INSERT INTO customers(name, address, age) VALUES (%s, %s, %s)"
    new_name = input("Enter new name: ")
    new_address = input("Enter new address: ")
    age = int(input("Enter age: "))
    params = (new_name, new_address, age)
    my_db.insert_item(sql, *params)

def testUpdate():
    sql = "UPDATE customers SET name=%s, address=%s, age=%s WHERE name=%s"
    old_name = input("Enter customer's name need to update: ")
    new_name = input("Enter new name: ")
    new_address = input("Enter new address: ")
    age = int(input("Enter age: "))
    params = (new_name, new_address, age, old_name)
    my_db.update(sql, *params)

def testDelete():
    sql = "DELETE FROM customers WHERE name=%s"
    name = input("Enter customer's name need to delete: ")
    my_db.delete(sql, *name)

# testUpdate()
# testInsert()
# testDelete()

# items = [('You', 'ngo quyen', 23), ('Hoc', 'ngo si lien', 20)]
# my_db.insert_list(items)
