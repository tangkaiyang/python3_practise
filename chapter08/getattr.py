# __getattr__, __getattribute__
# __getattr__ 就是在查找不到属性时调用
from datetime import date
class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        # return "not find attr"
        return self.info[item]

    def __getattribute__(self, item):  # 无条件返回,尽量不覆盖
        return "bobby"


if __name__ == "__main__":
    user = User("bobby", date(year=1993, month=12, day=28), info={"company_name": "immoc"})
    print(user.company_name)
    print(user.name)
    print(user.jfj)