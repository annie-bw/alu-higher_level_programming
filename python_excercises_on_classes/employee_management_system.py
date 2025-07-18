from abc import ABC, abstractmethod
class Person:
    def __init__(self, name,age):
        self.name =name
        self.age= age

class Employee(Person):
    def __init__(self,name,age,role,salary):
        super().__init__(name,age)
        self.role=role
        self.__salary=salary

    @property
    def salary(self):
        return self.__salary
   

class Manager(Employee):
      def employee_details(self):
          return super().employee_details()

emp= Employee("Bwiza Annie", "20", "Developer", "3000")
emp.salary
