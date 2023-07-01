class Employee:
    def __init__(self, idnum, name, role):
        self.idnum = idnum
        self.name = name
        self.role = role


class ManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, idnum, name, role):
        employee = Employee(idnum, name, role)
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def update_employee(self, idnum, name, role):
        for employee in self.employees:
            if employee.idnum == idnum:
                employee.name = name
                employee.role = role
                print(f"Employee {employee.name} updated successfully.")
                return
        print(f"Employee with ID {idnum} not found.")

    def delete_employee(self, idnum):
        for employee in self.employees:
            if employee.idnum == idnum:
                self.employees.remove(employee)
                print(f"Employee {employee.name} deleted successfully.")
                return
        print(f"Employee with ID {idnum} not found.")

    def display_employees(self):
        print("Employee List:")
        for employee in self.employees:
            print(f"ID: {employee.idnum}, Name: {employee.name}, Position: {employee.role}")


# Example usage
management_system = ManagementSystem()

# Adding employees
management_system.add_employee(1, "Joe Mama", "Manager")
management_system.add_employee(2, "Jimmy Neutron", "Associate")
management_system.add_employee(3, "Doug Dimmadome", "Assistant Manager")

# Displaying employee list
management_system.display_employees()

# Updating an employee
management_system.update_employee(2, "Timmy Turner", "Senior Developer")

# Deleting an employee
management_system.delete_employee(3)

# Displaying updated employee list
management_system.display_employees()
