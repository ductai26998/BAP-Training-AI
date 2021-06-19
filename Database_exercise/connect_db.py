from mysql import connector


class Database:
    """
        Database class is used to create a object which can connect to mySQL database
        and handle with this database.
        When you initialize a object of Database class, you have to transfer a kawargs
        contains host, user, password, port, database.
    """
    def __init__(self, **kwargs):
        self.__host = kwargs['host']
        self.__user = kwargs['user']
        self.__password = kwargs['password']
        self.__port = kwargs['port']
        self.__database = kwargs['database']
        
        self.__connect_database()

    def __connect_database(self):
        """
            __connect_database function is used to connect to your mySQL Database.
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

    def _get_all(self, sql: str):
        """
            get all record from table database
            input: sql query
            return: an array if get success
        """
        try:
            self.my_cursor.execute(sql)
            data = self.my_cursor.fetchall()
            return data
        except:
            print("Can't get data !!!")

    def _get_item(self, sql: str, *params):
        """
            get the first record which fit with condition
            input: sql query: string, params: tuple contain the conditions
            return: a record tuple if success
        """
        try:
            self.my_cursor.execute(sql, params)
            data = self.my_cursor.fetchone()
            return data
        except:
            print("Can't get data !!!")

    def _insert_item(self, sql: str, *args):
        """
            insert a new record into your table database.
            input: sql query: string, an args contain fields: tuple
        """
        try:
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't Insert !!!")

    def _insert_list(self, sql: str, items):
        """
            insert a new record list into your table database.
            input: sql query: string, items: a list tuple contain the records
        """
        try:
            self.my_cursor.executemany(sql, items)
            self.conn.commit()
        except:
            print("Can't Insert !!!")

    def _update(self, sql: str, *args):
        """
            update a specifically record by old_name in your table database.
            input: sql query: string, a tuple contain the fields
        """
        try:
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't update!!!")

    def _delete(self, sql: str, *params):
        """
           delete a record in your table database by the name record.
           input: sql query: string, params: tuple contain the conditions
        """
        try:
            self.my_cursor.execute(sql, params)
            self.conn.commit()
        except:
            print("Can't delete !!!")

my_db = Database(host='localhost',
                 user='root',
                 password='ductai2207',
                 port='3307',
                 database='bap_ai')
#
# sql = "SELECT * FROM customers WHERE name=%s"
# # print(my_db._get_all())
# name =("eee",)
# print(my_db._get_item(sql, *name))
#
# #
# def testInsert():
#     sql = "INSERT INTO customers(name, address, age) VALUES (%s, %s, %s)"
#     # new_name = input("Enter new name: ")
#     # new_address = input("Enter new address: ")
#     # age = int(input("Enter age: "))
#     # params = (new_name, new_address, age)
#     params = ('ooo', '0', 12)
#     my_db._insert_item(sql, *params)
#
# def testUpdate():
#     sql = "UPDATE customers SET name=%s, address=%s, age=%s WHERE name=%s"
#     old_name = input("Enter customer's name need to update: ")
#     new_name = input("Enter new name: ")
#     new_address = input("Enter new address: ")
#     age = int(input("Enter age: "))
#     params = (new_name, new_address, age, old_name)
#     my_db._update(sql, *params)
#
# def testDelete():
#     sql = "DELETE FROM customers WHERE name=%s"
#     # name = input("Enter customer's name need to delete: ")
#     # tuple(name)
#     name = ("ohh",)
#     my_db._delete(sql, *name)

# testUpdate()
# testInsert()
# testDelete()

# items = [('You', 'ngo quyen', 23), ('Hoc', 'ngo si lien', 20)]
# my_db._insert_list(items)

