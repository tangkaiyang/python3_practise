from datetime import date, datetime

class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # def get_age(self):
    #     return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("bobby", date(year=1993, month=12, day=28))
    user.age = 30
    print(user._age)
    print(user.age)
    # print(user.get_age())
    # 之前如果设置了age的属
    # 性,后期删除了age字段,不改动代码,
    # 同时直接age属性