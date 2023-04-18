class File:
  def __init__(self, name, status):
    self.name = name
    self.status = status

  def __enter__(self):
    self.file = open(self.name, self.status)
    return self.file

  def __exit__(self): #нет исключений
    self.file.close()


with File('example.txt', 'w') as file:
  file.write('Всем привет!')