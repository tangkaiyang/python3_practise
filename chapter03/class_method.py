class Date:

    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1
    @staticmethod #调用必须加Date.
    def parse_from_string(date_str):
        year, month, day = tuple(date_str.split("-"))
        return Date(int(year), int(month), int(day))
        # 缺点return硬编码,类名改变,这里的Date就要改变
    @classmethod #类方法
    def from_string(cls,date_str ): # 对象从self实例变为cls类本身
        year, month, day = tuple(date_str.split("-"))
        return cls(int(year), int(month), int(day)) # 完善了静态方法的硬编码问题

    @staticmethod # 判断字符串是否为合法的时间字符串
    def valid_str(date_string):
        year, month, day = tuple(date_string.split("-"))
        if int(year)>0 and (0 < int(month) <= 12) and (0 < int(day) <= 31):
            return True
        else:
            return False


    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)

if __name__ == '__main__':
    new_day = Date(2018, 12, 31)
    new_day.tomorrow()
    #tomorrow(new_day)
    print(new_day)

    # 希望传递2018-12-31进类,把下面的逻辑加入类中
    date_str = "2018-12-31"
    year, month, day = tuple(date_str.split("-"))
    new_day = Date(int(year), int(month), int(day))
    print(new_day)

    # 用staticmethod完成初始化
    new_day = Date.parse_from_string(date_str)
    print(new_day)



    # 用classmethod完成初始化
    new_day = Date.from_string(date_str)
    print(new_day)

    # 以上的self和cls只是规范,不是关键词

    print(Date.valid_str("2018-12-31"))