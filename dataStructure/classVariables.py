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


print(Employee.num_of_emp)
emp_1 = Employee('rashmi', 'mohapatra', 30000)
emp_2 = Employee('liti', 'mohapatra', 20000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.__dict__)

# emp_1.raise_amount=1.05
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
print(Employee.num_of_emp)
