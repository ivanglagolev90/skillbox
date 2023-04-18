class Data:
    def __init__(self):
        pass

    @classmethod
    def for_strings(cls, date) -> tuple:
        date_list = date.split('-')
        return f'День: {date_list[0]}\t Месяц: {date_list[1]}\t Год:  {date_list[2]}'

    @classmethod
    def is_valid(cls, date):
        date_list = date.split('-')
        if int(date_list[0]) > 31 or int(date_list[1]) > 12 or int(date_list[2]) > 9999:
            return False
        else:
            return True


date1 = Data.for_strings('10-12-2013')
print(date1)
print(Data.is_valid('10-12-2013'))
print(Data.is_valid('40-12-2013'))
