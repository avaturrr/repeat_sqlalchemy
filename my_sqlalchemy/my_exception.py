class MyException(Exception):
    def __init__(self, message="It's not int"):
        super().__init__(message)