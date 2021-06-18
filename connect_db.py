from mysql import connector

"""
    Database class is used to create a object which can connect to mySQL database and handle with this database.
    When you initialize a object of Database class, you have to transfer a kawargs contains host, user, password, port, database.
"""
class Database:
    def __init__(self, **kwargs):
        self.__host = kwargs['host']
        self.__user = kwargs['user']
        self.__password = kwargs['password']
        self.__port = kwargs['port']
        self.__database = kwargs['database']

    """
        connect_database function is used to connect to your mySQL Database.
    """
    def connect_database(self):
        try:
            self.conn = connector.connect(host=self.__host,
                                          user=self.__user,
                                          password=self.__password,
                                          port=self.__port,
                                          database=self.__database)
            self.my_cursor = self.conn.cursor()
        except:
            print("Can't connect database !!!")

    """
        insert function is used to insert a new record into your table database.
        It receive an args contain name, address, age make variable
    """
    def insert(self, *args):
        try:
            sql = "INSERT INTO customers(name, address, age) VALUES (%s, %s, %s)"
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't Insert !!!")

    """
        update function is used to update a specifically record by old_name in your table database.
        It receive an args contain new_name, new_address, new_age and old_name in the same order as above make variable
    """
    def update(self, *args):
        try:
            sql = "UPDATE customers SET name=%s, address=%s, age=%s WHERE name=%s"
            self.my_cursor.execute(sql, args)
            self.conn.commit()
        except:
            print("Can't update!!!")

    """
        delete function is used to delete a record in your table database by the name record.
        It receive an args contain new_name, new_address, new_age and old_name in the same order as above make variable
    """
    def delete(self, name):
        try:
            sql = "DELETE FROM customers WHERE name='{}'".format(name)
            self.my_cursor.execute(sql)
            self.conn.commit()
        except:
            print("Can't delete !!!")

my_db = Database(host='localhost',
                 user='root',
                 password='ductai2207',
                 port='3307',
                 database='bap_ai')
my_db.connect_database()
#
# def testInsert():
#     new_name = input("Enter new name: ")
#     new_address = input("Enter new address: ")
#     age = int(input("Enter age: "))
#     my_db.insert(new_name, new_address, age)
#
# def testUpdate():
#     old_name = input("Enter customer's name need to update: ")
#     new_name = input("Enter new name: ")
#     new_address = input("Enter new address: ")
#     age = int(input("Enter age: "))
#     my_db.update(new_name, new_address, age, old_name)
#
# def testDelete():
#     name = input("Enter customer's name need to delete: ")
#     my_db.delete(name)

# testUpdate()
# testInsert()
# testDelete()

# my_db.insert("aaaa", "ffff", 122)

