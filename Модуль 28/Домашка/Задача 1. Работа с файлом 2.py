import os
import io


class File:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __enter__(self):
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()
            self.file = open(self.file_name, 'w')
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type and issubclass(exc_type, IOError):
            return True


with File('example.txt') as file:
    file.write('Всем привет!')