# working with classes
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # def fullname():
    #     return '{} {}'.format(self.first, self.last)


emp_1 = Employee('rashmi', 'mohapatra', 50000)
emp_2 = Employee('liti', 'moha', 20000)

# print(emp_1.email)
# print(emp_2.email)

emp_1.fullname()
Employee.fullname(emp_1)
print(emp_1.fullname())
# print(emp_2.fullname())
