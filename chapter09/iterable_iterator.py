from collections.abc import Iterator
# 迭代器不支持切片
# 处理大文件

class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employ_list):
        self.iter_list = employ_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word =  self.iter_list[self.index]
        except IndexError:
            raise StopIteration # 迭代器异常
        self.index += 1
        return word
if __name__ == '__main__':
    company = Company(['tom', 'bob', 'jane'])
    my_iter = iter(company)
    # next(my_iter)
    # while True:
    #     try:
    #         print(next(my_iter))
    #     except StopIteration:
    #         pass
    # for item in company:   # __iter__ ==> __getitem__
        # print(item)
    for item in company:
        print(item)