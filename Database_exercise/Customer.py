class Customer:
    def __init__(self, *args):
        self.__name, self.__address, self.__age = args

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def set_name(self, name: str):
        self.__name = name

    def set_address(self, address: str):
        self.__address = address

    def set_age(self, age: int):
        self.__age = age