import datetime


class BirthDay():
    count = 0
    def __init__(self, birthday) -> None:
        self.birthday = birthday

        BirthDay.count += 1
    
    # date validator
    def validate(self):

        year, month, day = self.birthday.split("/")
        flag = True
        try:
            birthday = datetime.datetime(
                year=int(year), 
                month=int(month), 
                day=int(day)
            )
        except ValueError:
            flag = False

        if flag:
            today = datetime.datetime.today()
            self.age = today.year - birthday.year

            print(self.age)
        
        else:
            print("WRONG")


date = input()
a = BirthDay(date)
a.validate()


# By Sina Kazemi
# https://github.com/sina96n