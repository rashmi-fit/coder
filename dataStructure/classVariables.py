class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last,pay=emp_str.split('-')
        cls(first,last,pay)


print(Employee.num_of_emp)
emp_1 = Employee('rashmi', 'mohapatra', 30000)
emp_2 = Employee('liti', 'mohapatra', 20000)

emp_str_1="John-doe-7000"
emp_str_2="steve-smit-3000"
emp_str_3="jane-Dow-9000"


new_emp_1= Employee.from_string(emp_str_1)


print(new_emp_1.email)
print(new_emp_1.pay)


# # print(emp_1.pay)
# # emp_1.apply_raise()
# # print(emp_1.pay)
# # print(Employee.__dict__)
# Employee.set_raise_amt(1.05)
# emp_1.set_raise_amt(1.05)
# print(Employee.raise_amount)
# # emp_1.raise_amount=1.05
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# print(Employee.num_of_emp)
print(help(Employee))
