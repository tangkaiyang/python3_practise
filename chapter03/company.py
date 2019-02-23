class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])
# company1 = company[:2]
print(len(company))

# emploee = company.employee
# for em in emploee:
#     print(em)
# for em in company1:
#     print(em)
#定义了上述魔法函数之后,company变为可迭代类型,直接用for语句循环
#for循环调用迭代器
#没有迭代器就会尝试在类中寻找__getitem__方法
#先寻找__len__,再退而求其次寻找__getitem__