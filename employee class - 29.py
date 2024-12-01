class Employee:
    def _init_(self, name, Id, position):
        self.name = name
        self.Id = Id
        self.position = position

    def displayEmployee(self):
        print(f"The mf name is {self.name}, they have an ID: {self.Id}, and that mf has a position is {self.position}")


class Address:
    def _init_(self, street, state, country):
        self.street = street
        self.state = state
        self.country = country

    def display_address(self):
        print(f"Street: {self.street}")
        print(f"State: {self.state}")
        print(f"Country: {self.country}")


class EmployeeAddress(Employee, Address):
    def _init_(self, name, Id, position, street, state, country):
        Employee._init_(self, name, Id, position)
        Address._init_(self, street, state, country)

    def display_full_info(self):
        self.displayEmployee()  
        self.display_address()   


employee1 = EmployeeAddress("MESSI", "9041", "FOOTBALL", "RONALDO STREET", "California", "USA")

employee1.display_full_info()
